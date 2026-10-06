"""Serve the static review website locally with clean-route fallback."""
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import os
os.chdir(Path(__file__).resolve().parent)
class PreviewHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        target = Path(self.translate_path(self.path))
        if not target.exists() and not self.path.split('?')[0].startswith(('/assets/', '/data/')):
            self.path = '/index.html'
        super().do_GET()
print('Sambecca’s Closet preview: http://localhost:8000')
ThreadingHTTPServer(('127.0.0.1', 8000), PreviewHandler).serve_forever()
