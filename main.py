import json

def cargar_datos():
    with open("datos.json", "r") as archivo:
        datos = json.load(archivo)
    return datos

def separador():
    print("-" * 30)