import pymysql
from application.mysql import MySQL
from application.config import TelegramConfig


class Usuario():

    def __init__(self):
        mysql = MySQL()
        self.conexion = pymysql.connect(host=mysql.host,
                                        user=mysql.user,
                                        password=mysql.password,
                                        database=mysql.db)
        config = TelegramConfig()
        self.chatIdSoporte = config.CHAT_ID_SOPORTE

    def comprobarUsuario(self, chatId):
        self.cursor = self.conexion.cursor()
        self.sql = 'SELECT id FROM usuarios WHERE chatid = '+chatId
        self.cursor.execute(self.sql)
        self.resultado = self.cursor.fetchall()
        rows = len(self.resultado)
        return rows

    def guardarUsuario(self, chatId, first_name):
        self.cursor = self.conexion.cursor()
        self.sql = "INSERT INTO usuarios (chatId, first_name) VALUES ( %s, %s)"
        datosUsuario = (chatId, first_name)
        self.cursor.execute(self.sql, datosUsuario)
        self.conexion.commit()

    def comprobarUsuarioAutorizado(self, chatId):
        self.cursor = self.conexion.cursor()
        self.sql = 'SELECT id FROM usuarios WHERE chatid = '+chatId+' and autorizado = 1'
        self.cursor.execute(self.sql)
        self.resultado = self.cursor.fetchall()
        rows = len(self.resultado)
        return rows

    def solicitudUsuario(self, chatId):
        self.cursor = self.conexion.cursor()
        self.sql = "UPDATE usuarios SET pendiente = 1 WHERE chatid = "+chatId
        self.cursor.execute(self.sql)
        self.conexion.commit()

    def comprobarSolicitudUsuario(self, chatId):
        self.cursor = self.conexion.cursor()
        self.sql = 'SELECT pendiente FROM usuarios WHERE chatid = '+chatId+' and pendiente = 1'
        self.cursor.execute(self.sql)
        self.resultado = self.cursor.fetchall()
        rows = len(self.resultado)
        return rows

    def listadoUsuarios(self):
        self.cursor = self.conexion.cursor()
        self.sql = "SELECT id, chatid, first_name FROM usuarios ORDER BY id DESC"
        self.cursor.execute(self.sql)
        self.resultado = self.cursor.fetchall()
        # listadoUsuarios = list()
        # listadoUsuarios = list()
        # for row in self.resultado:
        #     usuario = row[0]
        #     listadoUsuarios.append(usuario)
        # usuarios = '\n'.join(listadoUsuarios)
        return self.resultado

    def listadoUsuariosPendientes(self):
        self.cursor = self.conexion.cursor()
        self.sql = "SELECT CONCAT (id, '-', chatid, '-',first_name) AS usuario FROM usuarios WHERE pendiente = 1 ORDER BY id DESC"
        self.cursor.execute(self.sql)
        self.resultado = self.cursor.fetchall()
        listadoUsuarios = list()
        listadoUsuarios = list()
        for row in self.resultado:
            usuario = row[0]
            listadoUsuarios.append(usuario)
        usuarios = '\n'.join(listadoUsuarios)
        return usuarios

    def listadoUsuariosAutorizados(self):
        self.cursor = self.conexion.cursor()
        self.sql = "SELECT CONCAT (id, '-', chatid, '-',first_name) AS usuario FROM usuarios WHERE autorizado = 1 ORDER BY id DESC"
        self.cursor.execute(self.sql)
        self.resultado = self.cursor.fetchall()
        listadoUsuarios = list()
        listadoUsuarios = list()
        for row in self.resultado:
            usuario = row[0]
            listadoUsuarios.append(usuario)
        usuarios = '\n'.join(listadoUsuarios)
        return usuarios
