import juego
obj_juego = juego.play()

class men:
    def Opciones(self, opc):
        if opc == 1:
            obj_juego.Agregar_palabra()
        if opc == 2:
            obj_juego.Iniciar_juego()
        if opc == 3:
            obj_juego.Salir()
        if opc == 4:
            obj_juego.Hibernar()