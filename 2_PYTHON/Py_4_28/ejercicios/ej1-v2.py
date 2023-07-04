def mostrarPorConsola(mensaje):
    print(mensaje);
# Funciones del tipo void

def sumarDosNumeros():
    num1 = int(input("Ingresa un numero: "));
    num2 = int(input("Ingresa otro numero: "));
    suma = num1 + num2;
    print(f'La suma dio como resultado {suma}');

def aplicacion(bienvenida,despedida):
    mostrarPorConsola(bienvenida);
    sumarDosNumeros();
    mostrarPorConsola(despedida);

#PP
aplicacion('Bienvenida','Hasta la proxima!');




