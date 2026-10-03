#!/usr/bin/env bash
# Fetch the latest news, start the local server, and open the site.
# Double-click this file in Finder (or run ./launch.command). Stop with Ctrl+C or close the window.
set -e
cd "$(dirname "$0")"
URL="http://localhost:8123"

open_site() {
  if command -v open >/dev/null; then open "$URL"
  elif command -v xdg-open >/dev/null; then xdg-open "$URL"
  else echo "Open $URL in your browser."; fi
}

if curl -s -o /dev/null "$URL"; then
  echo "Server already running at $URL"
  open_site
  exit 0
fi

echo "Fetching news…"
python3 fetch.py || echo "Fetch failed, showing saved data."

python3 serve.py &
SERVER=$!
trap 'kill $SERVER 2>/dev/null' EXIT INT TERM HUP

for _ in $(seq 20); do
  curl -s -o /dev/null "$URL" && break
  sleep 0.25
done
open_site
echo "Running at $URL. Press Ctrl+C to stop."
wait $SERVER
