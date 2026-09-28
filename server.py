# Smart SPA Server for Voomi Clone
import os, sys, mimetypes
from http.server import HTTPServer, SimpleHTTPRequestHandler

mimetypes.add_type('application/javascript', '.js')
mimetypes.add_type('text/css', '.css')
mimetypes.add_type('font/woff2', '.woff2')
mimetypes.add_type('font/woff', '.woff')
mimetypes.add_type('image/svg+xml', '.svg')
mimetypes.add_type('image/webp', '.webp')
mimetypes.add_type('audio/mpeg', '.mp3')
mimetypes.add_type('video/mp4', '.mp4')
mimetypes.add_type('application/manifest+json', '.webmanifest')

ASSET_PREFIXES = ('/assets/', '/sounds/', '/lp/', '/data/')
KNOWN_EXTENSIONS = {
    '.js', '.css', '.woff2', '.woff', '.svg', '.png', '.jpg', '.jpeg',
    '.webp', '.mp3', '.mp4', '.json', '.webmanifest', '.ico'
}

class SPARequestHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', '*')
        super().end_headers()

    def do_OPTIONS(self):
        self.send_response(200)
        self.end_headers()

    def do_GET(self):
        # Clean path
        clean_path = self.path.split('?')[0].split('#')[0]

        # Resolve filesystem path
        path = self.translate_path(clean_path)
        
        # If it exists on disk and is a file, serve it directly
        if os.path.isfile(path):
            return super().do_GET()
        
        # If it is a directory with index.html
        if os.path.isdir(path) and os.path.isfile(os.path.join(path, 'index.html')):
            return super().do_GET()

        # If checkout route
        if clean_path in ('/checkout', '/checkout/'):
            self.path = '/checkout.html'
            return super().do_GET()

        # If it starts with an asset prefix or has a known file extension, it is a missing asset
        _, ext = os.path.splitext(clean_path)
        if clean_path.startswith(ASSET_PREFIXES) or ext.lower() in KNOWN_EXTENSIONS:
            self.send_error(404, f'Asset not found: {self.path}')
            return

        # Otherwise it is an SPA route (/dashboard, /radar-2.0, /videos-ia, etc.)
        self.path = '/index.html'
        return super().do_GET()

if __name__ == '__main__':
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 3000
    server_address = ('', port)
    httpd = HTTPServer(server_address, SPARequestHandler)
    print(f'Voomi SPA Server running on http://localhost:{port} (PID: {os.getpid()})')
    httpd.serve_forever()
