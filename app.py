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

from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')
@app.route('/inventario')
def index():
    return render_template('inventario/lista.html', datos = datos)





