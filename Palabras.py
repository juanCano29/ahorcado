from random import shuffle
import os, time
class palabra:
    archivo_origen = []
    archivo_destino = []
    ao = ""
    ad = ""

    def __init__(self):
        self.archivo_origen = [line.rstrip() for line in open("Palabras.txt")]
        self.archivo_destino = [line.rstrip() for line in open("Guardado.txt")]
        self.ao = "Palabras.txt"
        self.ad = "Guardado.txt"

    def llenado_palabras(self):
        if len(self.archivo_origen) == 0:
             self.archivo_origen = self.archivo_destino
        shuffle(self.archivo_origen)

    def sobrescribir(self):
        ar = open(self.ao, "w")
        cadena = "\n".join(str(x) for x in self.archivo_origen)
        ar.write(cadena)
        ar.close()

    def Resetear(self):
        self.archivo_origen = self.archivo_destino
        shuffle(self.archivo_origen)
        arc = open(self.ao, "w")
        cad = "\n".join(str(i) for i in self.archivo_destino)
        arc.write(cad)
        arc.close()
        print("Palabras Restauradas")
        time.sleep(1)
        os.system("ahorcado.py")