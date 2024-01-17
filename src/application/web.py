import requests
from flask import render_template, request
from application.usuarios import Usuario
from application.config import TelegramConfig
from application.estado import Estado
from application.opciones import Opciones
from application.metodos import MetodosTelegram
from application.servicio import Servicio


def webhook():
    if request.method == 'POST':
        Servicio(request.json)
        return render_template('home.html')
    if request.method == 'GET':
        return render_template('home.html')


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
    usuarios = Usuario()
    if request.method == 'GET':
        notas = estado.obtenerNotasEstado()
        result = estado.comprobarEstado()
        return render_template('estado_servicio.html', notas=notas, estado=result)
    if request.method == 'POST':
        result = estado.comprobarEstado()
        if result == 0:
            estado.activarEstado()
            result = estado.comprobarEstado()
            for row in usuarios.chatIdUsuarios():
                chatId = row[0]
                metodos = MetodosTelegram()
                metodos.sendMessage(
                    chatId, "El servicio ha sido activado. Ya puedes utilizar el Bot.")
            return render_template('estado_servicio.html', estado=result)
        else:
            nuevasNotas = request.form['notas']
            estado.actualizarNotasEstado(nuevasNotas)
            notas = estado.obtenerNotasEstado()
            estado.desactivarEstado()
            result = estado.comprobarEstado()
            for row in usuarios.chatIdUsuarios():
                chatId = row[0]
                metodos = MetodosTelegram()
                metodos.sendMessage(
                    chatId, "El servicio ha sido desactivado por: \n\n" + notas + "\n\nDisculpa las molestias.")
            return render_template('estado_servicio.html', estado=result, notas=notas)

def enviar_mensajes():
    if request.method == 'GET':
        usuarios = Usuario()
        usuarios = usuarios.listadoUsuariosWeb()
        return render_template('enviar_mensajes.html', usuarios=usuarios)
    if request.method == 'POST':
        config = TelegramConfig()
        titulo = config.TITULO_APP 
        chatId = request.form['chatId']
        mensaje = titulo + request.form['mensaje']
        metodos = MetodosTelegram()
        metodos.sendMessage(chatId, mensaje)
        usuarios = Usuario()
        usuarios = usuarios.listadoUsuariosWeb()
        return render_template('enviar_mensajes.html', mensaje="Mensaje enviado correctamente.", usuarios=usuarios)