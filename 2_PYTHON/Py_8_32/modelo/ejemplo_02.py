print(type(1))
print(type(3.14))
print(type([]))
print(type(()))
print(type({}))

print(type(e).__name__)
print(type(1).__name__)
print(type(3.14).__name__)
print(type([]).__name__)
print(type(()).__name__)
print(type({}).__name__)


try:
    n = float(input("Ingrese un número divisor: "))
    5/n
except TypeError:
    print("No se puede dividir el número entre una cadena")
except ValueError:
    print("Debes introducir una cadena que sea un número")
except ZeroDivisionError:
    print("No se puede dividir por cero, prueba otro número")
except Exception as e: # Agregar esto yo después del segundo ejemplo
    print("Ha ocurrido un error no previsto", type(e).__name__)

#Caso 2 para obtener error - HACERLO YO 
try:
   # En el input no convertimos la cadena a número!
   n = input("Ingrese un número: ") 
   5/n
# Guardamos la excepción en la variable e
except Exception as e: 
   print("Ha ocurrido un error =>", type(e).__name__)

print(type(e))
