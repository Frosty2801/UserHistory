

# Definimos la lista de inventario con estadísticas

listainventario = []


# Función para agregar un producto al inventario

def agregar_producto ():
    print("AGREGAR PRODUCTO")
    nombre = (input("producto a añadir: "))

# Validar precio y cantidad

    while True:
        try:
            precio = float(input("Ingrese el precio del producto: "))
            if precio < 0:
                print("Error precio negativo. Intentelo de nuevo.")
                continue
            break
        except ValueError:
            print("Error: Debe ingresar un número válido para el precio: ")

# Validar cantidad

    while True: 
        try: 
            cantidad = int(input("Ingresa cantidad del producto: "))
            if cantidad < 0:
                print("Error cantidad negativa")
                continue
            break
        except ValueError:
            print ("Error cantidad invalida, intente nuevamente: ")

# Crear diccionario del producto y agregar a la lista

    producto = {
        'nombre' : nombre,
        "precio" : precio,
        "cantidad" : cantidad
    }
    listainventario.append(producto)
    print(f"producto {nombre} agregado")

# Función para mostrar el inventario

def mostrar_inventario():
    print("  MOSTRANDO INVENTARIO  ")
    if len(listainventario) == 0:
        print("La lista esta vacia")
    else: 
        print(f"Total productos {listainventario}")
        print()

# Función para calcular estadísticas del inventario

def calcular_estadisticas():
    print("  ESTADISTICAS DEL INVENTARIO  ")
    if len(listainventario) == 0:
        print("No hay productos para evaluar")
    else:
        total_inventario = sum(p["precio"] * p["cantidad"] for p in listainventario)
        total_productos = sum (p["cantidad"]for p in listainventario)
        print(f"Valor total del inventario {total_inventario}")
        print(f"Productos totales en inventario {total_productos}")

# Función para mostrar el menú y manejar las opciones

def mostrar_menu ():
    print("  MENU OPCIONES  ")
    print("1. Agregar producto")
    print("2. Mostrar inventario")
    print("3. Calcular estadísticas")
    print("4. Salir")

# Función principal para llamar al menú y manejar la lógica

def llamar ():

# Bucle principal del programa
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opcion (1-4): ")
        
        if opcion == "1":
            agregar_producto()

        elif opcion == "2":
            mostrar_inventario()
        
        elif opcion == "3":
            calcular_estadisticas()

        elif opcion == "4":
            print("SALINDO DEL PROGRAMA")
            break

        else:
            print("Ingrese una opcion valida")


# Punto de entrada del programa
if __name__ == "__main__":
    llamar()

# El objetivo de esta semana es gestionar un inventario de productos, 
# permitiendo al usuario agregar productos, 
# mostrar el inventario y calcular estadísticas como el valor total del inventario y la cantidad total de productos.
# En este programa utilizamos listas y diccionarios para almacenar y manejar los datos de los productos



