# from persona import Persona
# from Categoria import Categoria

# class Producto:
#     id = int
#     nombre = str
#     precio = float
#     inventario = int
#     Proveedor = Persona("","","","")
#     Categoria = Categoria("")

#     def __init__(self, nombre, precio, inventario, Proveedor, Categoria):
#         self.nombre = nombre
#         self.precio = precio
#         self.inventario = inventario
#         self.Proveedor = Proveedor
#         self.Categoria = Categoria
import mysql.connector
import tkinter
from tkinter import Label, ttk

mydb = mysql.connector.connect(
    host = "localhost",
    user = "admin",
    password = "1234",
    database = "TiendaElectronica"
    )

def verProductos():
    micursor = mydb.cursor()
    micursor.execute("SELECT * FROM Productos;")
    contador = 2
    for x in micursor:
        imprimirProductos(contador,x[0],x[1],x[2],x[3],x[4])
        contador = contador + 1

def crearProductos(nombre, precio, inventario, idProveedor):
    micursor = mydb.cursor()
    micursor.execute('INSERT INTO Productos(nombre, precio, inventario, idProveedor) VALUES("'+nombre+'","'+precio+'","'+inventario+'","'+idProveedor+'");')
    mydb.commit()
    ventana = tkinter.Tk()
    ventana.title("NOTIFICACION")
    ventana.geometry("")
    label1 = Label(ventana, text="SE HA CREADO UN PRODUCTOS")
    label1.grid(row = 0, column = 0)
    ventana.mainloop()
    
def imprimirProductos(contadorRow, id, nombre, precio, inventario, idProveedor):
    labelId = ttk.Entry()
    labelNombre = ttk.Entry()
    labelPrecio = ttk.Entry()
    labelInventario = ttk.Entry()
    labelIdProveedor = ttk.Entry()
    boxId = ttk.Entry()
    boxNombre = ttk.Entry()
    boxPrecio = ttk.Entry()
    boxInventario = ttk.Entry()
    boxIdProveedor = ttk.Entry()
    labelId.grid(row = 1, column = 1)
    labelNombre.grid(row = 1,column = 2)
    labelPrecio.grid(row = 1,column = 3)
    labelInventario.grid(row = 1,column = 4)
    labelIdProveedor.grid(row = 1,column = 5)
    labelId.insert(0, "ID")
    labelNombre.insert(0, "NOMBRE")
    labelPrecio.insert(0, "PRECIO")
    labelInventario.insert(0, "INVENTARIO")
    labelIdProveedor.insert(0, "PROVEEDOR")

    contador = contadorRow
    boxId.grid(row = contador, column= 1)
    boxNombre.grid(row = contador, column= 2)
    boxPrecio.grid(row = contador, column= 3)
    boxInventario.grid(row = contador, column= 4)
    boxIdProveedor.grid(row = contador, column= 5)
    boxId.insert(0, id)
    boxNombre.insert(0, nombre)
    boxPrecio.insert(0, precio)
    boxInventario.insert(0, inventario)
    boxIdProveedor.insert(0, idProveedor)

def ventanaCrearProductos():
    ventana = tkinter.Tk()
    ventana.title("INGRESAR PRODUCTO")
    ventana.geometry("")
    labelPrincipal = Label(ventana, text="INGRESE PRODUCTO")
    labelNombre = Label(ventana, text="NOMBRE")
    labelPrecio = Label(ventana, text="PRECIO")
    labelInventario = Label(ventana, text="INVENTARIO")
    labelIdProveedor = Label(ventana, text="PROVEEDOR")
    insertNombre = ttk.Entry()
    insertPrecio = ttk.Entry()
    insertInventario = ttk.Entry()
    insertIdProveedor = ttk.Entry()
    submit = tkinter.Button(ventana, text="GUARDAR", width=16, height=1, command= lambda: crearProductos(insertNombre.get(), insertPrecio.get(), insertInventario.get(),insertIdProveedor.get()))
    labelPrincipal.grid(row = 0,column = 0)
    labelNombre.grid(row = 1,column = 0)
    labelPrecio.grid(row = 2,column = 0)
    labelInventario.grid(row = 3,column = 0)
    labelIdProveedor.grid(row = 4,column = 0)
    insertNombre.grid(row = 1, column=1)
    insertPrecio.grid(row = 2, column=1)
    insertInventario.grid(row = 3, column=1)
    insertIdProveedor.grid(row = 4, column=1)
    submit.grid(row = 6, column = 1)
    ventana.mainloop()

def ventanaProductos():
    ventana = tkinter.Tk()
    ventana.title("Menu Empleados")
    ventana.geometry("900x600")
    botonCrearProducto = tkinter.Button(ventana, text="Crear Producto", width = 16, height = 1)
    botonCrearProducto.grid(row=0, column=0)
    verProductos()
    ventana.mainloop()