import tkinter
from turtle import width
from typing import Text
import Cliente
import Producto
import Categoria
import Empleado
import Proveedor
import mysql.connector
import time

def ventanaBienvenida():
    ventana = tkinter.Tk()
    ventana.geometry("600x200")
    ventana.resizable(0,0)
    # ventana.overrideredirect(True)
    nombrePrograma = tkinter.Label(ventana,text="Pykomi")
    nombrePrograma.config(foreground="black", font=("courier",24))
    nombrePrograma.pack(side=tkinter.LEFT)
    botonCerrar = tkinter.Button(ventana, text="Cerrar mensaje de bienvenida", command=ventana.destroy)
    botonCerrar.pack(side = tkinter.RIGHT)
    ventana.mainloop()

def ventanaPrincipal():
    ventana = tkinter.Tk()
    ventana.title("Menu Principal")
    ventana.geometry("800x600")
    botonVerEmpleados = tkinter.Button(ventana, text="Ver Empleados", width=12, height=1)
    botonVerProveedores = tkinter.Button(ventana, text="Ver Proveedores", width=12, height=1)
    nombreUltimasVentas = tkinter.Label(ventana,text="¡ULTIMAS VENTAS REGISTRADAS!")
    areaUltimasVentas = tkinter.Text(ventana, height=12,width=70)
    botonVerEmpleados.place(x=1, y=1)
    botonVerProveedores.place(x=100, y=1)
    nombreUltimasVentas.place(x = 100, y=28)
    areaUltimasVentas.place(x = 100, y = 48)
    
    ventana.mainloop()

if __name__ == "__main__":
    #eliminarClientes(4)
    # eliminarProveedores(1)
    #verProveedores()
    # print(type(buscarProveedor(2)))
    # Empleado.verEmpleados()
    # Cliente.verClientes()
    # Proveedor.verProveedores()
    # ventanaBienvenida()
    # ventanaPrincipal()
    #Cliente.verClientes()
    # Cliente.ventanaCliente()
    # Cliente.ventanaCrearCliente()
    # Empleado.ventanaCrearEmpleado()
    # Empleado.ventanaEmpleados()
    # Empleado.ventanaEliminarEmpleado()
    # Proveedor.ventanaCrearProveedores()
    # Proveedor.ventanaEliminarProveedor()
    Proveedor.ventanaProveedores()


