from paquetes.animales.super_animal import Animal as animal;
from paquetes.saludos.bienvenida import *;
from paquetes.saludos.despedir import *;
from paquetes.saludos.saludarConNombre import *;

perro1 = animal();
print(perro1);

bienvenida();
despedir();
saludarConNombre('Juana');
