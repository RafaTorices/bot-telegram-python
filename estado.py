# Clase para estado del sistema
from mysql import MySQL


class Estado():
    def __init__(self):
        mysql = MySQL()
        self.conexion = mysql.conexion

    def comprobarEstado(self):
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
