"""Fetch all sources in sources.json and write items.json. Stdlib only."""
import gzip
import html
import json
import re
import sys
import urllib.request
import xml.etree.ElementTree as ET
from collections import Counter
from datetime import datetime, timedelta, timezone
from email.utils import parsedate_to_datetime
from pathlib import Path

ROOT = Path(__file__).parent
OUT = ROOT / "items.json"
KEEP_DAYS = 60
DEFAULT_LIMIT = 20
UA = "Mozilla/5.0 (compatible; ai-news-aggregator)"


def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=20) as r:
        data = r.read()
    # Some sites (e.g. deepmind.google) send gzip even when it wasn't requested.
    return gzip.decompress(data) if data[:2] == b"\x1f\x8b" else data


def clean(text, n=300):
    text = html.unescape(re.sub(r"<[^>]+>", " ", text or ""))
    text = re.sub(r"\s+", " ", text).strip()
    return text if len(text) <= n else text[: n - 1].rstrip() + "…"


def iso(value):
    """RFC 822 (RSS) or ISO 8601 (Atom/JSON) -> UTC ISO string, or None."""
    if not value:
        return None
    value = value.strip()
    try:
        dt = parsedate_to_datetime(value)
    except (TypeError, ValueError):
        try:
            dt = datetime.fromisoformat(value.replace("Z", "+00:00"))
        except ValueError:
            return None
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return dt.astimezone(timezone.utc).isoformat(timespec="seconds")


def parse_feed(data):
    """RSS 2.0 or Atom bytes -> list of {title, url, date, excerpt}."""
    root = ET.fromstring(data)
    # Drop namespaces so RSS and Atom use the same tag names.
    for el in root.iter():
        if isinstance(el.tag, str) and "}" in el.tag:
            el.tag = el.tag.split("}", 1)[1]
    out = []
    for e in root.iter("item"):
        out.append({
            "title": clean(e.findtext("title"), 200),
            "url": (e.findtext("link") or e.findtext("guid") or "").strip(),
            "date": iso(e.findtext("pubDate") or e.findtext("date")),
            "excerpt": clean(e.findtext("description")),
        })
    for e in root.iter("entry"):
        link = e.find("link[@rel='alternate']")
        if link is None:
            link = e.find("link")
        out.append({
            "title": clean(e.findtext("title"), 200),
            "url": (link.get("href") if link is not None else "").strip(),
            "date": iso(e.findtext("published") or e.findtext("updated")),
            "excerpt": clean(e.findtext("summary") or e.findtext("content")),
        })
    return out


def parse_hf_papers(data):
    return [{
        "title": clean(p["paper"]["title"], 200),
        "url": "https://huggingface.co/papers/" + p["paper"]["id"],
        "date": iso(p.get("publishedAt")),
        "excerpt": clean(p["paper"].get("summary")),
    } for p in json.loads(data)]


def parse_hf_models(data):
    return [{
        "title": "New model: " + m["id"],
        "url": "https://huggingface.co/" + m["id"],
        "date": iso(m.get("createdAt")),
        "excerpt": "",
    } for m in json.loads(data)]


def parse_github_trending(data, known):
    """github.com/trending has no API; scrape its repo list. Date = first time a repo was seen
    trending (kept across runs), so a repo doesn't jump back to the top every hour."""
    now = datetime.now(timezone.utc).isoformat(timespec="seconds")
    out = []
    for a in re.findall(r'<article class="Box-row">(.*?)</article>', data.decode("utf-8", "replace"), re.S):
        name = re.search(r'<h2[^>]*>\s*<a[^>]*href="/([^"]+)"', a)
        if not name:
            continue
        url = "https://github.com/" + name.group(1)
        desc = re.search(r'<p class="[^"]*col-9[^"]*">(.*?)</p>', a, re.S)
        lang = re.search(r'itemprop="programmingLanguage">([^<]+)', a)
        stars = re.search(r"([\d,]+) stars? (today|this week|this month)", a)
        meta = " · ".join(x for x in [
            lang.group(1).strip() if lang else "",
            f"{stars.group(1)} stars {stars.group(2)}" if stars else ""] if x)
        out.append({
            "title": name.group(1),
            "url": url,
            "date": known[url]["date"] if url in known else now,
            "excerpt": clean((meta + " — " if meta else "") + (desc.group(1) if desc else "")),
        })
    return out


def parse_deepmind_publications(data):
    """deepmind.google/research/publications/: a dated list with no feed."""
    out = []
    for li in re.findall(r"<li class=list-group__item>(.*?)</li>", data.decode("utf-8", "replace"), re.S):
        href = re.search(r"href=[\"']?([^\"' >]+)", li)
        date = re.search(r"list-group__date>\s*([^<]+?)\s*<", li)
        title = re.search(r"list-group__description>([^<]+)<", li)
        if not (href and date and title):
            continue
        out.append({
            "title": clean(title.group(1), 200),
            "url": href.group(1),
            "date": datetime.strptime(date.group(1), "%d %B %Y").replace(tzinfo=timezone.utc).isoformat(),
            "excerpt": "",
        })
    return out


