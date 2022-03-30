# from persona import Persona

# class Cliente(Persona):

#     def __init__(self, nombre, app, apm, email):
#         super().__init__(nombre, app, apm, email)
import mysql.connector
import tkinter

mydb = mysql.connector.connect(
    host = "localhost",
    user = "admin",
    password = "1234",
    database = "TiendaElectronica"
    )
def verClientes():
    micursor = mydb.cursor()
    micursor.execute("SELECT * FROM Clientes;")
    for x in micursor:
        print (x)

def crearClientes(nombre, app, apm, email):
    micursor = mydb.cursor()
    micursor.execute('INSERT INTO Clientes(nombre, app, apm, email) VALUES("'+nombre+'","'+app+'","'+apm+'","'+email+'");')
    mydb.commit()

def ventanaCliente():
    ventana = tkinter.Tk()
    ventana.title("Menu Principal")
    ventana.geometry("800x600")
    areaClientes = tkinter.Text(ventana, height=12,width=70)
    areaClientes.place(x = 100, y = 48)
    ventana.mainloop()
    