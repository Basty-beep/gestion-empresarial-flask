from modulos.inventario import cargar_inventario, guardar_inventario

# inventario de prueba
inventario_prueba = {
    "lapiz": {"precio": 100, "cantidad": 10, "categoria": "utiles"},
    "cuaderno": {"precio": 1500, "cantidad": 5, "categoria": "utiles"}
}

# guardar datos
guardar_inventario(inventario_prueba)

# cargar datos
datos = cargar_inventario()

print(datos)

print("Guardando inventario...")
guardar_inventario(inventario_prueba)

print("Cargando inventario...")
datos = cargar_inventario()

print("Datos cargados:", datos)
