from clases.Alumno import Alumno

class Institucion:
    MIN_PROMOCION = 7

    def __init__(self,nombre, lista=[]):
        self.nombre = (nombre)
        self.__alumnos = lista
        self.__promocionados = []

    def agregarAlumno(self, al):
        if type(al) is Alumno:
            self.__alumnos.append(al)
    
    def mostrarAlumnos(self):
        print("Listado de alumnos: ")
        for alumno in self.__alumnos:
            print(alumno)
    
    def definirNota(self,alumno, nota):
        if type(alumno) is Alumno:
            alumno.definirNota(nota)
            
            if nota > self.MIN_PROMOCION:
                self.__promocionados.append(alumno)
                self.__alumnos.remove(alumno)

    def definirNotaImaginaria(self,dni, nota):
        alumno = self.buscarAlumnosPorDni(dni)

        if alumno != None:
            alumno.definirNota(nota)

    def buscarAlumnosPorDni(self, dni):
        i = 0
        alumno = None

        while i < len(self.__alumnos) and alumno == None:
            if self.__alumnos[i].dni == dni:
                alumno = self.__alumnos[i]
            else:
                i+=1

        return alumno

    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self,nombre):
        self.__nombre = nombre
    
    @property
    def alumnos(self):
        return self.__alumnos