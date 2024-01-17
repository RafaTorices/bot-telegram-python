import os
from dotenv import load_dotenv
# Parametros de configuracion del servicio

load_dotenv()


class TelegramConfig():
    APIURL = 'https://api.telegram.org/bot'
    TOKEN = os.getenv('TOKEN')
    TITULO_APP = os.getenv('TITULO_APP')
    TELEFONO_SOPORTE = os.getenv('TELEFONO_SOPORTE')
    CHAT_ID_SOPORTE = os.getenv('CHAT_ID_SOPORTE')
    EMAIL_SOPORTE = os.getenv('EMAIL_SOPORTE')

# Configuracion de MySQL


class MySQLConfig():
    DB_HOST = "172.17.0.3"
    DB_USER = "devops"
    DB_PASSWORD = "devops"
    DB_NAME = "devops"
    DB_PORT = 3306
