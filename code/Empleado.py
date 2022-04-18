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
# from cProfile import label
# from turtle import width
# from cProfile import label
# from matplotlib.pyplot import box
import mysql.connector
#Tkinter
import tkinter
from tkinter import Label, ttk

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

def crearEmpleados(nombre, app, apm, rfc, idCargo, password):
    micursor = mydb.cursor()
    micursor.execute('INSERT INTO Empleados(nombre, app, apm, rfc, idCargo, password) VALUES("'+nombre+'","'+app+'","'+apm+'","'+rfc+'","'+idCargo+'","'+password+'");')
    mydb.commit()

def despedirEmpleados(idEmpleado):
    micursor = mydb.cursor()
    micursor.execute('DELETE FROM Empleados WHERE id = '+str(idEmpleado)+';')
    mydb.commit()
    ventana = tkinter.Tk()
    ventana.title("ELIMINADO")
    label = Label(ventana, text="haz despedido a: "+idEmpleado)
    label.pack()
    ventana.mainloop()

def buscarEmpleado(idEmpleado):
    micursor = mydb.cursor()
    micursor.execute('SELECT * FROM Empleados WHERE id = '+str(idEmpleado)+';')

def imprimirEmpleados(contadorRow, id, nombre, app, apm, rfc, cargo, vigencia):
    labelId = ttk.Entry()
    labelNombre = ttk.Entry()
    labelApp = ttk.Entry()
    labelApm = ttk.Entry()
    labelRfc = ttk.Entry()
    labelCargo = ttk.Entry()
    labelVigencia = ttk.Entry()
    labelId.grid(row=1, column=0)
    labelNombre.grid(row=1, column=1)
    labelApp.grid(row=1, column=2)
    labelApm.grid(row=1, column=3)
    labelRfc.grid(row=1, column=4)
    labelCargo.grid(row=1, column=5)
    labelVigencia.grid(row=1, column=6)
    labelId.insert(0, "ID")
    labelNombre.insert(0,"NOMBRE")
    labelApp.insert(0, "AP PATERNO")
    labelApm.insert(0,"AP MATERNO")
    labelRfc.insert(0,"RFC")
    labelCargo.insert(0, "cargo")
    labelVigencia.insert(0, "Vigencia")
    boxId = ttk.Entry()
    boxNombre = ttk.Entry()
    boxApp = ttk.Entry()
    boxApm = ttk.Entry()
    boxRfc = ttk.Entry()
    boxCargo = ttk.Entry()
    boxVigencia = ttk.Entry()
    contador = contadorRow
    boxId.grid(row = contador, column=0)
    boxNombre.grid(row = contador, column=1)
    boxApp.grid(row = contador, column=2)
    boxApm.grid(row = contador, column=3)
    boxRfc.grid(row = contador, column=4)
    boxCargo.grid(row = contador, column=5)
    boxVigencia.grid(row = contador, column=6)
    boxId.insert(0, id)
    boxNombre.insert(0, nombre)
    boxApp.insert(0, app)
    boxApm.insert(0, apm)
    boxRfc.insert(0, rfc)
    boxCargo.insert(0, cargo)
    boxVigencia.insert(0, vigencia)

def verEmpleados():
    micursor = mydb.cursor()
    micursor.execute("SELECT Empleados.id, Empleados.nombre, Empleados.app, Empleados.apm, Empleados.rfc, Cargos.nombre, Empleados.vigencia FROM Empleados INNER JOIN Cargos ON Empleados.idCargo = Cargos.id;")
    contador = 2
    for x in micursor:
        imprimirEmpleados(contador, x[0],x[1],x[2],x[3],x[4],x[5],x[6])
        contador = contador + 1

def obtenerDatosNuevoEmpleado(nombre, app, apm, rfc, idCargo, password):
    crearEmpleados(nombre, app, apm, rfc, idCargo, password)
    ventana = tkinter.Tk()
    ventana.title("NOTIFICACION")
    ventana.geometry("")
    label1 = Label(ventana, text="SE HA CONTRATADO A UN NUEVO EMPLEADO")
    label1.grid(row = 0, column = 0)
    ventana.mainloop()

#ventanas
def ventanaEliminarEmpleado():
    ventana = tkinter.Tk()
    ventana.title("Eliminar Empleados")
    ventana.geometry("")
    labelMensaje = Label(ventana, text = "Digite el ID a despedir")
    labelID = Label(ventana, text = "ID: ")
    boxId = ttk.Entry()
    submit = tkinter.Button(ventana, text="¡¡¡DESPEDIR!!!", command= lambda: despedirEmpleados(boxId.get()))
    labelMensaje.grid(row=0, column=0)
    labelID.grid(row=1,column=0)
    boxId.grid(row=1, column=1)
    submit.grid(row=2, column=1)
    ventana.mainloop()

def ventanaCrearEmpleado():
    ventana = tkinter.Tk()
    ventana.title("Crear Empleados")
    ventana.geometry("")
    labelPrincipal =  Label(ventana, text="Ingrese los datos del nuevo empleado", width=16, height=1)
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
    insertNombre.grid(row=1, column=1)
    insertApp.grid(row=2, column=1)
    insertApm.grid(row=3, column=1)
    insertRFC.grid(row=4, column=1)
    insertIdCargo.grid(row=5, column=1)
    insertPassword.grid(row=6, column=1)
    submit =  tkinter.Button(ventana, text = "GUARDAR", width=16, height=1, command = lambda: obtenerDatosNuevoEmpleado(insertNombre.get(), insertApp.get(), insertApm.get(), insertRFC.get(), insertIdCargo.get(), insertPassword.get()))
    submit.grid(row=7, column=1)
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
    verEmpleados()
    ventana.mainloop()

