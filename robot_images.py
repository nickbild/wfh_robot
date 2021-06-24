import http.server
import socketserver
import subprocess

# Start up the camera.
subprocess.Popen(["python3 image_capture_loop.py"])

# Start simple web server (serves 'index.html' by default).
PORT = 8000
Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("HTTP server started on port:", PORT)
    httpd.serve_forever()
