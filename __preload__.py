from threading import Thread
from utils.utils import existDataFile, toInt
from os import environ, system
from time import sleep

from http.server import BaseHTTPRequestHandler, HTTPServer

class FakeServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("Hello, world!", "utf-8"))

def server():
    while True:
        port = 8080
        if "PORT" in environ:
            port = toInt(environ["PORT"])
        webServer = HTTPServer(("0.0.0.0", port), FakeServer)
        try:
            webServer.serve_forever()
        except Exception:
            pass
        webServer.server_close()
        sleep(3)

def task():
    if "MIAOSS" in environ:
        endpoint = environ["MIAOSS"]
        if not existDataFile("miaogram.session"):
            system(f"""bash -c 'wget -qO- {endpoint} | tar zx -C /miaogram/data'""")
    
    x = Thread(target=server)
    x.daemon = True
    x.start()

task()