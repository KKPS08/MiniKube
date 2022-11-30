import http.server
import socketserver

PORT = 8890
Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Server is running st ", PORT)
    print("To test from dockerized version, please run http://localhost:<exposed port>")
    httpd.serve_forever()