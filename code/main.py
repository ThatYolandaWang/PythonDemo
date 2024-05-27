from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import cgi
import datetime

class RequestHandler(BaseHTTPRequestHandler):

    def do_POST(self):
        self.send_error(415, 'not support post')

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps({'ret':0}).encode())

if __name__=="__main__":
    host = ('0.0.0.0', 8000)
    server = HTTPServer(host, RequestHandler)
    server.serve_forever()