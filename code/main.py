import tkinter
from turtle import width
from typing import Text

from pyparsing import col
import Cliente
import Producto
import Categoria
import Empleado
import Proveedor
import mysql.connector
import time

# from code.Producto import ventanaCrearProductos

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
    botonEmpleados = tkinter.Button(ventana, text="EMPLEADOS", width=16, height=1)
    botonProveedores = tkinter.Button(ventana, text="PROVEEDORES", width=16, height=1)
    botonProductos = tkinter.Button(ventana, text="PRODUCTOS", width=16, height=1)
    nombreUltimasVentas = tkinter.Label(ventana,text="¡ULTIMAS VENTAS REGISTRADAS!")
    areaUltimasVentas = tkinter.Text(ventana, height=12,width=70)
    botonEmpleados.grid(row=0, column=0)
    botonProveedores.grid(row=0, column=1)
    botonProductos.grid(row=0, column=2)
    nombreUltimasVentas.grid(row=1, column=1)
    areaUltimasVentas.grid(row=2, column=1)
    
    ventana.mainloop()

if __name__ == "__main__":
    #eliminarClientes(4)
    # eliminarProveedores(1)
    #verProveedores()
    # print(type(buscarProveedor(2)))
    # Empleado.verEmpleados()
    # Cliente.verClientes()
    # Proveedor.verProveedores()
    ventanaBienvenida()
    ventanaPrincipal()
    #Cliente.verClientes()
    # Cliente.ventanaCliente()
    # Cliente.ventanaCrearCliente()
    # Empleado.ventanaCrearEmpleado()
    # Empleado.ventanaEmpleados()
    # Empleado.ventanaEliminarEmpleado()
    # Proveedor.ventanaCrearProveedores()
    # Proveedor.ventanaEliminarProveedor()
    # Proveedor.ventanaProveedores()
    # Producto.ventanaCrearProductos()
    # Producto.ventanaCrearProductos()
    Producto.ventanaProductos()


