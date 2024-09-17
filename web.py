from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qsl, urlparse

# Diccionario con los proyectos y su contenido HTML
contenido = {

}

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
        #Obtener la ruta solicitada
        path = self.path

        # Buscar en el diccionario el contenido correspondiente a la ruta
        content = contenido.get(path, None)
    
        # Si existe el contenido para esa ruta, devolverlo
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.end_headers()
        self.wfile.write(self.get_response().encode("utf-8"))

    def do_POST(self):
        Archivo = leer_archivo_html('home.html')
        #Obtener la ruta solicitada
        path = self.path
        
        # Buscar en el diccionario el contenido correspondiente a la ruta
        content = contenido.get(path, None)
    
        # Si existe el contenido para esa ruta, devolverlo
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.end_headers()
        self.wfile.write(self.get_response().encode("utf-8"))

    def get_response(self):
        return f"""
    <h1> Hola Web </h1>
    <form action="" method="post" class="forma-ejemplo">
        <div class="forma">
	    <label for="nombre">Nombre:</label>
	    <input type="text" name="nombre" id="nombre" required/>
        </div>
         <div class="forma">
	        <label for="correo">Correo:</label>
	        <input type="correo" name="correo" id="correo" required/>
        </div>
        <div class="forma">
	        <input type="submit" vale="Registrate"/>
        </div>
    </form>
"""


if __name__ == "__main__":
    print("Starting server")
    print("Sitio WebHandler")
    server = HTTPServer(("0.0.0.0", 8000), WebRequestHandler)
    server.serve_forever()
