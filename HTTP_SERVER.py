from http.server import HTTPServer, BaseHTTPRequestHandler
import time

HOST =  "172.31.224.1"
PORT = 9999


class NeuralHTTP(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        self.wfile.write(bytes("<html><body><h1>Welcome to Olakanmi's HTTP Server :)</h1></body></html>" "utf-8"))

        def do_POST(self):
            self.send_response(200)
            self.send_header("Content type", "applivation/json")
            self.end_headers()

            date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
            self.wfile.write(bytes('{"time": "' + date + '"}', "utf-8"))


server = HTTPServer((HOST, PORT), NeuralHTTP)
print("Server now running on port 9999...")

server.serve_forever()
server.server_close()
print("Server Stopped...")
