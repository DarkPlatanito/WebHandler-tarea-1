from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qsl, urlparse

#Se crea un metodo para leer el archivo
def leer_archivo_html(nombre_archivo):
    try:
        with open(nombre_archivo, 'r', encoding="utf-8") as archivo:
            return archivo.read()
    except FileNotFoundError:
        return "<h1>Error 404: File Not Found</h1>"

class WebRequestHandler(BaseHTTPRequestHandler):
    def url(self):
        return urlparse(self.path)

    def query_data(self):
        return dict(parse_qsl(self.url().query))

    def do_GET(self):
        Archivo = leer_archivo_html('home.html')
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.end_headers()
        self.wfile.write(Archivo.encode("utf-8"))

    def get_response(self):
        return f"""
    <h1> Hola Web </h1>
    <h1>{self.url().path.split('/')[-2]}: {self.url().path.split('/')[-1]} {self.query_data()} <h1>
    <p> URL Parse Result : {self.url()}         </p>
    <p> Path Original: {self.path}         </p>
    <p> Headers: {self.headers}      </p>
    <p> Query: {self.query_data()}   </p>
"""


if __name__ == "__main__":
    print("Starting server")
    server = HTTPServer(("localhost", 8000), WebRequestHandler)
    server.serve_forever()
