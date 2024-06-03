# Manejo de ficheros


class Product:
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


product_list = []


def anadir():
    nombre_producto = input("Nombre")
    cantidad_vendida = input("Cantidad vendida")
    precio = input("Precio")
    product = Product(nombre_producto, cantidad_vendida, precio)
    product_list.append(product)
    return product


def consultar():
    for product in product_list:
        print(product)


def actualizar():
    return product_list


def eliminar():
    for product in product_list:
        product_list.remove(product)
    return product_list


def salir():
    salir = True
    return salir


salir = False
while salir == False:
    menu = input(
        "1. Añadir \n 2. Consultar \n 3.Actualizar \n 4.Eliminar Productos \n 5. Salir"
    )
