import mysql.connector
class coneccion:

  mydb = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        passwd="",
        database="ahorcadodb"
    )

  def Abrir(self):
       return self.mydb

  def Cursor(self):
      cursor = self.mydb.cursor()
      return cursor
