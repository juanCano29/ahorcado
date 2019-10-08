import juego, sys
obj_juego = juego.play()

class men:

    def Opciones(self, opc):

        if opc == 1:
            obj_juego.Agregar_palabra()
        elif opc == 2:
            obj_juego.Iniciar_juego()
        elif opc == 3:
            obj_juego.Resetear()
        elif opc == 4:
            sys.exit()
            # obj_juego.Salir()
        elif opc == 5:
            obj_juego.Hibernar()