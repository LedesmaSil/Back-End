# Comentario de linea 
"""
Comentario de bloque
"""

texto = 'Soy una cadena de texto' #str
print(type(texto))
enteros = 1 #int
decimales = 0.22 #float
print(type(decimales))
IVA = 0.21
booleanos = True #bool

nombre = None
print(type(nombre))
char = 'M'
print(type(char))

#edad = int(input('Ingresame tu edad: '))
#edad = int(edad)
#print("La edad del usuario es de " + str(edad))

'''num1 = int(input("Ingresame el primer numero de la suma: "))
num2 = float(input("Ingresame el segundo numero de la suma: "))
rdo = num1 + num2
print("La suma entre", str(num1) + " y " + str(num2) + " da como rdo " + str(rdo))'''


num1 = 10
num2 = 20
num3 = '30'
num4 = '40'
print(num1 + num2)
print(num3 + num4)
print(num1 + int(num4))

texto = 'Bienvenido a la comision 23003'
print('230038' in texto)

edad = 10

if edad >= 18:
    print("Es mayor de edad")
    print("print 2")
    print("HOLAAA")

'''nota = int(input("Ingrese la nota: "))
if nota >= 7 and nota <= 10:
    print("Puede promocionar la materia")
elif nota >= 4 and nota < 7:
    print("Esta aprobado")
elif nota >=1 and nota < 4:
    print("No esta aprobado")
else:
    print("La nota ingresada es incorrecta")'''


'''cantAlumnos = int(input("Ingrese la cantidad de alumnos: "))
contador = 0
acumNotas = 0

while contador < cantAlumnos:
    nota = int(input("Ingrese la nota: "))
    acumNotas += nota  # acumNotas = acumNotas + nota
    contador+=1

promedio = 0

if contador != 0:
    promedio = acumNotas / contador'''
    

    
secret_word = "python"
counter = 7

'''while True:
    print("Dentro del primer while");

    while True:
        word = input("Enter the secret word: ").lower()
        counter = counter + 1
        if word == secret_word:
            break
        if word != secret_word and counter > 7: 
            break
    
    break;'''

print("Tabla del 3")
for i in range(0,11,-1):
    print(i * 3)
