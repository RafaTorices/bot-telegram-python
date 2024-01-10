
from flask import Flask, request, render_template, jsonify
from servicio import Servicio

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def __init__():

    # Compruebo si es un POST
    if request.method == 'POST':
        # Llamo a la clase que inicia el servicio
        Servicio(request.json)
        return render_template('home.html')

    # Si es una peticion GET le devuelvo la home html
    if request.method == 'GET':
        return render_template('home.html')


if __name__ == "__main__":
    app.run(debug=True)
