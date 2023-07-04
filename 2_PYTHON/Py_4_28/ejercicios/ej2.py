"""
Realizá un programa que pida 2 valores y deuelva su suma. Se debe realizar este proceso la
cantidad de veces que el usuario necesite. 
Cada cuenta debe separarse en consola mediante asteriscos para mayor claridad.
"""
def mostrarPorConsola(texto):
    print(texto)

def sumarDosNums():
    num1 = int(input("Ingrese un numero: "))
    num2 = int(input("Ingrese un numero: "))
    print(num1 + num2)
    return num1 + num2

def ejecutarFuncionNVeces(cantidad, cb):
    for i in range(cantidad):
        cb()
        mostrarPorConsola('******************')

#PP
veces = int(input('Cuantas veces desea sumar: '))
ejecutarFuncionNVeces(veces, sumarDosNums)
