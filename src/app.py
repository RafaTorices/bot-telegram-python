
from flask import Flask, request, render_template
from app.servicio import Servicio

app = Flask(__name__, template_folder='app/templates')


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
    app.run(debug=True, port=5000)
