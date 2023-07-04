import random

class Dado:

    def __init__(self):
        self.lado = random.randint(1,6)

    def __str__(self):
        return "{}".format(self.lado)
    
    def tirar(self):
        self.lado = random.randint(1,6)

"""d = Dado()
print(d.lado)
d.tirar()
print(d.lado)"""