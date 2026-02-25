import json, os

def cargar_inventario(archivo="datos/inventario.json"):
    if not os.path.exists(archivo):
        return {}

    with open(archivo, "r", encoding="utf-8") as f:
        return json.load(f)

def guardar_inventario(inventario, archivo="datos/inventario.json"):
    os.makedirs(os.path.dirname(archivo), exist_ok=True)

    with open(archivo, "w", encoding="utf-8") as f:
        json.dump(inventario, f, indent=4, ensure_ascii=False)