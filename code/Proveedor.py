# from persona import Persona

# class Proveedor(Persona):
#     pais = str
#     nombreEmpresa = str

#     def __init__(self, nombre, app, apm, email, pais, nombreEmpresa):
#         super().__init__(nombre, app, apm, email)
#         self.pais = pais
#         self.nombreEmpresa = nombreEmpresa
import tkinter
from tkinter import Label, ttk
import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "admin",
    password = "1234",
    database = "TiendaElectronica"
    )

def verProveedores():
    micursor = mydb.cursor()
    micursor.execute("SELECT * FROM Proveedores;")
    contador = 2
    for x in micursor:
        imprimirProveedores(contador, x[0], x[1],x[2],x[3],x[4],x[5],x[6])
        contador = contador + 1
        # print (x)

def crearProveedores(nombre, app, apm, email, pais, nombreEmpresa):
    micursor = mydb.cursor()
    micursor.execute('INSERT INTO Proveedores(nombre, app, apm, email, pais, nombreEmpresa) VALUES("'+nombre+'","'+app+'","'+apm+'","'+email+'","'+pais+'","'+nombreEmpresa+'");')
    mydb.commit()

def eliminarProveedores(idProveedor):
    micursor = mydb.cursor()
    micursor.execute('DELETE FROM Proveedores WHERE id = '+str(idProveedor)+';')
    mydb.commit()
    ventana = tkinter.Tk()
    ventana.title("Crear proveedor")
    ventana.geometry("")
    labelPrincipal =  Label(ventana, text="Ingrese los datos del proveedor", width=16, height=1)
    labelPrincipal.grid(row=0, column=0)
    ventana.mainloop()

def buscarProveedor(idProveedor):
    micursor = mydb.cursor()
    micursor.execute('SELECT * FROM Proveedores WHERE id = '+str(idProveedor)+';')
    result = micursor.fetchall()

    for x in result:
        return x

def obtenerDatosNuevoProveedor(nombre, app, apm, email, pais, nombreEmpresa):
    crearProveedores(nombre, app, apm, email, pais, nombreEmpresa)
    ventana = tkinter.Tk()
    ventana.title("NOTIFICACION")
    ventana.geometry("")
    label1 = Label(ventana, text="SE HA CREADO UN PROVEEDOR")
    label1.grid(row = 0, column = 0)
    ventana.mainloop()

def imprimirProveedores(contadorRow, id, nombre, app, apm, email, pais, nombreEmpresa):
    labelId = ttk.Entry()
    labelNombre = ttk.Entry()
    labelApp = ttk.Entry()
    labelApm = ttk.Entry()
    labelEmail = ttk.Entry()
    labelPais = ttk.Entry()
    labelNombreEmpresa = ttk.Entry()
    boxId = ttk.Entry()
    boxNombre = ttk.Entry()
    boxApp = ttk.Entry()
    boxApm = ttk.Entry()
    boxEmail = ttk.Entry()
    boxPais = ttk.Entry()
    boxNombreEmpresa = ttk.Entry()
    labelId.insert(0,"ID")
    labelNombre.insert(0,"NOMBRE")
    labelApp.insert(0,"AP PATERNO")
    labelApm.insert(0,"AP MATERNO")
    labelEmail.insert(0,"EMAIL")
    labelPais.insert(0,"PAIS")
    labelNombreEmpresa.insert(0,"EMPRESA")
    labelId.grid(row=0,column=0)
    labelNombre.grid(row=0,column=1)
    labelApp.grid(row=0,column=2)
    labelApm.grid(row=0,column=3)
    labelEmail.grid(row=0,column=4)
    labelPais.grid(row=0,column=5)
    labelNombreEmpresa.grid(row=0,column=6)
    contador = contadorRow
    boxId.grid(row=contador, column=0)
    boxNombre.grid(row=contador, column=1)
    boxApp.grid(row=contador, column=2)
    boxApm.grid(row=contador, column=3)
    boxEmail.grid(row=contador, column=4)
    boxPais.grid(row=contador, column=5)
    boxNombreEmpresa.grid(row=contador, column=6)
    boxId.insert(0, id)
    boxNombre.insert(0, nombre)
    boxApp.insert(0, app)
    boxApm.insert(0, apm)
    boxEmail.insert(0, email)
    boxPais.insert(0, pais)
    boxNombreEmpresa.insert(0, nombreEmpresa)