def page_date(page):
    """Best-guess publish date from a post's HTML: published_time meta, else the most
    repeated 'Sep 15, 2026'-style date on the page. ponytail: heuristic, add per-site
    parsers if a site starts showing wrong dates."""
    m = re.search(r'published_time" content="([^"]+)"', page)
    if m:
        return iso(m.group(1))
    dates = re.findall(r"\b(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]* \d{1,2}, \d{4}", page)
    if dates:
        best = Counter(dates).most_common(1)[0][0]
        return datetime.strptime(best[:3] + best[best.index(" "):], "%b %d, %Y").replace(tzinfo=timezone.utc).isoformat()
    return None


def parse_github_releases(data):
    """GitHub releases API, stable releases only (skips rc/canary prereleases)."""
    return [{
        "title": r["name"] or r["tag_name"],
        "url": r["html_url"],
        "date": iso(r["published_at"]),
        "excerpt": clean(r.get("body")),
    } for r in json.loads(data) if not r["prerelease"] and not r["draft"]]


def parse_links(data, src, known):
    """Sites with no feed: collect post links matching src['pattern'], read title/date from each
    new post page. Falls back to first-seen time when the page has no date."""
    base = src["url"].split("/", 3)[:3]
    pat = re.compile(src["pattern"])
    urls = []
    # Works on an HTML listing page (href) or a sitemap.xml (<loc>).
    for href in re.findall(r'href="([^"#?]+)"|<loc>([^<]+)</loc>', data.decode("utf-8", "replace")):
        href = "".join(href).strip()
        if href.startswith("./") or href.startswith("/"):
            href = "/".join(base) + "/" + href.lstrip("./")
        href = href.rstrip("/")
        if pat.match(href) and href not in urls:
            urls.append(href)
    now = datetime.now(timezone.utc).isoformat(timespec="seconds")
    out = []
    for url in urls:
        if url in known:
            out.append(known[url])
            continue
        title, excerpt, date = url.rsplit("/", 1)[1].replace("-", " ").capitalize(), "", None
        try:
            page = get(url).decode("utf-8", "replace")
            m = re.search(r'<meta property="og:title" content="([^"]*)"', page)
            title = clean(m.group(1), 200) if m else title
            m = re.search(r'<meta (?:property="og:description"|name="description") content="([^"]*)"', page)
            excerpt = clean(m.group(1)) if m else ""
            date = page_date(page)
        except Exception as e:
            print(f"  ! {url}: {e}", file=sys.stderr)
        item = {"title": title, "url": url, "date": date or now, "excerpt": excerpt}
        if not date:
            item["date_estimated"] = True
        out.append(item)
    return out


def fetch_source(src, known):
    data = get(src["url"])
    kind = src["type"]
    if kind == "rss":
        items = parse_feed(data)
    elif kind == "hf_papers":
        items = parse_hf_papers(data)
    elif kind == "hf_models":
        items = parse_hf_models(data)
    elif kind == "deepmind_publications":
        items = parse_deepmind_publications(data)
    elif kind == "github_trending":
        items = parse_github_trending(data, known)
    elif kind == "github_releases":
        items = parse_github_releases(data)
    elif kind == "links":
        items = parse_links(data, src, known)
    else:
        raise ValueError(f"unknown type {kind}")
    items = [i for i in items if i["url"] and i["title"]]
    if "include" in src:  # optional regex: keep only items whose title or excerpt matches
        pat = re.compile(src["include"], re.I)
        items = [i for i in items if pat.search(i["title"] + " " + i["excerpt"])]
    items.sort(key=lambda i: i["date"] or "", reverse=True)
    for i in items:
        i["source"], i["category"] = src["name"], src["category"]
    return items[: src.get("limit", DEFAULT_LIMIT)]


def merge(old, new, keep_days=KEEP_DAYS):
    """Dedupe by URL (newest fetch wins, but keeps the old date if the new one is missing),
    drop items older than keep_days, sort newest first."""
    by_url = {i["url"]: i for i in old}
    for i in new:
        prev = by_url.get(i["url"])
        if prev and not i["date"]:
            i["date"] = prev["date"]
        by_url[i["url"]] = i
    cutoff = (datetime.now(timezone.utc) - timedelta(days=keep_days)).isoformat()
    items = [i for i in by_url.values() if (i["date"] or "") >= cutoff]
    return sorted(items, key=lambda i: i["date"], reverse=True)


def main():
    sources = json.loads((ROOT / "sources.json").read_text())
    old = json.loads(OUT.read_text())["items"] if OUT.exists() else []
    known = {i["url"]: i for i in old}
    new, failed = [], []
    for src in sources:
        try:
            items = fetch_source(src, known)
            print(f"{len(items):3d}  {src['name']}")
            new += items
        except Exception as e:
            print(f"  !  {src['name']}: {e}", file=sys.stderr)
            failed.append(src["name"])
    items = merge(old, new)
    # Re-tag saved items too, so moving a source to another category applies everywhere.
    cats = {src["name"]: src["category"] for src in sources}
    for i in items:
        i["category"] = cats.get(i["source"], i["category"])
    OUT.write_text(json.dumps({
        "updated": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "failed": failed,
        "items": items,
    }, ensure_ascii=False, indent=1))
    print(f"{len(items)} items written, {len(failed)} sources failed")


if __name__ == "__main__":
    main()
