#Programa que maneja el inventario (precio y nombre)de los productos de una tienda de abarrotes usando Diccionarios (Dictionary).
def agregar():
    nombre = input("Ingrese el producto a agregar ")
    print("Todos los productos se manejan en MXN$")
    precio = int(input("Ingrese su precio "))
    productos.update({nombre: precio})
    print("El inventario actual es")
    print (productos)

def quitar():
    print(productos)
    print("El producto debe estar en el inventario")
    B = input("Escriba el producto a borrar ")
    L = productos
    if (B in L):
        del productos[B]
        print("El inventario actual es")
        print(productos)
    else:
        print("Producto no encontrado")
def desplegar():
    print(productos)
productos = {'Leche': 20}
print("Programa para guardar los datos de productos")
print("Para agregar productos al inventario presione 1, para quitar presione 2 y para desplegar los productos en el inventario 3")
print("para cerrar el progrma presione 0\n")
op = int(input("Seleccione una opción "))
while (op != 0):
    if (op == 1):
        agregar()
    elif(op == 2):
        quitar()
    elif(op == 3):
        desplegar()
    else:
        print("seleccione una opción válida")
    print("Para agregar productos al inventario presione 1, para quitar presione 2 y para desplegar los productos en el inventario 3")
    print("para cerrar el progrma presione 0\n")
    op = int(input("Seleccione una opción "))
print("Que tenga buen día")