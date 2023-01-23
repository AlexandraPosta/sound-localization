import http.server
import socketserver
from urllib.parse import parse_qs, urlparse

from main import getroom

PORT = 8000

class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Split get request up into components
        query = urlparse(self.path)

        if query.path == "/endpoint":
            type = parse_qs(query.query)["type"][0]

            if type == "getroom":
                data = getroom()
                self.send_response(200)
                self.send_header("Content-length", len(data))
                self.end_headers()
                self.wfile.write(bytes(data, encoding='utf8'))
            else:
                print('Invalid request.') 

        return http.server.SimpleHTTPRequestHandler.do_GET(self)


    def do_POST(self):
        query = urlparse(self.path)

    

handler_object = MyHttpRequestHandler
my_server = socketserver.TCPServer(("", PORT), handler_object)

# Star the server
my_server.serve_forever()