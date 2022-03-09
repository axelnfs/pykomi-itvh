from persona import Persona
from Categoria import Categoria

class Producto:
    id = int
    nombre = str
    precio = float
    inventario = int
    Proveedor = Persona("","","","","","","")
    Categoria = Categoria("")

    def __init__(self, nombre, precio, inventario, idProveedor, idCategoria):
        self.nombre = nombre
        self.precio = precio
        self.inventario = inventario
        self.idProveedor = idProveedor
        self.idCategoria = idCategoria