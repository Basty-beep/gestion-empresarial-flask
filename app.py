from modulos.inventario import cargar_inventario, guardar_inventario

from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)
@app.route('/')
@app.route('/inventario')
def index():
    datos = cargar_inventario()
    return render_template('inventario/lista.html', datos=datos)

# Agregar productos

@app.route('/inventario/agregar', methods = ['GET', 'POST'])
def agregar():
    if request.method == 'POST':
        producto = request.form['producto']
        precio = int(request.form['precio'])
        cantidad = int(request.form['cantidad'])
        categoria = request.form['categoria']

        # cargar inventario actual
        inventario = cargar_inventario()

        # agregar producto nuevo
        inventario[producto] = {
            "precio": precio,
            "cantidad": cantidad,
            "categoria": categoria
        }

        # guardar en el archivo json
        guardar_inventario(inventario)

        # volver a la lista
        return redirect(url_for('index'))
    return render_template('inventario/agregar.html')





