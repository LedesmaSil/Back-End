
try:
    n = float(input("Ingrese un número divisor: "))
    5/n
except TypeError: #Valido tipo de dato, si me ingresan texto
    print("No se puede dividir el número entre una cadena")
except ValueError: # !!!!! 
    print("Debes introducir una cadena que sea un número")
except ZeroDivisionError: #Valido que no me ingresen 0
    print("No se puede dividir por cero, prueba otro número")


    