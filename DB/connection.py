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
                print("Error trying to connect: {a}".format(ex))

    def BuyAssets(self, asset):
        if self.connection.is_connected():
            try:
                cursor = self.connection.cursor()
                query = "INSERT INTO assets (Ticker, Quantity) VALUES ('{0}', '{1}')"
                cursor.execute(query.format(asset[0], asset[1]))
                self.connection.commit()
                print("¡Asset(s) purchased! \n")
            except Error as ex:
                print("Error trying to connect: {a}".format(ex))

    def deleteAsset(self, TickerDelete):
        if self.connection.is_connected():
            try:
                cursor = self.connection.cursor()
                query = "DELETE FROM assets WHERE Ticker = '{0}' LIMIT 1"
                cursor.execute(query.format(TickerDelete))
                self.connection.commit()
                print("¡Asset(s) deleted! \n")
            except Error as ex:
                print("Error trying to connect: {a}".format(ex)) 