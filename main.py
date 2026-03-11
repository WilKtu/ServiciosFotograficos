import json

def cargar_datos():
    with open("datos.json", "r") as archivo:
        datos = json.load(archivo)
    return datos

def guardar_datos(datos):
    with open("datos.json", "w") as archivo:
        json.dump(datos, archivo, indent=4)
        
def agregar_servicio(datos):
    id_servicio = input("Ingrese el ID del servicio: ")
    nombre = input("Ingrese el nombre del servicio: ")
    descripcion = input("Ingrese la descripción del servicio: ")
    precio = float(input("Ingrese el precio del servicio: "))
    
    nuevo_servicio = {
        "id": id_servicio,
        "nombre": nombre,
        "descripcion": descripcion,
        "precio": precio
    }
    
    datos.append(nuevo_servicio)
    guardar_datos(datos)
    print("Servicio fotográfico agregado exitosamente.")

def mostrar_servicios(datos):
    if not datos:
        print("No hay servicios fotográficos disponibles.")
        return
    for servicio in datos:
        print(f"ID: {servicio['id']}")
        print(f"Nombre: {servicio['nombre']}")
        print(f"Descripción: {servicio['descripcion']}")
        print(f"Precio: ${servicio['precio']}")
        separador()

def separador():
    print("-" * 30)

def menu():
    print("1. Agregar servicio fotográfico")
    print("2. Editar servicio fotográfico")
    print("3. Eliminar servicio fotográfico")
    print("4. Salir")

