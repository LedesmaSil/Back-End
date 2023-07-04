class Vehiculo:
    cantVehiculos = 0
    id = 0
    cantMotos = 0

    def __init__(self, patente, marca, anio, color, tipo):
        self.tipo = tipo
        self.patente = patente
        self.marca = marca
        self.anio = anio
        self.color = color
        self.velActual = 0
        Vehiculo.cantVehiculos+=1
        Vehiculo.id +=1
        self.id = Vehiculo.id

        if tipo == 'moto' or tipo == 'Moto':
            Vehiculo.cantMotos+=1
    
    def acelerar(self, vel):
        self.velActual += vel
        print(self.velActual)

    def frenar(self):
        self.velActual = 0

    def __str__(self):
        return 'Pantente {} Marca {}'.format(self.patente, self.marca)
        
    def __del__(self):
        print('Borrdado vehiculo con patente {}'.format(self.patente))

auto1 = Vehiculo('asd 111', 'Fiat', 2008, 'Azul', 'auto')
auto2 = Vehiculo('asd 222', 'Fiat', 2008, 'Azul', 'auto')
auto1.acelerar(80)
auto1.frenar()
print(auto1.velActual)
print(Vehiculo.cantVehiculos)
print("IDS", auto1.id, auto2.id)
del auto1
#print(auto1)
print("IDS", auto2.id)
auto3 = Vehiculo('asd 333', 'Fiat', 2008, 'Azul', 'auto')
print("Hola")
auto4 = Vehiculo('asd 444', 'Fiat', 2008, 'Azul', 'auto')
print("Finalizacion del programa")
