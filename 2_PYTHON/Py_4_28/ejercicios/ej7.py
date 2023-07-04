"""
PASANDO PARAMETROS DESORDENADOS.
Realizar un programa que permita calcular el sueldo de una persona. La persona debe
ingresar su nombre, la cantidad de horas trabajadas y el valor de su hora de trabajo.
"""
def calcular_sueldo(nombre, valor_hora, cantidad_horas ):
    sueldo = cantidad_horas*valor_hora;
    print(f"{nombre} trabajo {cantidad_horas} horas y cobra un sueldo de ${sueldo}")

#Programa principal
calcular_sueldo("Juan",100, 120)
calcular_sueldo(valor_hora=100, nombre="Juan", cantidad_horas=40)
