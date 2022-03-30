# import string
# from persona import Persona

# class Empleado(Persona):
#     cargo = string
#     contraseña = string

#     def __init__(self, nombre, app, apm, email, cargo, contraseña):
#         super().__init__(nombre, app, apm, email)
#         self.cargo = cargo
#         self.contraseña = contraseña
import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "admin",
    password = "1234",
    database = "TiendaElectronica"
    )
    
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

def buscarEmpleado(idEmpleado):
    micursor = mydb.cursor()
    micursor.execute('SELECT * FROM Empleados WHERE id = '+str(idEmpleado)+';')