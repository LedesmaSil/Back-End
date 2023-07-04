"""
Hacer un programa que le pida al usuario el lado de un cuadrado y calculo su perimetro o
su superficie según lo solicite el usuario;
"""
def mostrar_superficie(lado):
    superficie=lado*lado;
    print ("La superficie es: {}m2".format(superficie));

def mostrar_perimetro(lado):
    perimetro=lado*4;
    print("El perimetro del cuadrado es de {}m".format(perimetro));

def cargar_dato():
    respuesta = ''
    la = int(input("Ingrese el valor del lado de un cuadrado : "));

    while(respuesta != "perimetro" and respuesta !="superficie"):
        respuesta=input("Quiere calcular el perimetro o la superficie? ");
        respuesta= respuesta.lower();

    if respuesta=="perimetro":
        mostrar_perimetro(la);
    elif respuesta == "superficie":
        mostrar_superficie(la);


#Programa principal
cargar_dato();