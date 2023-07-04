
class Alumno:

    def __init__(self, nombreCompleto, dni):
        self.nombreCompleto = (nombreCompleto)
        self.dni = (dni) #Llama al setter
        self.notaFinal = 0
    
    def definirNota(self, nota):
        self.notaFinal = nota

    @property
    def dni(self): #Getter
        print("Pasando por el getter")
        return self.__dni

    @dni.setter
    def dni(self, dni):
        #Aca van las validaciones
        print("Pasando por el setter")
        self.__dni = dni
    
    @property
    def nombreCompleto(self): #Getter
        return self.__nombreCompleto

    @nombreCompleto.setter
    def nombreCompleto(self, nombreCompleto):
        self.__nombreCompleto = nombreCompleto
    
    @property
    def notaFinal(self): #Getter
        return self.__notaFinal

    @notaFinal.setter
    def notaFinal(self, notaFinal):
        #Validar que sea entre 1 y 0
        self.__notaFinal = notaFinal

    def __str__(self):
        return "{} - Dni: {}".format(self.nombreCompleto, self.__dni)
    

a = Alumno('Sofia G.', '33554566')
print(a.dni)
#a.dni = "aaaaaaaa"