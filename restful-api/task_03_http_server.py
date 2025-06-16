#!/usr/bin/python3
"""
This is a simple API using Python with 'http.server' module
"""


import http.server
import socketserver
import json


PORT = 8000


class MyHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            # tells the browser/tool everything went okay
            self.send_response(200)
            # Headers describe what kind of content is being sent
            self.send_header("Content-type", "text/plain")
            # this finalises the HTTP response headers before sending the
            # actual content
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")
        elif self.path == "/data":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            data = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(json.dumps(data).encode())
        elif self.path == "/info":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            data = {"version": "1.0", "description": "A simple API built with http.server"}
            self.wfile.write(json.dumps(data).encode())
        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")
        else:
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Endpoint not found")


Handler = MyHandler

# socket server helps create network servers
# for this project, it's used to create a HTTP server that
# listens on port 8000,
# accepts incoming connections (like from a browser), and passes them to the
# handler (MyHandler) to deal with

# socketserver.TCPserver sets up a basic server that uses TCP
# (protocol used for HTTP)
# "" - means "listen on all available network interfaces" (e.g localhost)
# PORT - port number - how browsers know where to find your server
# Handler - class that tells server how to respond to requests
# httpd - gives a name to the server instance so it can be used below
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving on port {PORT}")
    # starts server listening for requests and doesn't stop until
    # manually ended/killed
    httpd.serve_forever()
