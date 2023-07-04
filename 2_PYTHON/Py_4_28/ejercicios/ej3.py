 """
Pedirle al usuario que ingrese 3 valores y devolver el mayor de ellos. 
"""
def ingresarYEvaluarMayorTresNums():
    num1 = int(input('Ingrese el primer numero: '))
    num2 = int(input('Ingrese el segundo numero: '))
    num3 = int(input('Ingrese el tercer numero: '))

    '''mayor = num1

    if num2 > num3 and num2 > mayor:
        mayor = num2
    elif num3 > mayor:
        mayor = num3

    print(mayor)'''
    return calcularMayorEntreTres(num1,num2,num3)

def calcularMayorEntreTres(num1,num2,num3):
    lista = [num1, num2, num3]
    '''lista.sort()
    return lista[len(lista)-1] o -1'''
    return max

#PP
print(ingresarYEvaluarMayorTresNums())