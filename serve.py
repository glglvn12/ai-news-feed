"""Local server: serves the site and runs fetch.py on POST /refresh."""
import threading
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer

import fetch

lock = threading.Lock()


class Handler(SimpleHTTPRequestHandler):
    def do_POST(self):
        if self.path != "/refresh":
            return self.send_error(404)
        if not lock.acquire(blocking=False):
            return self.send_error(409, "Refresh already running")
        try:
            fetch.main()
            self.send_response(204)
            self.end_headers()
        except Exception as e:
            self.send_error(500, str(e))
        finally:
            lock.release()


if __name__ == "__main__":
    print("http://localhost:8123")
    ThreadingHTTPServer(("127.0.0.1", 8123), Handler).serve_forever()
