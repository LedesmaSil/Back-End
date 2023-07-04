"""
CANTIDAD VARIABLE DE PARAMETROS
Confeccionar una función que reciba entre 2 y n valores enteros.
Se debe retornar la suma de todos los valores.
"""
# resto es una lista
def sumar(v1, v2, *restoNums): #Guarda los datos en tuplas
    sumatoria = v1 + v2

    for i in restoNums:
        sumatoria += i

    return sumatoria

# Bloque principal
print("La suma de 1+2: {}".format(sumar(1, 2)));
print("La suma de 1+2+4: {}".format(sumar(1,2,4)));
print("La suma de 1+2+3+4+5+6+7+8+9+10: {}".format(sumar(1, 2, 3,4,5,6,7, 8,9,10)));
