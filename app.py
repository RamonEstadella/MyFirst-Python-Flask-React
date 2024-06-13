'''
Estas líneas importan las bibliotecas necesarias:

Flask: el microframework que utilizamos para crear el servidor web.
request: para acceder a los datos de las solicitudes HTTP.
jsonify: para convertir los datos a formato JSON.
CORS: para permitir solicitudes desde un dominio diferente (necesario para conectar el frontend y el backend).

'''
from flask import Flask, request, jsonify  # Importa las bibliotecas necesarias de Flask
from flask_cors import CORS  # Importa CORS para permitir solicitudes desde un dominio diferente


'''
Estas líneas inicializan la aplicación Flask y configuran CORS para permitir que el frontend de React se comunique con el backend de Flask.
'''
app = Flask(__name__)  # Inicializa la aplicación Flask
CORS(app)  # Configura CORS para permitir que el frontend de React se comunique con el backend de Flask

@app.route('/api/books', methods=['GET'])  # Define una ruta para la solicitud GET en /api/books
def get_books():  # Define la función que maneja las solicitudes GET
    books = [  # Crea una lista de libros como ejemplo
        {'title': 'Book 1', 'author': 'Author 1'},
        {'title': 'Book 2', 'author': 'Author 2'},
    ]
    return jsonify(books)  # Devuelve la lista de libros en formato JSON

@app.route('/api/books', methods=['POST'])  # Define una ruta para la solicitud POST en /api/books
def add_book():  # Define la función que maneja las solicitudes POST
    new_book = request.json  # Obtiene los datos del nuevo libro enviados en la solicitud POST
    # Aquí deberías añadir el libro a tu base de datos o lista
    return jsonify(new_book), 201  # Devuelve los datos del nuevo libro en formato JSON y una respuesta HTTP 201

if __name__ == '__main__':  # Verifica si el archivo se está ejecutando directamente
    app.run(debug=True)  # Inicia el servidor Flask en modo debug

