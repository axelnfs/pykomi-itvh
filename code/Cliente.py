from persona import Persona

class Cliente(Persona):

    def __init__(self, nombre, app, apm, email):
        super().__init__(nombre, app, apm, email)