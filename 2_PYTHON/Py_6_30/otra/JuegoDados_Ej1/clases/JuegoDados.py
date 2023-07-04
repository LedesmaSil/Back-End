from clases.Dado import Dado

class JuegoDados:

    def __init__(self):
        self.dado1 = Dado()
        self.dado2 = Dado()
        self.dado3 = Dado()

    def jugar(self):
        self.dado1.tirar()
        self.dado2.tirar()
        self.dado3.tirar()
        print(self.dado1, self.dado2, self.dado3)

        self.obtenerRdo()

    def obtenerRdo(self):
        if self.dado1.lado == self.dado2.lado and self.dado2.lado == self.dado3.lado:
            print("Gano")
        else:
            print("Perdio")