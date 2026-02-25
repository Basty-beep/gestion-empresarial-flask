from modulos.inventario import cargar_inventario, guardar_inventario
from flask import Flask, render_template, request, url_for, redirect, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# LISTA DE PRODUCTOS
@app.route('/')
@app.route('/inventario')
def inventario():
    datos = cargar_inventario()

    buscar = request.args.get('buscar', '').lower()
    categoria = request.args.get('categoria', '')

    filtrados = {}

    for nombre, info in datos.items():
        coincide_nombre = buscar in nombre.lower() if buscar else True
        coincide_categoria = info.get("categoria") == categoria if categoria else True

        if coincide_nombre and coincide_categoria:
            filtrados[nombre] = info

    categorias = sorted(set(info.get("categoria", "") for info in datos.values()))

    return render_template(
        'inventario/lista.html',
        datos=filtrados,
        categorias=categorias,
        buscar=buscar,
        categoria=categoria
    )


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///productos.db'
db = SQLAlchemy(app)


# ENDPOINT GET

@app.route('/api/inventario', methods=['GET'])
def api_inventario():
    return jsonify(cargar_inventario())


# ENDPOINT POST

@app.route('/api/inventario', methods=['POST'])
def crear():

    data = request.get_json()
    if not data:
        return jsonify({"error": "No se recibió JSON"}), 400

    nombre = str(data.get("nombre", "")).strip()
    precio = data.get("precio")
    stock = data.get("stock")

    if not nombre or precio is None or stock is None:
        return jsonify({"error": "Faltan datos obligatorios"}), 400

    # validar tipos
    try:
        precio = int(precio)
        stock = int(stock)
    except:
        return jsonify({"error": "Precio y stock deben ser números"}), 400

    inventario = cargar_inventario()

    if nombre in inventario:
        return jsonify({"error": "El producto ya existe"}), 400

    if precio < 0:
        return jsonify({"error": "El precio no puede ser negativo"}), 400

    if stock <= 0:
        return jsonify({"error": "El stock debe ser positivo"}), 400

    inventario[nombre] = {
        "precio": precio,
        "cantidad": stock
    }

    guardar_inventario(inventario)

    return jsonify({
        "mensaje": "Producto creado correctamente",
        "producto": inventario[nombre]
    }), 201


# ENDPOINT GET POR ID

@app.route('/api/inventario/<nombre>', methods=['GET'])
def buscar_id(nombre):

    inventario = cargar_inventario()

    if nombre in inventario:
        return jsonify({
            "nombre": nombre,
            "info": inventario[nombre]
        }), 200

    return jsonify({"error": "Producto no encontrado"}), 404


# ENDPOINT DELETE

@app.route('/api/inventario/<nombre>', methods=['DELETE'])
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

    return jsonify({"error": "Producto no encontrado"}), 404


# AGREGAR PRODUCTO

@app.route('/inventario/agregar', methods=['GET', 'POST'])
def agregar():

    if request.method == 'POST':

        producto = request.form['producto'].strip()
        categoria = request.form['categoria']

        try:
            precio = int(request.form['precio'])
            cantidad = int(request.form['cantidad'])
        except:
            return render_template('inventario/agregar.html',
                                   error="Precio y cantidad deben ser números")

        inventario = cargar_inventario()

        if producto in inventario:
            return render_template('inventario/agregar.html',
                                   error="El producto ya existe")

        if precio < 0:
            return render_template('inventario/agregar.html',
                                   error="El precio no puede ser negativo")

        if cantidad <= 0:
            return render_template('inventario/agregar.html',
                                   error="La cantidad debe ser mayor a 0")

        inventario[producto] = {
            "precio": precio,
            "cantidad": cantidad,
            "categoria": categoria
        }

        guardar_inventario(inventario)

        return redirect(url_for('inventario'))

    return render_template('inventario/agregar.html')


# ELIMINAR PRODUCTO

@app.route('/inventario/eliminar/<nombre>')
def eliminar(nombre):

    inventario = cargar_inventario()

    if nombre in inventario:
        del inventario[nombre]
        guardar_inventario(inventario)

    return redirect(url_for('inventario'))


# EDITAR PRODUCTO

@app.route('/inventario/editar/<nombre>', methods=['GET','POST'])
def editar(nombre):

    datos = cargar_inventario()

    if nombre not in datos:
        return "Producto no encontrado"

    if request.method == 'POST':

        nuevo_nombre = request.form['nombre'].strip()
        categoria = request.form['categoria']

        try:
            precio = int(request.form['precio'])
            cantidad = int(request.form['cantidad'])
        except:
            return render_template(
                'inventario/editar.html',
                nombre=nombre,
                info=datos[nombre],
                error="Precio y cantidad deben ser números"
            )

        # validaciones
        if nuevo_nombre != nombre and nuevo_nombre in datos:
            return render_template(
                'inventario/editar.html',
                nombre=nombre,
                info=datos[nombre],
                error="Ya existe un producto con ese nombre"
            )

        if precio < 0:
            return render_template(
                'inventario/editar.html',
                nombre=nombre,
                info=datos[nombre],
                error="El precio no puede ser negativo"
            )

        if cantidad <= 0:
            return render_template(
                'inventario/editar.html',
                nombre=nombre,
                info=datos[nombre],
                error="La cantidad debe ser mayor a 0"
            )

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