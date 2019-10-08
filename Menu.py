import juego, os
obj_juego = juego.play()

class men:

    def Opciones(self, opc):
       cont = 1
       while cont == 1:
        if opc == 1:
            obj_juego.Agregar_palabra()
        if opc == 2:
            obj_juego.Iniciar_juego()
        if opc == 3:
            cont = -1
        if opc == 4:
            obj_juego.Resetear()
            # obj_juego.Salir()
        if opc == 5:
            obj_juego.Hibernar()