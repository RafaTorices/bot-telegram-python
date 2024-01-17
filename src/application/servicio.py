from application.respuesta import Respuesta
from application.metodos import MetodosTelegram
from application.config import TelegramConfig
import json
from application.usuarios import Usuario
from application.estado import Estado
from application.opciones import Opciones


class Servicio():

    def __init__(self, data):
        # Obtengo los datos de config de telegram
        config = TelegramConfig()
        self.ApiUrl = config.APIURL
        self.token = config.TOKEN
        self.chatIdSoporte = config.CHAT_ID_SOPORTE
        self.emailSoporte = config.EMAIL_SOPORTE
        self.tituloApp = config.TITULO_APP
        self.metodos = MetodosTelegram()
        self.usuario = Usuario()
        self.estado = Estado()
        self.respuesta = Respuesta()
        self.opciones = Opciones()

        ficheroJson = 'data.json'

        # Obtengo la data con el mensaje del usuario
        self.data = data
        # Creo un fichero json vacio
        with open(ficheroJson, 'w') as file:
            file.write('')
        # Añado los [] para estructura json
        with open(ficheroJson, 'a') as file:
            file.write('[')
        # Inserto mi data en el json
        with open(ficheroJson, 'a') as file:
            json.dump(self.data, file)
        # Cierro []
        with open(ficheroJson, 'a') as file:
            file.write(']')
        # Leo el fichero json y lo guardo en mi data para acceder a los datos
        with open(ficheroJson) as file:
            self.data = json.load(file)
        # Si la data no esta vacía
        if self.data != []:
            # Recorro el json
            for dato in self.data:
                try:
                    # Obtengo los parametros del mensaje
                    chatId = str(dato['message']['chat']['id'])
                    first_name = str(dato['message']['chat']['first_name'])
                    username = str(dato['message']['chat']['username'])
                    # date = dato['message']['date']
                    text = str(dato['message']['text'])
                    # Inserto el mensaje en la BD
                    self.usuario.guardarMensajeUsuario(chatId, first_name, text, username)
                except Exception:
                    print("Error: "+Exception)
                # Envio respuesta
                # Primero compruebo el estado del servicio y el usuario
                estadoActual = self.estado.comprobarEstado()
                usuarioActual = self.usuario.comprobarUsuario(chatId)
                # Compruebo el usuario, si no esta guardado en BD lo guardo
                if usuarioActual == 0:
                    self.usuario.guardarUsuario(chatId, first_name, username)
                    # y le doy la bienvenida al sistema como usuario nuevo
                    text = self.tituloApp+"Hola "+first_name + \
                        " !!,\nBienvenido a nuestro sistema informático automatizado.\n\nAquí tienes nuestras /OPCIONES"+self.emailSoporte
                    self.metodos.sendMessage(chatId, text)
                else:
                    # Una vez comprobado el usuario compruebo el servicio
                    # Si esta fuera de servicio y el usuario no es el admin se lo comunico
                    if (estadoActual == 0 and chatId != self.chatIdSoporte):
                        notas = self.estado.obtenerNotasEstado()
                        text = self.tituloApp+"El sistema está fuera de servicio en este momento:\n\n" + \
                            notas+"\n\nPor favor, pruebe de nuevo más tarde."+self.emailSoporte
                        self.metodos.sendMessage(chatId, text)
                    # Si no esta fuera de servicio o es el admin...
                    else:
                        # Compruebo si es autorizado del sistema
                        # Si es autorizado o es admin procesamos su mensaje y le damos respuesta
                        if self.usuario.comprobarUsuarioAutorizado(chatId) == 1 or chatId == self.chatIdSoporte:
                            self.respuesta.enviarRespuesta(
                                chatId, text, first_name)
                        # Si no es autorizado ni admin se lo decimos y le mandamos las opciones pertinentes
                        else:
                            # Si el mensaje enviado es solicitud de acceso le mandamos a admin la solicitud y las opciones
                            if text == '/SOLICITAR_ACCESO' and chatId != self.chatIdSoporte:
                                if self.usuario.comprobarSolicitudUsuario(chatId) == 0:
                                    text = self.tituloApp+"Solicitud de acceso del Usuario: \n\n" + \
                                        first_name+" - ("+chatId+")" + \
                                        self.emailSoporte
                                    # self.metodos.sendKeyboard(
                                    #     self.chatIdSoporte, self.opciones.enviarOpcionesSolicitud(chatId, first_name))
                                    # Al usuario le comunicamos que ha enviado correctamente una solicitud de acceso
                                    # Actualizamos su estado de solicitud a pendiente
                                    self.usuario.solicitudUsuario(chatId)
                                    self.metodos.sendMessage(
                                        self.chatIdSoporte, text)
                                    text = self.tituloApp + \
                                        "Su solicitud de acceso ha sido enviada a Soporte Técnico.\nEn breve recibirá una respuesta."+self.emailSoporte
                                    self.metodos.sendMessage(chatId, text)
                                # Si ya esta solicitada previamente se lo decimos al usuario y al admin se lo recordamos
                                else:
                                    text = self.tituloApp + \
                                        "Ya tiene una solicitud de acceso pendiente, espere a obtener respuesta desde Soporte Técnico.\nEn breve recibirá una respuesta."+self.emailSoporte
                                    self.metodos.sendMessage(chatId, text)
                                    text = self.tituloApp+"Recuerde la Solicitud de acceso del Usuario: \n\n" + \
                                        first_name+" - ("+chatId+")" + \
                                        self.emailSoporte
                                    self.metodos.sendMessage(
                                        self.chatIdSoporte, text)
                                    # self.metodos.sendKeyboard(
                                    #     self.chatIdSoporte, self.opciones.enviarOpcionesSolicitud(chatId, first_name))
                            # Si no es autorizado..
                            else:
                                text = self.tituloApp+"Lo sentimos "+first_name + \
                                    ", pero este sistema es para usuarios autorizados.\nSolicite su acceso si lo cree necesario:\n\n/SOLICITAR_ACCESO"+self.emailSoporte
                                self.metodos.sendMessage(chatId, text)
                # Vacío el fichero
                with open(ficheroJson, 'w') as file:
                    file.write('')
