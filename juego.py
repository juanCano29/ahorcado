import re, os, time
import Palabras, DataBase
from random import shuffle

class play:
    obj_palabras = Palabras.palabra()

    def Agregar_palabra(self):

        opc = input("Desea agregar una palabra s/n: ")
        while opc.lower() == "s":
            try:
                db = DataBase.database()
                palabra = input(str("ingrese una palabra: "))
                db.setInsertar_palabras(palabra)
                os.system("cls")
                if ((not (re.fullmatch(r"[A-Za-z ]{1,50}", palabra)))):
                    print("max car. {1,15}, solo caracteres.")

                opc = input("Desea agregar una palabra s/n: ")
                os.system("cls")
            except Exception:
                os.system("cls")
                print("Error al insertar en la base de datos")
                time.sleep(2)
                os.system("cls")
                pal = input("ingrese una palabra: ")
                os.system("cls")
                if ((not (re.fullmatch(r"[A-Za-z ]{1,50}", pal)))):
                    print("max car. {1,15}, solo caracteres.")
                else:
                    arch = open(self.obj_palabras.ad, "a")
                    arch.writelines(pal + "\n")
                    arch.close()
                    arch_2 = open(self.obj_palabras.ao, "a")
                    arch_2.writelines(pal + "\n")
                    arch_2.close()
                    opc = input("Desea agregar una palabra s/n: ")
                    os.system("cls")
        if opc.lower() == "n":
            os.system("ahorcado.py")

    def Iniciar_juego(self):

        ahorcado = [
            '''
              _________________________________________________
              ************************************************|
              ************************************************|                            
              ************************************************|
              ************************************************|
              ************************************************|
              ************************************************O
              ***********************************************/|\ 
              ***********************************************/ \ 
                                                                   ''',
            '''
               _________________________________________________
               ************************************************|
               ************************************************|
               ************************************************|
               ************************************************|
               ************************************************|
               ************************************************O
               ***********************************************/|\ 
               ***********************************************/     ''',
            '''
              _________________________________________________
              ************************************************|
              ************************************************|
              ************************************************|
              ************************************************|
              ************************************************|
              ************************************************O
              ***********************************************/|\ 
                                    ''',
            '''
              _________________________________________________
              ************************************************|
              ************************************************|
              ************************************************|
              ************************************************|
              ************************************************|
              ************************************************O
              ***********************************************/|  
                                                           ''',

            ''' 
               _________________________________________________
               ************************************************|
               ************************************************|
               ************************************************|
               ************************************************|
               ************************************************|
               ************************************************O
               *********************************************** | 
                                                     ''',
            """
               _________________________________________________
               ************************************************|
               ************************************************|
               ************************************************|
               ************************************************|
               ************************************************|
               ************************************************O 
                                                    """
        ]

        try:
            lista_mostrar = []
            palabrasbd = self.obj_palabras.archivo_origenbd
            shuffle(palabrasbd)
            Palabra_obtenidadb = palabrasbd.pop()
            pase = True
            intentos = 5
            opc = input("Desea Iniciar s/n: ")
            os.system("cls")
            while opc.lower() == "s":
                pl = list(Palabra_obtenidadb)
                palab = ''.join(pl)
                for item in pl:
                    lista_mostrar.append('_')
                while pase:
                    print(' '.join(lista_mostrar))
                    letra = input("Ingresa letra: ")
                    os.system("cls")

                    while (not (re.fullmatch(r"[A-Za-z]{1}", letra))):
                        os.system("cls")
                        print("max car. {1}, solo letras.")
                        letra = input("Ingresa letra: ")

                    if letra not in pl:
                        intentos = intentos - 1
                        print('Has fallado!!!! Te quedan ' + str(intentos) + ' intentos')
                        input()
                    print(ahorcado[intentos])

                    for i, valor in enumerate(pl):
                        if valor == letra:
                            lista_mostrar[i] = valor

                    if intentos <= 0:
                        pase = False
                        print('Has perdido, la palabra '
                              'era ' + palab)
                        time.sleep(1)
                        print("GAME OVER")
                        time.sleep(1)
                        print("Cargando...")
                        time.sleep(1)
                        os.system("ahorcado.py")

                    elif pl == lista_mostrar:
                        pase = False
                        print("Felicidades Has Ganado")
                        print('la palabra '
                              'era ' + palab)
                        time.sleep(1)
                        print("GAME OVER")
                        time.sleep(1)
                        print("Cargando...")
                        os.system("cls")
                        time.sleep(1)
                        os.system("ahorcado.py")
        except Exception:
            print("Conexion Fallida a la base de datos")
            lista_mostrar = []
            self.obj_palabras.llenado_palabras()
            Palabra_obtenida = self.obj_palabras.archivo_origen.pop()
            self.obj_palabras.sobrescribir()
            pase = True
            intentos = 5
            opc = input("Desea Iniciar s/n: ")
            os.system("cls")
            while opc.lower() == "s" and len(self.obj_palabras.archivo_origen) > 0:
                pl = list(Palabra_obtenida)
                palab = ''.join(pl)
                for item in pl:
                    lista_mostrar.append('_')
                while pase:
                    print(' '.join(lista_mostrar))
                    letra = input("Ingresa letra: ")
                    os.system("cls")

                    while (not (re.fullmatch(r"[A-Za-z]{1}", letra))):
                        os.system("cls")
                        print("max car. {1}, solo letras.")
                        letra = input("Ingresa letra: ")

                    if letra not in pl:
                        intentos = intentos - 1
                        print('Has fallado!!!! Te quedan ' + str(intentos) + ' intentos')
                        input()
                    print(ahorcado[intentos])


                    for i, valor in enumerate(pl):
                        if valor == letra:
                            lista_mostrar[i] = valor

                    if intentos <= 0:
                        pase = False
                        print('Has perdido, la palabra '
                              'era ' + palab)
                        time.sleep(1)
                        print("GAME OVER")
                        time.sleep(1)
                        print("Cargando...")
                        time.sleep(1)
                        os.system("ahorcado.py")

                    elif pl == lista_mostrar:
                        pase = False
                        print("Felicidades Has Ganado")
                        print('la palabra '
                              'era ' + palab)
                        time.sleep(1)
                        print("GAME OVER")
                        time.sleep(1)
                        print("Cargando...")
                        os.system("cls")
                        time.sleep(1)
                        os.system("ahorcado.py")



        if opc.lower() == "n":
            os.system("ahorcado.py")

    # def Salir(self):
    #     sys.exit()
    def Resetear(self):
        self.obj_palabras.Resetear()

    def Hibernar(self):
        os.system("shutdown /h")