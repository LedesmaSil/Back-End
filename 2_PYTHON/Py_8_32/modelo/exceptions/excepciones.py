
#print('Fin del programa');

resultado = 0;

while True:
    try:
        num2 = int(input('Ingrese un numero: '));
        num1 = 3;
        resultado = num1/num2
        print('El resultadon de tu numero dividido {} es de {}'.format(num2,resultado));
    except:
        print('Hubo un error, vuelva a intentar');
    else:
        print('Calculo exitoso!');
        break;
    finally:
        print('Yo me voy a mostrar siempre');


resultado+=1;
print(resultado);
print('POST TRY/EXCEPT')
