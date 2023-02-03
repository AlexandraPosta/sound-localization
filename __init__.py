import http.server
import socketserver
from urllib.parse import parse_qs, urlparse

from main import *

PORT = 8000

class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Split get request up into components
        query = urlparse(self.path)

        if query.path == "/endpoint":
            query = parse_qs(query.query)

            # Generate the room 
            if query["type"][0] == "getroom":
                data = getroom(query["room[]"], query["src[]"], [query["mic[0][]"], query["mic[1][]"]])
                self.send_response(200)
                self.send_header("Content-length", len(data))
                self.end_headers()
                self.wfile.write(bytes(data, encoding='utf8'))

            # Run localization prediction using the specified method
            elif query["type"][0] == "run_model":
                data = runModel(query["model"][0])
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