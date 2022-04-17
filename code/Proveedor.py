# from persona import Persona

# class Proveedor(Persona):
#     pais = str
#     nombreEmpresa = str

#     def __init__(self, nombre, app, apm, email, pais, nombreEmpresa):
#         super().__init__(nombre, app, apm, email)
#         self.pais = pais
#         self.nombreEmpresa = nombreEmpresa
import tkinter
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
    for x in micursor:
        print (x)

def crearProveedores(nombre, app, apm, email, pais, nombreEmpresa):
    micursor = mydb.cursor()
    micursor.execute('INSERT INTO Proveedores(nombre, app, apm, email, pais, nombreEmpresa) VALUES("'+nombre+'","'+app+'","'+apm+'","'+email+'","'+pais+'","'+nombreEmpresa+'");')
    mydb.commit()

def eliminarProveedores(idProveedor):
    micursor = mydb.cursor()
    micursor.execute('DELETE FROM Proveedores WHERE id = '+str(idProveedor)+';')
    mydb.commit()

def buscarProveedor(idProveedor):
    micursor = mydb.cursor()
    micursor.execute('SELECT * FROM Proveedores WHERE id = '+str(idProveedor)+';')
    result = micursor.fetchall()

    for x in result:
        return x

#ventanas
def ventanaCrearProveedores():
    ventana = tkinter.Tk()
    ventana.title("Crear proveedor")
    ventana.geometry("")
    

