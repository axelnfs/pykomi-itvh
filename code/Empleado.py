# import string
# from persona import Persona

# class Empleado(Persona):
#     cargo = string
#     contraseña = string

#     def __init__(self, nombre, app, apm, email, cargo, contraseña):
#         super().__init__(nombre, app, apm, email)
#         self.cargo = cargo
#         self.contraseña = contraseña

#mysql
from cProfile import label
from turtle import width
from matplotlib.pyplot import text
import mysql.connector
#Tkinter
import tkinter
from tkinter import Label, ttk

from numpy import column_stack, insert
from pyparsing import col


mydb = mysql.connector.connect(
    host = "localhost",
    user = "admin",
    password = "1234",
    database = "TiendaElectronica"
    )

#funciones
def verEmpleados():
    micursor = mydb.cursor()
    micursor.execute("SELECT * FROM Empleados;")
    for x in micursor:
        print (x)

def crearEmpleados(nombre, app, apm, rfc, idCargo, password, vigencia):
    micursor = mydb.cursor()
    micursor.execute('INSERT INTO Empleados(nombre, app, apm, rfc, idCargo, password) VALUES("'+nombre+'","'+app+'","'+apm+'","'+rfc+'","'+idCargo+'","'+password+'","'+1+'");')
    mydb.commit()

def despedirEmpleados(idEmpleado):
    micursor = mydb.cursor()
    micursor.execute('DELETE FROM Empleados WHERE id = '+str(idEmpleado)+';')
    mydb.commit()

def buscarEmpleado(idEmpleado):
    micursor = mydb.cursor()
    micursor.execute('SELECT * FROM Empleados WHERE id = '+str(idEmpleado)+';')

#ventanas
def ventanaCrearEmpleado():
    ventana = tkinter.Tk()
    ventana.title("Crear Empleados")
    ventana.geometry("")
    labelPrincipal = Label(ventana, text="Ingrese los datos del nuevo empleado", width=16, height=1)
    labelNombre = Label(ventana, text="Nombre: ")
    labelApp = Label(ventana, text="Apellido Pat: ")
    labelApm= Label(ventana, text="Apellido Mat: ")
    labelRFC = Label(ventana, text="RFC: ")
    labelIdCargo = Label(ventana, text="COMBOBOX: ")
    labelPassword = Label(ventana, text="Contraseña: ")
    insertNombre = ttk.Entry()
    insertApp = ttk.Entry()
    insertApm = ttk.Entry()
    insertRFC = ttk.Entry()
    insertIdCargo = ttk.Entry()
    insertPassword = ttk.Entry()
    labelPrincipal.grid(row=0, column=0)
    labelNombre.grid(row=1, column=0)
    labelApp.grid(row=2, column=0)
    labelApm.grid(row=3, column=0)
    labelRFC.grid(row=4, column=0)
    labelIdCargo.grid(row=5, column=0)
    labelPassword.grid(row=6, column=0)
    ventana.mainloop()

def ventanaEmpleados():
    ventana = tkinter.Tk()
    ventana.title("Menu Empleados")
    ventana.geometry("900x600")
    botonEditarEmpleado = tkinter.Button(ventana, text = "Editar Empleado", width= 16, height=1)
    botonCrearEmpleado = tkinter.Button(ventana, text="Crear Empleado", width=16, height=1)
    botonEliminarEmpleado = tkinter.Button(ventana, text="Despedir Empleado", width=16, height=1)
    botonCrearEmpleado.grid(row = 0, column = 0)
    botonEditarEmpleado.grid(row = 0, column = 1)
    botonEliminarEmpleado.grid(row = 0, column = 2)
    ventana.mainloop()

