import Coneccion
import os
class database:
 try:
    con = Coneccion.coneccion()
    c = con.Cursor()
    db = con.Abrir()

    def __init__(self):
        pass

    def setInsertar_nombre(self, name):
        sql = "INSERT INTO jugadores ( nickname ) VALUES ('"+(name)+"')"
        self.c.execute(sql)
        self.db.commit()


    def setInsertar_palabras(self, palabra):
        sql = "INSERT INTO palabras (palabra) VALUES ('"+(palabra)+"')"
        self.c.execute(sql)
        self.db.commit()


    def getPalabras(self):
        lista = []
        sql = "select palabra from palabras"
        self.c.execute(sql)
        a = self.c.fetchall()
        if len(a) > 0:
            for i in a:
                lista.append(i[0])
        else:
            print(a)
        return lista

    def getHistorial(self):
        sql = "select nickname, puntos, status from jugadores inner join partidas p on jugadores.nickname = p.jugador_id"
        self.c.execute(sql)
        self.c.fetchall()
        return self.c

 except Exception:
      print("")
      os.system("cls")

