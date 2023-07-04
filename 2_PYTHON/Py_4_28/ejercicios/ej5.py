"""
Confeccioná un programa al cual le pasan una lista de numeros y ejecute 3 funciones:
una que sume todos los valores y devuelva la suma, una que devuelva el mayor de los 
numero y la tercera que devuelva el menor numero de la lista.
"""

def sumarizar(lista):
    acum = lista[0]

    for i in range(1,len(lista)):
        acum += lista[i]

    return acum; 


def mayor(lista):
    mayor = lista[0]

    for i in range(len(lista)):
        if lista[i] > mayor:
            mayor = lista[i]

    '''mayor = 0

    for i in lista:
        if i > mayor:
            mayor = i'''

    return mayor;


def menor(lista):
    return min(lista);


#Bloque principal del programa
lista_valores = [10, 26, 23, 120, 94];
print("La lista completa es : {}".format(lista_valores));
print("La suma de todos su elementos es: {}".format(sumarizar(lista_valores)));
print("El mayor valor de la lista es: {}".format(mayor(lista_valores)));
elmenor = menor(lista_valores);
print("El menor valor de la lista es: {}".format(elmenor));
