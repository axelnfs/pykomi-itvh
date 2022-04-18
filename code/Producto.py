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
    micursor.execute("SELECT * FROM Clientes;")
    contador = 2
    for x in micursor:
        imprimirProductos(contador,x[0])
        contador = contador + 1

def crearProductos(nombre, precio, inventario, idProveedor, idCategoria):
    micursor = mydb.cursor()
    micursor.execute('INSERT INTO Clientes(nombre, app, apm, email) VALUES("'+nombre+'","'+precio+'","'+inventario+'","'+idProveedor+'","'+idCategoria+'");')
    mydb.commit()

def ventanaCrearProductos():
    ventana = tkinter.Tk()
    ventana.title("INGRESAR PRODUCTO")
    ventana.geometry("")
    label1 = Label(ventana, text="INGRESE PRODUCTO")