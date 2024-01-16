import requests
from flask import render_template, request
from application.usuarios import Usuario
from application.config import TelegramConfig
from application.estado import Estado
from application.opciones import Opciones
from application.metodos import MetodosTelegram


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


def editar_opcion(id):
    if request.method == 'POST':
        id = request.form['id']
        opcion = request.form['opcion']
        texto = request.form['texto']
        opciones = Opciones()
        opciones.editarOpcion(id, opcion, texto)
        opciones = opciones.enviarOpcionesWeb()
        mensaje = opcion+" editada correctamente."
        return render_template('listado_opciones.html', opciones=opciones, mensaje=mensaje)


def activar_desactivar_usuario(id, first_name, chatId, estado):
    if request.method == 'POST':
        id = request.form['id']
        first_name = request.form['first_name']
        chatId = request.form['chatId']
        estado = request.form['estado']
        usuario = Usuario()
        metodos = MetodosTelegram()
        if (estado == "1"):
            usuario.desactivarUsuarioWeb(id)
            mensaje = "Usuario " + first_name + \
                " desactivado correctamente e informado por Telegram."
            metodos.sendMessage(
                chatId, "Hola "+first_name+", tu usuario ha sido desactivado. Contacta con Soporte para más información.")
        else:
            usuario.activarUsuarioWeb(id)
            mensaje = "Usuario " + first_name + \
                " activado correctamente e informado por Telegram."
            metodos.sendMessage(
                chatId, "Hola "+first_name+", tu usuario ha sido activado. Ya puedes utilizar el Bot.")
        usuarios = usuario.listadoUsuariosWeb()
        return render_template('listado_usuarios.html', usuarios=usuarios, mensaje=mensaje)


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
