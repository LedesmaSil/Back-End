
class Alumno:

    def __init__(self, nombreCompleto, dni):
        self.nombreCompleto = (nombreCompleto) #Se ejecuta el setter
        self.dni = (dni) #Se ejecuta el setter
        self.notaFinal = 0
    
    @property
    def dni(self): #Getter
        #print("Pasando por Getter")
        return self.__dni
    
    @dni.setter
    def dni(self,dni):
        #ACA HAGO VALIDACIONES
        #print("Pasando por Setter")
        self.__dni = dni
    
    @property
    def nombreCompleto(self): #Getter
        return self.__nombreCompleto
    
    @nombreCompleto.setter
    def nombreCompleto(self, nombre):
        self.__nombreCompleto = nombre

    @property
    def notaFinal(self): #Getter
        return self.__notaFinal
    
    @notaFinal.setter
    def notaFinal(self, nota):
        self.__notaFinal = nota
    
    def __mostrarse(self): 
        print("")
    
    def __str__(self):
        return "{} - Dni: {}".format(self.nombreCompleto, self.__dni)

a = Alumno('Sofia G.', '33554566')
print(a.dni)
a.dni = "aaaaaaa"