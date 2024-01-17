from dotenv import load_dotenv
from flask import Flask, request, render_template, url_for
from application.web import webhook, getWebhookInfo, listado_usuarios, \
    estado_servicio, activar_desactivar_usuario, \
    listado_opciones, editar_opcion, enviar_mensajes , listado_mensajes \
    , deleteWebhook, setWebhook
from application.config import TelegramConfig

load_dotenv()

app = Flask(__name__, template_folder='application/templates',
            static_folder='application/static')


@app.route('/', methods=['GET'])
def index():
    titulo = TelegramConfig.TITULO_APP
    return render_template('home.html', titulo=titulo)


@app.errorhandler(404)
def error404_(error):
    titulo = TelegramConfig.TITULO_APP
    return render_template('404.html', titulo=titulo)


@app.route('/webhook', methods=['GET', 'POST'])
def webhook_():
    return webhook()

@app.route('/getWebhookInfo', methods=['GET'])
def getWebhookInfo_():
    return getWebhookInfo()

@app.route('/setWebhook', methods=['POST'])
def setWebhook_():
    return setWebhook()

@app.route('/deleteWebhook', methods=['GET'])
def deleteWebhook_():
    return deleteWebhook()


@app.route('/listado_usuarios', methods=['GET'])
def listado_usuarios_():
    return listado_usuarios()


@app.route('/listado_opciones', methods=['GET'])
def listado_opciones_():
    return listado_opciones()


@app.route('/editar_opcion', methods=['POST'])
def editar_opcion_():
    return editar_opcion(id)


@app.route('/activar_desactivar_usuario', methods=['POST'])
def activar_desactivar_usuario_():
    first_name = request.form['first_name']
    id = request.form['id']
    estado = request.form['estado']
    chatId = request.form['chatId']
    return activar_desactivar_usuario(id, first_name, chatId, estado)


@app.route('/estado_servicio', methods=['POST', 'GET'])
def estado_servicio_():
    return estado_servicio()

@app.route('/enviar_mensajes', methods=['POST', 'GET'])
def enviar_mensajes_():
    return enviar_mensajes()

@app.route('/listado_mensajes', methods=['GET'])
def listado_mensajes_():
    return listado_mensajes()

if __name__ == "__main__":
    with app.test_request_context():
        home = url_for('index')
        webhookurl = url_for('webhook_')
        listadousuarios = url_for('listado_usuarios_')
        getwebhookinfo = url_for('getWebhookInfo_')
        estadoservicio = url_for('estado_servicio_')
        activardesactivarusuario = url_for('activar_desactivar_usuario_')
        listadoopciones = url_for('listado_opciones_')
        enviarmensajes = url_for('enviar_mensajes_')
        listadomensajes = url_for('listado_mensajes_')
        deletewebhook = url_for('deleteWebhook_')
        setwebhook = url_for('setWebhook_')
    app.run()
