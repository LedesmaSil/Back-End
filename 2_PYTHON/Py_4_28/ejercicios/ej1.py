"""
Confeccionar una app que le de la bienvenida al usuario y le pida que ingrese dos 
valores y devuelva su suma. Al finalizar debe despedir al usuario.
"""

def sumarDosNums():
    num1 = int(input("Ingrese un numero: "))
    num2 = int(input("Ingrese un numero: "))
    print(num1 + num2)
    return num1 + num2

def mostrarPorConsola(texto):
    print(texto)

'''def despedir():
    print("Chau")'''

#PP
mostrarPorConsola("Bienvenida")
rdo = sumarDosNums()
mostrarPorConsola('Chau')

sumarDosNums()