import string
from persona import Persona

class Empleado(Persona):
    cargo = string
    contraseña = string

    def __init__(self, nombre, app, apm, email, cargo, contraseña):
        super().__init__(nombre, app, apm, email)
        self.cargo = cargo
        self.contraseña = contraseña