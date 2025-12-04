import csv
from services import Inventario  # Se usa la lista compartida

def guardar_csv():  # Guarda inventario en archivo CSV
    archivo = input("Ingrese nombre del archivo (*.csv): ")

    with open(archivo, "w", newline="") as detalles:
        writer = csv.writer(detalles)
        writer.writerow(["nombre", "precio", "cantidad"])  # Encabezado

        for p in Inventario:
            writer.writerow([p["nombre"], p["precio"], p["cantidad"]])
    print("Inventario guardado. \n")

def cargar_csv():  # Carga inventario desde CSV
    archivo = input("Archivo CSV a cargar: ")

    try:
        with open(archivo, "r") as detalles:
            reader = csv.reader(detalles)
            next(reader)  # Saltar encabezado
            
            Inventario.clear()  # Limpiar lista

            for row in reader:
                nombre, precio, cantidad = row  # Extraer datos
                Inventario.append({
                    "nombre": nombre,
                    "precio": float(precio),
                    "cantidad": int(cantidad)
                })

        print("Inventario cargado.\n")

    except FileNotFoundError:
        print("Archivo no encontrado.\n")

