import requests
from flask import render_template, request
from application.usuarios import Usuario
from application.config import TelegramConfig
from application.estado import Estado


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


def listado_usuarios_pendientes():
    usuarios = Usuario()
    usuarios = usuarios.listadoUsuariosPendientesWeb()
    return render_template('listado_usuarios_pendientes.html', usuarios=usuarios)


def activar_usuario():
    if request.method == 'POST':
        id = request.form['id']
        usuario = Usuario()
        usuario.activarUsuario(id)
        usuarios = usuario.listadoUsuariosPendientesWeb()
        return render_template('listado_usuarios_pendientes.html', usuarios=usuarios)


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
