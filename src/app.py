
from flask import Flask, request, render_template, url_for
import requests
from application.servicio import Servicio
from application.usuarios import Usuario
from application.config import TelegramConfig

app = Flask(__name__, template_folder='application/templates',
            static_folder='application/static')


@app.route('/', methods=['POST', 'GET'])
def index():
    # Compruebo si es un POST
    if request.method == 'POST':
        # Llamo a la clase que inicia el servicio
        Servicio(request.json)
        return render_template('home.html')

    # Si es una peticion GET le devuelvo la home html
    if request.method == 'GET':
        return render_template('home.html')


@app.route('/getWebhookInfo', methods=['GET'])
def getWebhookInfo():
    apiURL = TelegramConfig.APIURL+TelegramConfig.TOKEN+"/getWebhookInfo"
    response = requests.get(apiURL)
    if response.status_code == 200:
        data = response.json()
        return render_template('get_webhook_info.html', data=data)
    else:
        return render_template('get_webhook_info.html', error="Error: "+response)


@app.route('/list_users', methods=['GET'])
def list_users():
    usuarios = Usuario()
    usuarios = usuarios.listadoUsuarios()
    return render_template('list_users.html', usuarios=usuarios)


if __name__ == "__main__":
    with app.test_request_context():
        # Generate URLs using url_for()
        home = url_for('index')
        listusers = url_for('list_users')
        getwebhookinfo = url_for('getWebhookInfo')
    app.run()
