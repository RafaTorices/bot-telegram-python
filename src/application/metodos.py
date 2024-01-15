from application.config import TelegramConfig
import requests
import json


class MetodosTelegram():
    def __init__(self):
        # Obtengo los datos de config de telegram
        config = TelegramConfig()
        self.ApiUrl = config.APIURL
        self.token = config.TOKEN
        self.chatIdSoporte = config.CHAT_ID_SOPORTE
        self.emailSoporte = config.EMAIL_SOPORTE
        self.tituloApp = config.TITULO_APP

    def sendMessage(self, chatId, text):
        return requests.post(self.ApiUrl+self.token+'/sendMessage',
                             data={'chat_id': chatId, 'text': text})

    def sendKeyboard(self, chatId, keyboard):
        return requests.post(self.ApiUrl+self.token+'/sendMessage',
                             data={'chat_id': chatId, 'text': '/OPCIONES', 'reply_markup': json.dumps(keyboard)})
