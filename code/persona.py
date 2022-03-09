import string


class Producto:
    id = int
    nombre = str
    app = string
    apm = string
    email = string


    def __init__(self, nombre, app, apm, email):
        self.nombre = nombre
        self.app = app
        self.apm = apm
        self.email = email
