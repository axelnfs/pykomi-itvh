from persona import Persona

class Proveedor(Persona):
    pais = str
    nombreEmpresa = str

    def __init__(self, nombre, app, apm, email, pais, nombreEmpresa):
        super().__init__(nombre, app, apm, email)
        self.pais = pais
        self.nombreEmpresa = nombreEmpresa

