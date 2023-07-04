
while True:
    try:
        num2= int(input('Ingrese un valor: '));
        num1 =3;
        print('El resultado de dividir su numero por {} da como rdo {}'.format(num2, num1/num2))
    except ZeroDivisionError:
        print('No puede ingresar el numero 0');
    except Exception as e:
        #print(type(e))
        print('Error: '+ type(e).__name__);
    else:
        print('Operacion exitosa')
        break;


"""
except TypeError:
        print('Debe ingresar un numero');

except ValueError:
        print('No puede ingresar letras');
"""
    