import re, os, time
import Palabras
obj_palabras = Palabras.palabra()
class play:

    def Agregar_palabra(self):

        opc = input("Desea agregar una palabra s/n: ")
        while opc.lower() == "s":
            palabra = input("ingrese una palabra: ")
            os.system("cls")
            if ((not (re.fullmatch(r"[A-Za-z ]{1,50}", palabra)))):
                print("max car. {1,15}, solo caracteres.")
            else:
                arch = open(obj_palabras.ad, "a")
                arch.writelines(palabra + "\n")
                arch.close()
                arch_2 = open(obj_palabras.ao, "a")
                arch_2.writelines(palabra + "\n")
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


        lista_mostrar = []
        obj_palabras.llenado_palabras()
        Palabra_obtenida = obj_palabras.archivo_origen.pop()
        obj_palabras.sobrescribir()
        pase = True
        intentos = 5
        opc = input("Desea Iniciar s/n: ")
        os.system("cls")
        while opc.lower() == "s" and len(obj_palabras.archivo_origen) > 0:
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
        obj_palabras.Resetear()

    def Hibernar(self):
        os.system("shutdown /h")