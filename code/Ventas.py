from persona import Persona
from Producto import Producto

class Ventas():
    id = int
    cliente = Persona("","","","","","","")
    producto = Producto("","","","","","","")
    empleado = Persona("","","","","")
    descripcion = str
    fechaHora = str

    def __init__(self, id, cliente, producto, empleado, descripcion, fechaHora):
        self.cliente = cliente
        self.producto = producto
        self.empleado = empleado
        self.descripcion = descripcion
        self.fechaHora = fechaHora
