import mysql.connector


class DAO():

    def __init__(self):
        try:
            self.connection=mysql.connector.connect()
        except: