
from flask import Flask, request, render_template, url_for
from application.servicio import Servicio
from application.web import getWebhookInfo, listado_usuarios, \
    estado_servicio, activar_usuario, desactivar_usuario, listado_opciones

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
def getWebhookInfo_():
    return getWebhookInfo()


@app.route('/listado_usuarios', methods=['GET'])
def listado_usuarios_():
    return listado_usuarios()


@app.route('/listado_opciones', methods=['GET'])
def listado_opciones_():
    return listado_opciones()


@app.route('/activar_usuario', methods=['POST'])
def activar_usuario_():
    return activar_usuario(id)


@app.route('/desactivar_usuario', methods=['POST'])
def desactivar_usuario_():
    return desactivar_usuario(id)


@app.route('/estado_servicio', methods=['POST', 'GET'])
def estado_servicio_():
    return estado_servicio()


if __name__ == "__main__":
    with app.test_request_context():
        home = url_for('index')
        listadousuarios = url_for('listado_usuarios_')
        getwebhookinfo = url_for('getWebhookInfo_')
        estadoservicio = url_for('estado_servicio_')
        activarusuario = url_for('activar_usuario_')
        desactivarusuario = url_for('desactivar_usuario_')
        listadoopciones = url_for('listado_opciones_')
    app.run()
