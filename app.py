from modulos.inventario import cargar_inventario, guardar_inventario

from flask import Flask, render_template, request, url_for, redirect, jsonify

from flask_sqlalchemy import SQLAlchemy

import json

app = Flask(__name__)
@app.route('/')
@app.route('/inventario')
def inventario():
    datos = cargar_inventario()
    return render_template('inventario/lista.html', datos=datos)


# Agregamos el endpoint GET

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///productos.db'
db = SQLAlchemy(app)

@app.route('/api/inventario', methods=['GET'])
def api_inventario():
    datos = cargar_inventario()
    return jsonify(datos)

# Agregamos endpoint POST
@app.route('/api/inventario', methods =['POST'])
def crear():
   
    data = request.get_json()

    # Validar que reciba información
    if not data:
        return jsonify({"error": "No se recibió JSON"}), 400

    # Ejemplos
    nombre = data.get("nombre")
    precio = data.get("precio")
    stock = data.get("stock")

    if not nombre or precio is None or stock is None:
        return jsonify({"error": "Faltan datos obligatorios"}), 400

    # 2. Cargar inventario actual
    inventario = cargar_inventario()

    # 3. Agregar producto
    inventario[nombre] = {
        "precio": precio,
        "stock": stock
    }

    # 4. Guardar inventario
    guardar_inventario(inventario)

    # 5. Respuesta exitosa
    return jsonify({
        "mensaje": "Producto creado correctamente",
        "producto": inventario[nombre]
    }), 201

# Endpoint GET por id
@app.route('api/inventario/<nombre>', methods = ['GET'])
def buscar_id(nombre):
    inventario = cargar_inventario()

    # verificar si existe el producto
    if nombre in inventario:
        return jsonify({
            "nombre": nombre,
            "info": inventario[nombre]
        }), 200

    # si no existe va a dar error 404
    return jsonify({
        "error": "Producto no encontrado"
    }), 404

# Endpoint DELETE
@app.route('/api/inventario/<nombre>', methods = ['DELETE'])
def endpoint_delete(nombre):

    inventario = cargar_inventario()

    if nombre in inventario:
        eliminado = inventario.pop(nombre)   

        guardar_inventario(inventario)       

        return jsonify({
            "mensaje": "Producto eliminado correctamente",
            "producto": nombre,
            "datos": eliminado
        }), 200

    # si no encuentra nada devuelve error 404
    return jsonify({
        "error": "Producto no encontrado"
    }), 404



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
        return redirect(url_for('inventario'))
    return render_template('inventario/agregar.html')


# Eliminar productos
@app.route('/inventario/eliminar/<nombre>')
def eliminar(nombre):

    # cargar inventario actual
    inventario = cargar_inventario()

    # verificar si existe el producto
    if nombre in inventario:
        del inventario[nombre]   # eliminar producto
        guardar_inventario(inventario)

    # volver a la lista
    return redirect(url_for('inventario'))

# Editar producto
@app.route('/inventario/editar/<nombre>', methods=['GET','POST'])
def editar(nombre):

    datos = cargar_inventario()

    if nombre not in datos:
        return "Producto no encontrado"

    if request.method == 'POST':

        nuevo_nombre = request.form['nombre']
        precio = int(request.form['precio'])
        cantidad = int(request.form['cantidad'])
        categoria = request.form['categoria']

        datos.pop(nombre)

        datos[nuevo_nombre] = {
            "precio": precio,
            "cantidad": cantidad,
            "categoria": categoria
        }

        guardar_inventario(datos)

        return redirect(url_for('inventario'))

    return render_template(
        'inventario/editar.html',
        nombre=nombre,
        info=datos[nombre]
    )
if __name__ == '__main__':
    app.run(debug=True)