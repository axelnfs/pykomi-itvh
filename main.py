from Cliente import Cliente
from Producto import Producto
from Categoria import Categoria
from Proveedor import Proveedor
import mysql.connector
import recovery_exe

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

def verClientes():
    micursor = mydb.cursor()
    micursor.execute("SELECT * FROM Clientes;")
    for x in micursor:
        print (x)

def crearClientes(nombre, app, apm, email):
    micursor = mydb.cursor()
    micursor.execute('INSERT INTO Clientes(nombre, app, apm, email) VALUES("'+nombre+'","'+app+'","'+apm+'","'+email+'");')
    mydb.commit()

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

def eliminarClientes(idCliente):
    micursor = mydb.cursor()
    micursor.execute('DELETE FROM Clientes WHERE id = '+str(idCliente)+'')
    mydb.commit()

if __name__ == "__main__":
    #crearClientes("MANUEL", "HERNANDEZ", "FELIX", "felix99@mail.com")
    # crearClientes("JOSE", "MARTINEZ", "SANCHEZ", "josm@mail.com")
    # crearClientes("ALEXANDER", "LOPEZ", "MERINO", "alel@mail.com")
    #eliminarClientes(4)
    #verClientes()
    #crearEmpleados("AXEL MANUEL","MOSQUEDA","DE LA CRUZ", "1MODA235", "1", "administrador")
    #verEmpleados()
    # eliminarProveedores(1)
    #crearProveedores("DANNA PAOLA", "SANCHEZ","SANCHEZ","danpal@mail.com","España","Tiendas ChocoTec")
    #verProveedores()
    #print(type(buscarProveedor(2)))
    pass



