import mysql.connector
from mysql.connector import Error


class DAO():

    def __init__(self):
        try:
            self.connection=mysql.connector.connect(
                host = "localhost", 
                user = "root", 
                passwd = "Tobby2019", 
                database = "portfolio"
                )
        except Error as ex:
            print("Error al intentar la conexión: {a}".format(ex))

    def ShowAssets(self):
        if self.connection.is_connected():
            try:
                cursor = self.connection.cursor()
                cursor.execute("SELECT * FROM assets")
                results = cursor.fetchall()
                return results
            except Error as ex:
                print("Error al intentar la conexión: {a}".format(ex))