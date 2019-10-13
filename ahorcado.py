import Menu, DataBase, os, time
db = DataBase.database()
name = input(str("Ingrese su nickname: "))
db.setInsertar_nombre(name)
time.sleep(1)
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




