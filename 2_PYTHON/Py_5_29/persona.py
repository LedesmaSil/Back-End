class Persona:
    LENGTH_MIN_DNI = 8
    
    def __init__(self, dniRecibido,nombre, apellido, edad, ocupado=True):
        self.setDni(dniRecibido)
        self.dni = dniRecibido
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.ocupado = ocupado

    def setDni(self,dniRecibido):
        if len(dniRecibido) < Persona.LENGTH_MIN_DNI:
            self.dni = 0
        else:
            self.dni = dniRecibido

    def desocuparse(self):
        self.ocupado = False
    
    def realizarActividad(self):
        pudoAsignarseTarea = False
        if not self.ocupado:
            self.ocupado = True
            pudoAsignarseTarea = True
        else:
            print("El usuario ya esa ocupado")
        
        return pudoAsignarseTarea

    def presentarse(self):
        print('Hola, mi nombre es {}'.format(self.nombre + " " + self.apellido))
    #ToString
    def __str__(self):
        return 'Dni: {}, Nombre: {}, Apellido: {}, Edad:{}'.format(self.dni, self.nombre, self.apellido, self.edad)

p1 = Persona("1111111", 'Denise', 'Eichenblat', 50)
print(p1.ocupado)
p2 = Persona('222222222', 'Walter', 'Ustaris', 25)
print(p2)
p2.presentarse()
p3 = Persona("1111111", 'Denise', 'Eichenblat', 50, False)
print(p3.ocupado)
p3.realizarActividad()
p3.realizarActividad()
print(p3.ocupado)