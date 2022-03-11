from Cliente import Cliente
from Producto import Producto
from Categoria import Categoria
from Proveedor import Proveedor

if __name__ == "__main__":
    Cliente1 = Cliente("Adri Hiday","Herrera","Velazquez","rmoreno@mail.com")
    #print(vars(Cliente1))

    Proveedor1 = Proveedor("Juan","Ramirez","Cordoba","jramirez@empresa.com","Espana","RamiresEspana")
    Proveedor2 = Proveedor("JOSE","SANCHEZ","OCA","jsanches@empresa.com", "chile","jempresa")
    Categoria1 = Categoria("Embutido")

    Producto1 = Producto("Jamon Espanol",20.4,10,vars(Proveedor2),vars(Categoria1))
    print(vars(Producto1))

