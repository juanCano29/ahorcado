import os
import Menu
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




