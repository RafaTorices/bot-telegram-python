import os
from dotenv import load_dotenv
# Parametros de configuracion del servicio

load_dotenv()


class TelegramConfig():
    URL_WEBHOOK = os.getenv('URL_WEBHOOK')
    APIURL = 'https://api.telegram.org/bot'
    TOKEN = os.getenv('TOKEN')
    TITULO_APP = os.getenv('TITULO_APP')+"\n\n"
    TELEFONO_SOPORTE = os.getenv('TELEFONO_SOPORTE')
    CHAT_ID_SOPORTE = os.getenv('CHAT_ID_SOPORTE')
    EMAIL_SOPORTE = os.getenv('EMAIL_SOPORTE')

# Configuracion de MySQL


class MySQLConfig():
    DB_HOST = os.getenv('MYSQL_HOST')
    DB_USER = os.getenv('MYSQL_USER')
    DB_PASSWORD = os.getenv('MYSQL_PASSWORD')
    DB_NAME = os.getenv('MYSQL_DATABASE')
    DB_PORT = os.getenv('MYSQL_PORT')
