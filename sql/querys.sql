CREATE DATABASE TiendaElectronica;

use TiendaElectronica;

//Para crear un usuario
CREATE USER 'kylo' IDENTIFIED BY 'passwordingresado';

CREATE TABLE Clientes(
    id int AUTO_INCREMENT NOT NULL,
    nombre VARCHAR(50) NOT NULL,
    app VARCHAR(50) NOT NULL,
    apm VARCHAR(50) NOT NULL,
    email VARCHAR(50) NOT NULL,
    PRIMARY KEY(id)
);

CREATE TABLE Cargos(
    id INT NOT NULL AUTO_INCREMENT,
    nombre VARCHAR(50) NOT NULL,
    PRIMARY KEY(id)
);

CREATE TABLE Empleados(
    id INT NOT NULL AUTO_INCREMENT,
    nombre VARCHAR(50) NOT NULL,
    app VARCHAR(50) NOT NULL,
    apm VARCHAR(50) NOT NULL,
    rfc VARCHAR(50) NOT NULL,
    idCargo int NOT NULL,
    password varchar(250) not null,
    vigencia TINYINT not null DEFAULT 1,
    PRIMARY KEY (id),
    FOREIGN KEY (idCargo) REFERENCES Cargos(id)
);

CREATE TABLE Proveedor(
    id int NOT NULL AUTO_INCREMENT,
    nombre VARCHAR(50) NOT NULL,
    app VARCHAR(50) NOT NULL, 
    apm VARCHAR(50) NOT NULL,
    email VARCHAR(50) NOT NULL,
    pais VARCHAR(50) NOT NULL,
    PRIMARY KEY(id)
);

CREATE TABLE Categorias(
    id int NOT NULL AUTO_INCREMENT,
    nombre VARCHAR(50) NOT NULL,
    PRIMARY KEY(id)
);

CREATE TABLE Productos(
    id int NOT NULL AUTO_INCREMENT,
    nombre VARCHAR(50) NOT NULL,
    precio FLOAT NOT NULL DEFAULT 0,
    inventario INT NOT NULL DEFAULT 0,
    idProveedor INT NOT NULL, 
    idCategoria INT NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (idProveedor) REFERENCES Proveedor(id),
    FOREIGN KEY (idCategoria) REFERENCES Categorias(id) 
);

CREATE TABLE Ventas(
    id INT NOT NULL AUTO_INCREMENT,
    fecha DATE NOT NULL,
    hora TIME NOT NULL,
    idCliente INT NOT NULL,
    idProducto INT NOT NULL,
    idEmpleado INT NOT NULL,
    descripcion MEDIUMTEXT,
    PRIMARY KEY(id),
    FOREIGN KEY (idCliente) REFERENCES Clientes(id),
    FOREIGN KEY (idProducto) REFERENCES Productos(id),
    FOREIGN KEY(idEmpleado) REFERENCES Empleados(id)
    );

CREATE VIEW resumenVentas AS
SELECT Ventas.id, Ventas.fecha, Ventas.hora, Empleados.nombre AS 'EMPLEADONOM', Empleados.app AS 'EMPLADOAPP', Ventas.idCliente AS 'IDCLIENTE', Productos.id AS 'CODIGO', Productos.nombre AS 'PRODUCTO', Ventas.descripcion AS 'DESCRIPCION'
from Ventas 
INNER JOIN Empleados ON Ventas.idEmpleado = Empleados.id
INNER JOIN Productos ON Ventas.idProducto = Productos.id




