from clases.Alumno import Alumno

class Institucion:

    def __init__(self,nombre, listado=[]):
        self.nombre = (nombre)
        self.__alumnos = listado

    def agregarAlumno(self, alumno):
        if type(alumno) is Alumno:
            self.__alumnos.append(alumno)
        else:
            print("No se puedo agregar, debe pasar un Alumno")

    def mostrarAlumnos(self):
        print("Listado de los alumnos")
        for alumno in self.__alumnos:
            print(alumno)

    def definirNota(self, alumno, nota):
        if type(alumno) is Alumno:
            alumno.guardarNota(nota)

    def buscarPersonaPorDni(self, dni):
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
    

    def __str__(self):
        return "self.__nombre"