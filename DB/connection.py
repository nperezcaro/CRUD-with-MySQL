import mysql.connector
from mysql.connector import Error


class DAO():

    def __init__(self):
        try:
            self.connection=mysql.connector.connect(
                host = "localhost", 
                user = "root", 
                passwd = "notarealpassword", 
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

    def SellAssets(self, asset):
        if self.connection.is_connected():
            try:
                cursor = self.connection.cursor()
                query_1 = "SET @sell = {0};".format(asset[1])
                query_2 = "SET @Quantity_0 = (SELECT Quantity FROM assets WHERE Ticker = '{0}');".format(asset[0])
                query_3 = "UPDATE assets SET Quantity = @Quantity_0 - @sell WHERE Ticker = '{0}' LIMIT 1;".format(asset[0])

                cursor.execute(query_1)
                cursor.execute(query_2)
                cursor.execute(query_3)

                self.connection.commit()

                print("¡Asset(s) sold! \n")
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

    def BuyExistingAssets(self, asset):
        if self.connection.is_connected():
            try:
                cursor = self.connection.cursor()
                query_1 = "Set @buy = {0};".format(asset[1])
                query_2 = "SET @Quantity_0 = (SELECT Quantity from assets WHERE Ticker = '{0}');".format(asset[0])
                query_3 = "UPDATE assets SET Quantity = @Quantity_0 + @buy WHERE Ticker = '{0}' LIMIT 1;".format(asset[0])

                cursor.execute(query_1)
                cursor.execute(query_2)
                cursor.execute(query_3)

                self.connection.commit()

                print("¡Asset(s) purchased! \n")
            except Error as ex:
                print("Error trying to connect: {a}".format(ex))