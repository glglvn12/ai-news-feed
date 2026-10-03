from fetch import merge, page_date, parse_deepmind_publications, parse_feed, parse_github_trending

RSS = b"""<rss version="2.0"><channel><item><title>GPT &amp; news</title><link>https://a.com/1</link>
<pubDate>Wed, 30 Sep 2026 12:00:00 GMT</pubDate><description>&lt;p&gt;Hello &lt;b&gt;world&lt;/b&gt;&lt;/p&gt;</description></item></channel></rss>"""

ATOM = b"""<feed xmlns="http://www.w3.org/2005/Atom"><entry><title>v1.2</title>
<link rel="alternate" href="https://b.com/2"/><updated>2026-10-01T08:00:00Z</updated><content>notes</content></entry></feed>"""

r = parse_feed(RSS)[0]
assert r == {"title": "GPT & news", "url": "https://a.com/1", "date": "2026-09-30T12:00:00+00:00", "excerpt": "Hello world"}, r
a = parse_feed(ATOM)[0]
assert a["url"] == "https://b.com/2" and a["date"] == "2026-10-01T08:00:00+00:00" and a["title"] == "v1.2", a

# merge: dedupe by URL, keep old date when new is missing, newest first, drop old items
old = [dict(r, source="A"), {"url": "https://x.com/old", "title": "t", "date": "2000-01-01T00:00:00+00:00"}]
new = [dict(r, date=None, title="updated"), a]
m = merge(old, new, keep_days=100000)
assert [i["url"] for i in m] == ["https://b.com/2", "https://a.com/1", "https://x.com/old"], m
assert m[1]["title"] == "updated" and m[1]["date"] == r["date"]
assert len(merge(old, new, keep_days=1000)) == 2

assert page_date('<meta property="article:published_time" content="2025-12-01T19:56:35+00:00">') == "2025-12-01T19:56:35+00:00"
assert page_date("Updated Sep 28, 2026 · Sep 15, 2026 ... Sep 15, 2026").startswith("2026-09-15")
assert page_date("no date") is None
TRENDING = b"""<article class="Box-row"><h2 class="h3"> <a href="/acme/agent">acme / agent</a></h2>
<p class="col-9 color-fg-muted">An &amp; agent</p><span itemprop="programmingLanguage">Python</span> 1,435 stars today</article>"""
t = parse_github_trending(TRENDING, {})[0]
assert t["title"] == "acme/agent" and t["url"] == "https://github.com/acme/agent", t
assert t["excerpt"] == "Python · 1,435 stars today — An & agent", t
old_date = "2026-01-01T00:00:00+00:00"
assert parse_github_trending(TRENDING, {t["url"]: {"date": old_date}})[0]["date"] == old_date
DM = b"""<ul class=list-group><li class=list-group__item><a class=list-group__link href=https://deepmind.google/research/publications/265605/>
<dl><dd><span class=list-group__date> 1 September 2026 </span></dd><dd><span class=list-group__description>Proactive &amp; Partners</span></dd></dl></a></li></ul>"""
d = parse_deepmind_publications(DM)[0]
assert d == {"title": "Proactive & Partners", "url": "https://deepmind.google/research/publications/265605/",
             "date": "2026-09-01T00:00:00+00:00", "excerpt": ""}, d
print("ok")
