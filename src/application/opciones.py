import pymysql
from application.mysql import MySQL
from application.config import TelegramConfig


class Opciones():

    def __init__(self):
        mysql = MySQL()
        self.conexion = pymysql.connect(host=mysql.host,
                                        user=mysql.user,
                                        password=mysql.password,
                                        database=mysql.db)

    def enviarOpciones(self):
        self.cursor = self.conexion.cursor()
        self.sql = "SELECT opcion FROM opciones"
        self.cursor.execute(self.sql)
        self.resultado = self.cursor.fetchall()
        # opciones = [["1", "2", "3", "4"]]
        keyboard = {
            "keyboard": self.resultado,
            "one_time_keyboard": True,
            "remove_keyboard": True,
            "resize_keyboard": True,
        }
        return keyboard

    def enviarOpcionesWeb(self):
        self.cursor = self.conexion.cursor()
        self.sql = "SELECT id, opcion, texto FROM opciones"
        self.cursor.execute(self.sql)
        self.resultado = self.cursor.fetchall()
        return self.resultado

    # def enviarOpcionesSolicitud(self, chatId, first_name):
    #     opciones = [["ACTIVAR_"+first_name +
    #                  "("+chatId+")", "CANCELAR_"+first_name+"("+chatId+")"]]
    #     keyboard = {
    #         "keyboard": opciones,
    #         "one_time_keyboard": True,
    #         "remove_keyboard": True,
    #         "resize_keyboard": True,
    #     }
    #     return keyboard
