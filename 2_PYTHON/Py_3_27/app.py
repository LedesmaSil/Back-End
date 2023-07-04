estacion = 'verano'

#distintas formas de imprimir
print("Mi estacion favorita es: " + estacion)
print("Mi estacion favorita es: {}".format(estacion))
print(f"Mi estacion favorita es: {estacion}")

risa = 'JA'
risa = risa.lower() # pasa minusculas
print(risa*10) # cuanto se repite
print(risa.upper()*10) # mayusculas

if risa == 'ja':
    print('El string coincide')
else:
    print('El string NO coincide')

frase = 'Federico dijo: "xxxxx"'

#for letra in frase: #recorre en forma vertical
    #print(letra)

print(frase[1:len(frase)]) # len hasta el final

numeros = '12345678'
mensaje = 'Soy la profesora del curso, mi nombre es Denise'

print(mensaje.count('e')) #6
print(mensaje.index('S')) #posicion o un error
print(" ".join(numeros)) # espacio entre letras
print(mensaje.split(" ")) # 
print(mensaje.replace('a','x', 1)) # se reemplaza 1 vez a por x

nombre = 'Alejandra'
stringNums = 'Hola40'

print(nombre.isalpha()) #Bool True si hay solo letras
print(stringNums.isalpha()) 
print(numeros.isdigit()) #Bool True si hay solo numeros
print(stringNums.isdigit())
print(len(nombre))

titulo = '-------Caperucita roja--------'
titulo = titulo.capitalize() # minusculas todas
titulo = titulo.title() # mayscula las primeras
titulo = titulo.strip('-') # se saca lo q pides 
print(titulo)

#Listas
vacia = []
lista = [1,2,3]
print(lista[0]) # 1
num1, num2, num3 = lista; #pasa a variable la cantidad
print(num1) # 1
lista.append(4) # agrega la cantidad de elementos
lista.insert(0, -1)# se agrega el lugar y que cosa
lista.pop() #elimina el ultimo
eliminado = lista.pop(0)
lista.remove(2) # elimina el num 2
#print(eliminado) # veo el liminado
print(lista.index(1)) #en que posicion esta

lista.append(10)
lista.append(10)
lista.append(10)
lista.append(10)
print(lista)
print(lista.count(10)) #cuantas veces se repite el 10
#print(len(lista))

#1 form de mostrar
for i in lista:
    print(i)
print()
print("SEGUNDO FOR ")
print()
#2 form de mostrar
for i in range(len(lista)):
    print(lista[i])

matriz = [[1,2,3,4,5,6,], [2022, 2023]]
print(matriz[0][0])# posicion de posicion

# Tuplas - DATOS INMUTABLES
fecha = (2023,11,7)
#fecha = (2022, 10,2)
anio, mes, dia = fecha # si o si se desempaqueta en tupla
print(anio)

#Diccionarios - Dictionary
dic = {"Denise": "Docente de Codo a Codo", "Juaquin": "Contador"}
dic2 = {1: "Curso python", 2: "Curso JS"}
print(type(dic2))

for i in dic.keys(): # accede la forma
    print(dic[i])

for clave, valor in dic.items():
    print(clave, "trabaja como: " + valor)

#Conjuntos - Sets no rrepetirodos y desordenados
conj = {"Denise", "Joaquin", "Alejandra"}
nums = {1 , 30, 40, 22}
conj_vacio = {}
#conj2 = set(nums) # devuelve lo mismo desordenado
conj2 = nums.copy
# print(conj2) # devuelve la direc de memoria
nums.add(80) # agrega el num
print(nums)
print(type(nums)) # dice el tipo de conjunto












