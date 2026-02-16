import json

def cargar_inventario(archivo="datos/inventario.json"):
    try:
        with open(archivo, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def guardar_inventario(inventario, archivo="datos/inventario.json"):
    with open(archivo, "w", encoding="utf-8") as f:
        json.dump(inventario, f, indent=4, ensure_ascii=False)