import mysql.connector

mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    passwd="",
    database="ahorcadodb"
)
print(mydb)
mycursor = mydb.cursor()

# class Database:
#
#     def __init__(self):
#         pass
#
#     def InsertarNombre(self,name):
#         sql = "insert into jugadores (nickname) values (%name);"
#         nom = name
#         mycursor.execute(sql, nom)
#         mydb.commit()

