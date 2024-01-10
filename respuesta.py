from usuarios import Usuario
from estado import Estado
from metodos import MetodosTelegram
from config import TelegramConfig
from opciones import Opciones


class Respuesta():
    def __init__(self):
        self.metodos = MetodosTelegram()
        self.config = TelegramConfig()
        self.opciones = Opciones()
        self.estado = Estado()
        self.usuario = Usuario()

    def enviarRespuesta(self, chatId, text, first_name):
        if text == '/OPCIONES' or text == '/opciones':
            respuesta = self.config.TITULO_APP + \
                "Tu respuesta es "+text+self.config.EMAIL_SOPORTE
            self.metodos.sendMessage(chatId, respuesta)
            return self.metodos.sendKeyboard(chatId, self.opciones.enviarOpciones())
        elif text == 'ACTIVAR_SERVICIO' or text == 'activar_servicio':
            if chatId == self.config.CHAT_ID_SOPORTE:
                self.estado.activarEstado()
                respuesta = self.config.TITULO_APP + \
                    "OK, SERVICIO ACTIVADO"+self.config.EMAIL_SOPORTE
                self.metodos.sendMessage(chatId, respuesta)
        elif text == 'DESACTIVAR_SERVICIO' or text == 'desactivar_servicio':
            if chatId == self.config.CHAT_ID_SOPORTE:
                self.estado.desactivarEstado()
                respuesta = self.config.TITULO_APP + \
                    "OK, SERVICIO DESACTIVADO"+self.config.EMAIL_SOPORTE
                self.metodos.sendMessage(chatId, respuesta)
        elif text == '/LISTADO_USUARIOS':
            if chatId == self.config.CHAT_ID_SOPORTE:
                respuesta = self.config.TITULO_APP + \
                    "LISTADO DE USUARIOS: \n\n"+self.usuario.listadoUsuarios()+self.config.EMAIL_SOPORTE
                self.metodos.sendMessage(
                    self.config.CHAT_ID_SOPORTE, respuesta)
        elif text == '/LISTADO_USUARIOS_PENDIENTES':
            if chatId == self.config.CHAT_ID_SOPORTE:
                respuesta = self.config.TITULO_APP + \
                    "LISTADO DE USUARIOS PENDIENTES DE AUTORIZACIÓN: \n\n" + \
                    self.usuario.listadoUsuariosPendientes()+self.config.EMAIL_SOPORTE
                self.metodos.sendMessage(
                    self.config.CHAT_ID_SOPORTE, respuesta)
        elif text == '/LISTADO_USUARIOS_AUTORIZADOS':
            if chatId == self.config.CHAT_ID_SOPORTE:
                respuesta = self.config.TITULO_APP + \
                    "LISTADO DE USUARIOS AUTORIZADOS: \n\n" + \
                    self.usuario.listadoUsuariosAutorizados()+self.config.EMAIL_SOPORTE
                self.metodos.sendMessage(
                    self.config.CHAT_ID_SOPORTE, respuesta)
        else:
            respuesta = self.config.TITULO_APP + \
                "Lo siento "+first_name + \
                ", pero no entiendo lo que me dices ("+text+" - "+chatId + \
                ")\n\nPrueba con una de mis /OPCIONES"+self.config.EMAIL_SOPORTE
            self.metodos.sendMessage(chatId, respuesta)
            keyboard = self.opciones.enviarOpciones()
            return self.metodos.sendKeyboard(chatId, keyboard)
