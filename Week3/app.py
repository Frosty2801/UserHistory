
from services import (
    agregar_producto, mostrar_inventario, buscar_producto, 
    actualizar_producto, eliminar_producto, 
    calcular_estadisticas,

)

from archives import cargar_csv, guardar_csv


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

