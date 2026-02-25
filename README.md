🧾 Sistema de Inventario con Flask

Aplicación web desarrollada en Python + Flask para gestionar un inventario de productos.
Permite agregar, editar, eliminar, visualizar productos y acceder a los datos mediante una API REST en JSON.

🚀 Funcionalidades

✅ Ver lista de productos en interfaz web

✅ Agregar productos

✅ Editar productos

✅ Eliminar productos

✅ Guardado persistente en archivo JSON

✅ API REST para acceso externo

✅ Validaciones en formularios

🛠️ Tecnologías utilizadas

Python 3

Flask

HTML

JSON

Thunder Client / Postman (para pruebas API)

📦 Instalación
1️⃣ Clonar repositorio
git clone https://github.com/TU-USUARIO/TU-REPO.git
cd TU-REPO
2️⃣ Crear entorno virtual
python -m venv venv

Activar:

Windows

venv\Scripts\activate

Mac / Linux

source venv/bin/activate
3️⃣ Instalar dependencias

Si tienes requirements.txt:

pip install -r requirements.txt

Si no:

pip install flask
4️⃣ Ejecutar aplicación
python app.py

Abrir en navegador:

http://127.0.0.1:5000/inventario
🌐 Endpoints de la API
📋 Obtener inventario

GET

/inventario/api
✅ Respuesta ejemplo
{
  "Laptop": {
    "precio": 500000,
    "cantidad": 5,
    "categoria": "Tecnologia"
  },
  "Mouse": {
    "precio": 10000,
    "cantidad": 10,
    "categoria": "Accesorios"
  }
}

Código esperado: 200 OK

➕ Agregar producto

POST

/inventario/api/agregar
📥 Body JSON
{
  "producto": "Teclado",
  "precio": 15000,
  "cantidad": 3,
  "categoria": "Accesorios"
}
✅ Respuesta ejemplo
{
  "mensaje": "Producto agregado correctamente"
}

Código esperado: 201 Created

✏️ Editar producto

PUT

/inventario/api/editar/<producto>

Ejemplo:

/inventario/api/editar/Teclado
📥 Body JSON
{
  "precio": 18000,
  "cantidad": 5,
  "categoria": "Perifericos"
}
✅ Respuesta ejemplo
{
  "mensaje": "Producto actualizado correctamente"
}

Código esperado: 200 OK

🗑️ Eliminar producto

DELETE

/inventario/api/eliminar/<producto>

Ejemplo:

/inventario/api/eliminar/Teclado
✅ Respuesta ejemplo
{
  "mensaje": "Producto eliminado correctamente"
}

Código esperado: 200 OK

🧪 Ejemplos de uso
✔️ Desde navegador

Abrir:

http://127.0.0.1:5000/inventario/api

Mostrará el inventario en JSON.

✔️ Desde Thunder Client

Abrir Thunder Client en VSCode

Crear nueva request

Elegir método (GET / POST / PUT / DELETE)

Escribir URL del endpoint

En POST o PUT → seleccionar Body → JSON

Enviar request

📸 Screenshots


<img width="562" height="500" alt="image" src="https://github.com/user-attachments/assets/bdf4f032-61a0-4602-b574-56b750dc80c0" />

<img width="562" height="500" alt="image" src="https://github.com/user-attachments/assets/d46c712e-bd0a-4106-911e-d4ed8fac964d" />

<img width="374" height="481" alt="image" src="https://github.com/user-attachments/assets/a2ee6aea-c874-4ffe-a2ff-e617fcf3ce5b" />


<img width="1219" height="528" alt="image" src="https://github.com/user-attachments/assets/be21a77d-7d7e-4fce-bb8b-052fcdbea6d9" />




Lista de productos

Agregar producto

Editar producto

API funcionando

📁 Estructura del proyecto
/proyecto
│── app.py
│── inventario.json
│── requirements.txt
│── /templates
│     └── /inventario
│            lista.html
│            agregar.html
│            editar.html
│── /modulos
│     inventario.py
👨‍💻 Autor

Desarrollado como proyecto académico para práctica de:

Flask

APIs REST

Manejo de JSON

Formularios HTML

📜 Licencia

Uso educativo.






🧪 Testing realizado
✔️ Pruebas funcionales

Se agregaron múltiples productos correctamente

Se editaron productos con cambios persistentes

Se eliminaron productos sin errores

La interfaz web funcionó correctamente

✔️ Pruebas API

GET devuelve inventario en JSON

POST crea productos correctamente

PUT actualiza productos

DELETE elimina productos

✔️ Casos extremos probados

nombres largos

precios altos

cantidades altas

caracteres especiales

productos inexistentes

✔️ Resultado

La aplicación funciona correctamente tras corregir validaciones menores.
