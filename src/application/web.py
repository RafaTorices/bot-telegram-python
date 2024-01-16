import requests
from flask import render_template, request
from application.usuarios import Usuario
from application.config import TelegramConfig
from application.estado import Estado
from application.opciones import Opciones


def getWebhookInfo():
    apiURL = TelegramConfig.APIURL+TelegramConfig.TOKEN+"/getWebhookInfo"
    response = requests.get(apiURL)
    if response.status_code == 200:
        data = response.json()
        return render_template('get_webhook_info.html', data=data)
    else:
        return render_template('get_webhook_info.html', error="Error: "+response)


def listado_usuarios():
    usuarios = Usuario()
    usuarios = usuarios.listadoUsuariosWeb()
    return render_template('listado_usuarios.html', usuarios=usuarios)


def listado_opciones():
    opciones = Opciones()
    opciones = opciones.enviarOpcionesWeb()
    return render_template('listado_opciones.html', opciones=opciones)


def activar_usuario(id):
    if request.method == 'POST':
        id = request.form['id']
        usuario = Usuario()
        usuario.activarUsuarioWeb(id)
        usuarios = usuario.listadoUsuariosWeb()
        return render_template('listado_usuarios.html', usuarios=usuarios)


def desactivar_usuario(id):
    if request.method == 'POST':
        id = request.form['id']
        usuario = Usuario()
        usuario.desactivarUsuarioWeb(id)
        usuarios = usuario.listadoUsuariosWeb()
        return render_template('listado_usuarios.html', usuarios=usuarios)


def estado_servicio():
    estado = Estado()
    if request.method == 'GET':
        result = estado.comprobarEstado()
        return render_template('estado_servicio.html', estado=result)
    if request.method == 'POST':
        result = estado.comprobarEstado()
        if result == 0:
            estado.activarEstado()
            result = estado.comprobarEstado()
            return render_template('estado_servicio.html', estado=result)
        else:
            estado.desactivarEstado()
            result = estado.comprobarEstado()
            return render_template('estado_servicio.html', estado=result)
