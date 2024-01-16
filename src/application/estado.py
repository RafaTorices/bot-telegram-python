# Clase para estado del sistema
import pymysql
from application.mysql import MySQL


class Estado():
    def __init__(self):
        mysql = MySQL()
        self.conexion = pymysql.connect(host=mysql.host,
                                        user=mysql.user,
                                        password=mysql.password,
                                        database=mysql.db)

    def comprobarEstado(self):
        self.cursor = self.conexion.cursor()
        self.sql = 'SELECT estado FROM estado WHERE id = 1'
        self.cursor.execute(self.sql)
        self.resultado = self.cursor.fetchall()
        for row in self.resultado:
            estado = row[0]
            return estado

    def comprobarEstadoWeb(self):
        self.cursor = self.conexion.cursor()
        self.sql = 'SELECT estado FROM estado WHERE id = 1'
        self.cursor.execute(self.sql)
        self.resultado = self.cursor.fetchall()
        for row in self.resultado:
            estado = row[0]
            return estado

    def obtenerNotasEstado(self):
        self.cursor = self.conexion.cursor()
        self.sql = 'SELECT notas FROM estado WHERE id = 1'
        self.cursor.execute(self.sql)
        self.resultado = self.cursor.fetchall()
        for row in self.resultado:
            notas = row[0]
            return notas

    def actualizarNotasEstado(self, notas):
        self.cursor = self.conexion.cursor()
        self.sql = 'UPDATE estado SET notas = "'+notas+'" WHERE id = 1'
        self.cursor.execute(self.sql)
        self.conexion.commit()

    def activarEstado(self):
        self.cursor = self.conexion.cursor()
        self.sql = 'UPDATE estado SET estado = 1 WHERE id = 1'
        self.cursor.execute(self.sql)
        self.conexion.commit()

    def desactivarEstado(self):
        self.cursor = self.conexion.cursor()
        self.sql = 'UPDATE estado SET estado = 0 WHERE id = 1'
        self.cursor.execute(self.sql)
        self.conexion.commit()