#ventanas
def ventanaCrearProveedores():
    ventana = tkinter.Tk()
    ventana.title("Crear proveedor")
    ventana.geometry("")
    labelPrincipal =  Label(ventana, text="Ingrese los datos del proveedor", width=16, height=1)
    labelNombre = Label(ventana, text="Nombre: ")
    labelApp = Label(ventana, text="Apellido Pat: ")
    labelApm= Label(ventana, text="Apellido Mat: ")
    labelEmail = Label(ventana, text="RFC: ")
    labelPais = Label(ventana, text="Pais")
    labelNombreEmpresa = Label(ventana, text="Empresa")
    insertNombre = ttk.Entry()
    insertApp = ttk.Entry()
    insertApm = ttk.Entry()
    insertEmail = ttk.Entry()
    insertPais = ttk.Entry()
    insertNombreEmpresa = ttk.Entry()
    submit = tkinter.Button(ventana, text = "GUARDAR", width=16, height=1, command = lambda: obtenerDatosNuevoProveedor(insertNombre.get(), insertApp.get(), insertApm.get(), insertEmail.get(), insertPais.get(), insertNombreEmpresa.get()))
    labelPrincipal.grid(row=0, column=0)
    labelNombre.grid(row= 1,column=0)
    labelApp.grid(row= 2,column=0)
    labelApm.grid(row= 3,column=0)
    labelEmail.grid(row= 4,column=0)
    labelPais.grid(row= 5,column=0)
    labelNombreEmpresa.grid(row= 6,column=0)
    insertNombre.grid(row= 1, column=1)
    insertApp.grid(row= 2, column=1)
    insertApm.grid(row= 3, column=1)
    insertEmail.grid(row= 4, column=1)
    insertPais.grid(row= 5, column=1)
    insertNombreEmpresa.grid(row= 6, column=1)
    submit.grid(row=7, column=1)
    ventana.mainloop()

def ventanaEliminarProveedor():
    ventana = tkinter.Tk()
    ventana.title("Eliminar proveedor")
    ventana.geometry("")
    labelPrincipal =  Label(ventana, text="Ingrese el ID para eliminar proveedor", width=16, height=1)
    labelId = Label(ventana, text="ID: ")
    insertId = ttk.Entry()
    submit = ttk.Button(ventana, text="ELIMINAR")
    submit = tkinter.Button(ventana, text = "GUARDAR", width=16, height=1, command = lambda: eliminarProveedores(insertId.get()))
    labelPrincipal.grid(row=0, column=0)
    labelId.grid(row=1, column=0)
    insertId.grid(row=1, column=1)
    submit.grid(row=2, column=1)
    ventana.mainloop()

def ventanaProveedores():
    ventana = tkinter.Tk()
    ventana.title("Menu Empleados")
    ventana.geometry("900x600")
    botonEditarEmpleado = tkinter.Button(ventana, text = "Ver Proveedores", width= 16, height=1)
    botonCrearEmpleado = tkinter.Button(ventana, text="Eliminar Proveedores", width=16, height=1)
    botonEliminarEmpleado = tkinter.Button(ventana, text="Nuevo Proveedor", width=16, height=1)
    botonCrearEmpleado.grid(row = 0, column = 0)
    botonEditarEmpleado.grid(row = 0, column = 1)
    botonEliminarEmpleado.grid(row = 0, column = 2)

    verProveedores()
    ventana.mainloop()






