# Manejo de ficheros


class Producto:
    def __init__(self, nombre_producto, cantidad_vendida, precio) -> None:
        pass
        self.__nombre_producto = nombre_producto
        self.__cantidad_vendida = cantidad_vendida
        self.__precio = precio

    def get_nombre_producto(self):
        return self.__nombre_producto

    def get_cantidad_vendida(self):
        return self.__cantidad_vendida

    def get_precio(self):
        return self.__precio


def anadir():
    nombre_producto = input("Nombre")
    cantidad_vendida = input("Cantidad vendida")
    precio = input("Precio")
    producto = Producto(nombre_producto, cantidad_vendida, precio)
    return producto


i = 0
while i == 0:
    menu = input(
        "1. Añadir \n 2. Consultar \n 3.Actualizar \n 4.Eliminar Productos \n 5. Salir"
    )
