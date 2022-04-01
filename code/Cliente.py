# from persona import Persona

# class Cliente(Persona):

#     def __init__(self, nombre, app, apm, email):
#         super().__init__(nombre, app, apm, email)
import mysql.connector
import tkinter
from tkinter import ttk

mydb = mysql.connector.connect(
    host = "localhost",
    user = "admin",
    password = "1234",
    database = "TiendaElectronica"
    )

def imprimirClientes(contadorRow, id, nombre, app, apm, email):
    labelid = ttk.Entry()
    labelnombre = ttk.Entry()
    labelapp = ttk.Entry()
    labelapm = ttk.Entry()
    labelemail = ttk.Entry()
    boxid = ttk.Entry()
    boxnombre = ttk.Entry()
    boxapp = ttk.Entry()
    boxapm = ttk.Entry()
    boxemail = ttk.Entry()
    labelid.grid(row = 1, column=1)
    labelnombre.grid(row = 1, column=2)
    labelapp.grid(row = 1, column=3)
    labelapm.grid(row = 1, column=4)
    labelemail.grid(row = 1, column=5)
    labelid.insert(0, "ID")
    labelnombre.insert(0,"NOMBRE")
    labelapp.insert(0, "AP PATERNO")
    labelapm.insert(0,"AP MATERNO")
    labelemail.insert(0,"EMAIL")

    contador = contadorRow
    boxid.grid(row = contador, column=1)
    boxnombre.grid(row = contador, column=2)
    boxapp.grid(row = contador, column=3)
    boxapm.grid(row = contador, column=4)
    boxemail.grid(row = contador, column=5)
    boxid.insert(0, id)
    boxnombre.insert(0, nombre)
    boxapp.insert(0, app)
    boxapm.insert(0, apm)
    boxemail.insert(0, email)

def verClientes():
    micursor = mydb.cursor()
    micursor.execute("SELECT * FROM Clientes;")
    contador = 2
    for x in micursor:
        imprimirClientes(contador,x[0], x[1],x[2],x[3],x[4])
        contador = contador + 1
        #print (x)
        # print(x[1])
        # print(type(x))

def crearClientes(nombre, app, apm, email):
    micursor = mydb.cursor()
    micursor.execute('INSERT INTO Clientes(nombre, app, apm, email) VALUES("'+nombre+'","'+app+'","'+apm+'","'+email+'");')
    mydb.commit()

def ventanaCliente():
    ventana = tkinter.Tk()
    ventana.title("Menu Principal")
    ventana.geometry("900x600")
    #areaClientes = tkinter.Text(ventana, height=12,width=70)
    #areaClientes.place(x = 100, y = 48)
    # entry = ttk.Entry()
    # entry1 = ttk.Entry()
    # entry2 = ttk.Entry()
    # entry3 = ttk.Entry()
    # entry4 = ttk.Entry()
    # entry5 = ttk.Entry()
    boton1 =  tkinter.Button(ventana, text = "Ver Clientes", width=16, height=1)
    boton2 =  tkinter.Button(ventana, text = "Crear Clientes", width=16, height=1)
    boton3 =  tkinter.Button(ventana, text = "ayuda", width=16, height=1)

    boton1.grid(row= 0, column=0)
    boton2.grid(row= 0, column=1)
    boton3.grid(row= 0, column=2)
    #entry.place(x = 100, y = 48)
    verClientes()
    ventana.mainloop()
    