import Coneccion
class database:
    con = Coneccion.coneccion()
    c = con.Cursor()
    db = con.Abrir()

    def __init__(self):
        pass

    def setInsertar_nombre(self, name):
        sql = "INSERT INTO jugadores ( nickname ) VALUES ('"+(name)+"')"
        self.c.execute(sql)
        self.db.commit()
        self.c.close()
        self.db.close()

    def setInsertar_palabras(self, palabra):
        sql = "INSERT INTO palabras (palabra) VALUES ('"+palabra+"')"
        self.c.execute(sql)
        self.db.commit()
        self.c.close()
        self.db.close()

    def getPalabras(self):
        sql = 'select * from palabras'
        self.c.execute(sql)
        self.c.fetchall()
        return self.c

    def getHistorial(self):
        sql = "select nickname, puntos, status from jugadores inner join partidas p on jugadores.nickname = p.jugador_id"
        self.c.execute(sql)
        self.c.fetchall()
        return self.c