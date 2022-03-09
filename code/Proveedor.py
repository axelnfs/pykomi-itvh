import string
from persona import Persona

class Proveedor(Persona):
    pais = string
    nombreEmpresa = string

    def __init__(self, nombre, app, apm, email, pais, nombreEmpresa):
        super().__init__(nombre, app, apm, email)
        self.pais = pais
        self.nombreEmpresa = nombreEmpresa

