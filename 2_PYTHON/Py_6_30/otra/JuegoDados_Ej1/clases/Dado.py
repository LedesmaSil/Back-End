import random as ran

class Dado:

    def __init__(self):
        self.lado = ran.randint(1,6)
    
    def __str__(self):
        return "{}".format(self.lado)
    
    def tirar(self):
        self.lado = ran.randint(1,6)