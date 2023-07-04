
while True:
    try:
        num1 = int(input('Ingresa un numero: '));
        num2 = 3;
        resultado = num1/num2;
        print('Su numero divido {} da como resultado {}'.format(num2, resultado));  
    except:
        print('Hubo un error');
    else:
        print('Calculo exitoso!');
        break;
    finally:
        print('Sistema corriendo...');

print('Fin de la ejecucion');