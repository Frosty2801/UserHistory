
'''Docstring'''

import csv

Inventario = []


def agregar_producto():
    nombre = str(input("Nombre: "))
    precio = float(input("Precio: ")) 
    cantidad = int(input("Cantidad: "))

    Inventario.append({
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    })
    print("Producto agregado.\n")


def mostrar_inventario():
    if not Inventario:
        print("Inventario vacío.\n")
        return

    for p in Inventario:
        print(f"{p['nombre']} - ${p['precio']} - Cant: {p['cantidad']}")
    print() 


'''P (PRODUCTO)'''


def buscar_producto():
    nombre = input("Nombre del producto: ")

    for p in Inventario:
        if p["nombre"].lower() == nombre.lower():
            print("Encontrado:", p, "\n")
            return
    print("No encontrado.\n")


def actualizar_producto():
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


def eliminar_producto():
    nombre = input("Producto a eliminar: ")

    for p in Inventario:
        if p["nombre"].lower() == nombre.lower():
            Inventario.remove(p)
            print("Producto eliminado.\n")
            return
    print("No encontrado.\n")



def calcular_estadisticas():
    if len(Inventario) == 0:
        print("No hay productos para evaluar")
        return
    
    unidades_totales = sum(p["cantidad"]for p in Inventario)
    total_inventario = sum(p["precio"] * p["cantidad"] for p in Inventario)
    print(f"El inventario tiene un total de: {unidades_totales} productos")
    print(f"Valor total del inventario: ${total_inventario}\n")


def guardar_csv():
    archivo = input("Ingrese nombre del archivo (*.csv): ")

    with open(archivo, "w", newline="") as detalles:
        writer = csv.writer(detalles)
        writer.writerow(["nombre", "precio", "cantidad"])

        for p in Inventario:
            writer.writerow([p["nombre"], p["precio"], p["cantidad"]])
    print("Inventario guardado. \n")

def cargar_csv():
    archivo = input("Archivo CSV a cargar: ")

    try:
        with open(archivo, "r") as detalles:
            reader = csv.reader(detalles)
            next(reader)
            
            Inventario.clear()

            for row in reader:
                nombre, precio, cantidad = row
                Inventario.append({
                    "nombre": nombre,
                    "precio": float(precio),
                    "cantidad": int(cantidad)
                })

        print("Inventario cargado.\n")

    except FileNotFoundError:
        print("Archivo no encontrado.\n")


def menu():
    while True:
        print(""""
        ===================
            MENU INVENTARIO
        ===================
        1. agregar producto
        2. mostrar inventario
        3. buscar producto
        4. actualizar producto
        5. eliminar producto
        6. calcular estadisticas  
        7. guardar csv
        8. cargar csv
        9. salir
        """)
            
        op = input("elija una opcion: ")

        if op == "1": agregar_producto()
        elif op == "2": mostrar_inventario()
        elif op == "3": buscar_producto()
        elif op == "4": actualizar_producto()
        elif op == "5": eliminar_producto()
        elif op == "6": calcular_estadisticas()
        elif op == "7": guardar_csv()
        elif op == "8": cargar_csv()
        elif op == "9":
            print("Adiós")
            break
        else:
            print("Opción inválida.\n")


menu()