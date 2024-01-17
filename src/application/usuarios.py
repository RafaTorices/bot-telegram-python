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

    def guardarUsuario(self, chatId, first_name, username):
        self.cursor = self.conexion.cursor()
        self.sql = "INSERT INTO usuarios (chatId, first_name, username) VALUES ( %s, %s, %s)"
        datosUsuario = (chatId, first_name, username)
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
        self.sql = "SELECT CONCAT (id, '-', chatid, '-',first_name, '-', username) AS usuario FROM usuarios ORDER BY id DESC"
        self.cursor.execute(self.sql)
        self.resultado = self.cursor.fetchall()
        listadoUsuarios = list()
        listadoUsuarios = list()
        for row in self.resultado:
            usuario = row[0]
            listadoUsuarios.append(usuario)
        usuarios = '\n'.join(listadoUsuarios)
        return usuarios

    def listadoUsuariosWeb(self):
        self.cursor = self.conexion.cursor()
        self.sql = "SELECT id, chatid, first_name, username, autorizado, pendiente FROM usuarios ORDER BY id DESC"
        self.cursor.execute(self.sql)
        self.resultado = self.cursor.fetchall()
        return self.resultado

    def chatIdUsuarios(self):
        self.cursor = self.conexion.cursor()
        self.sql = "SELECT chatid FROM usuarios WHERE id = 14"
        self.cursor.execute(self.sql)
        self.resultado = self.cursor.fetchall()
        return self.resultado

    def activarUsuarioWeb(self, id):
        self.cursor = self.conexion.cursor()
        self.sql = "UPDATE usuarios SET autorizado = 1, pendiente = 0 WHERE id = "+id
        self.cursor.execute(self.sql)
        self.conexion.commit()

    def desactivarUsuarioWeb(self, id):
        self.cursor = self.conexion.cursor()
        self.sql = "UPDATE usuarios SET autorizado = 0, pendiente = 1 WHERE id = "+id
        self.cursor.execute(self.sql)
        self.conexion.commit()

    def listadoUsuariosPendientes(self):
        self.cursor = self.conexion.cursor()
        self.sql = "SELECT CONCAT (id, '-', chatid, '-',first_name, '-', username) AS usuario FROM usuarios WHERE pendiente = 1 ORDER BY id DESC"
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
        self.sql = "SELECT CONCAT (id, '-', chatid, '-',first_name, '-', username) AS usuario FROM usuarios WHERE autorizado = 1 ORDER BY id DESC"
        self.cursor.execute(self.sql)
        self.resultado = self.cursor.fetchall()
        listadoUsuarios = list()
        listadoUsuarios = list()
        for row in self.resultado:
            usuario = row[0]
            listadoUsuarios.append(usuario)
        usuarios = '\n'.join(listadoUsuarios)
        return usuarios

    def guardarMensajeUsuario(self, chatId, first_name, text, username):
        self.cursor = self.conexion.cursor()
        self.sql = "INSERT INTO mensajes (chatId, first_name, mensaje, username) VALUES ( %s, %s, %s, %s)"
        datosMensaje = (chatId, first_name, text, username)
        self.cursor.execute(self.sql, datosMensaje)
        self.conexion.commit()
        
    def listadoMensajesWeb(self):
        self.cursor = self.conexion.cursor()
        self.sql = "SELECT updated, first_name, username, mensaje FROM mensajes ORDER BY updated DESC LIMIT 100"
        self.cursor.execute(self.sql)
        self.resultado = self.cursor.fetchall()
        return self.resultado