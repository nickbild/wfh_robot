import http.server
import socketserver


# Start simple web server (serves 'index.html' by default).
PORT = 8000
Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("HTTP server started on port:", PORT)
    httpd.serve_forever()
