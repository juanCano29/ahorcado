import Menu, DataBase, os, time
db = DataBase
db.mydb.cursor()
name = input(str("Ingrese su nickname: "))
sql = "INSERT INTO jugadores ( nickname ) VALUES ('"+(name)+"')"
a = db.mycursor.execute(sql)
db.mydb.commit()
db.mydb.close()
time.sleep(1)
from time import sleep
obj_menu = Menu.men()
op = int(input(""" 
1) Agregar Palabra 
2) Iniciar Juego
3) Resetear
4) Salir
5) Hibernar
Opcion: """))

os.system("cls")
obj_menu.Opciones(op)




