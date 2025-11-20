import csv
from services import Inventario

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

