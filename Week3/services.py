
import csv

Inventario = []  # Lista principal del inventario

def agregar_producto(): # Agregar producto nuevo
    nombre = str(input("Nombre: "))
    precio = float(input("Precio: ")) 
    cantidad = int(input("Cantidad: "))

    Inventario.append({  # Agregar a la lista
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    })
    print("Producto agregado.\n")


def mostrar_inventario(): # Mostrar productos existentes
    if not Inventario:
        print("Inventario vacío.\n")
        return

    for p in Inventario:
        print(f"{p['nombre']} - ${p['precio']} - Cant: {p['cantidad']}")
    print() 


'''P (PRODUCTO)'''


def buscar_producto():  # Buscar producto por nombre
    nombre = input("Nombre del producto: ")

    for p in Inventario:
        if p["nombre"].lower() == nombre.lower():
            print("Encontrado:", p, "\n")
            return
    print("No encontrado.\n")

  
def actualizar_producto():  # Modificar datos de producto
    nombre = input("Producto a actualizar: ")

    for producto in Inventario:
        try:
            if producto["nombre"].lower() == nombre.lower():
                producto["precio"] = float(input("Nuevo precio: "))
                producto["cantidad"] = int(input("Nueva cantidad: "))
                print("Actualizado.\n")
                return
        except ValueError:
            print("Error: Entrada inválida. Intente nuevamente.")


def eliminar_producto():  # Eliminar producto
    nombre = input("Producto a eliminar: ")

    for p in Inventario:
        if p["nombre"].lower() == nombre.lower():
            Inventario.remove(p)
            print("Producto eliminado.\n")
            return
    print("No encontrado.\n")

 
def calcular_estadisticas():  # Muestra totales del inventario
    if len(Inventario) == 0:
        print("No hay productos para evaluar")
        return
    
    unidades_totales = sum(p["cantidad"]for p in Inventario) # Items totales
    total_inventario = sum(p["precio"] * p["cantidad"] for p in Inventario) # Valor total inventario
    print(f"El inventario tiene un total de: {unidades_totales} productos")
    print(f"Valor total del inventario: ${total_inventario}\n")
