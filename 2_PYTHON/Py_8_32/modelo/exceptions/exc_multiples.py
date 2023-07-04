"""while True:
    try:
        n = float(input("Ingrese un número divisor: "))
        5/n
    except TypeError: 
        print("No se puede dividir el número entre una cadena")
    except ValueError:  
        print("Debes introducir una cadena que sea un número")
    except Exception as e:
        print("Error " + type(e).__name__);
    else: 
        print('Su operacion fue exitosa');
        break;"""


while True:
    try:
        n = float(input("Ingrese un número divisor: "))
        5/n
    except ZeroDivisionError:
        print('ZERO ERROR');
    except Exception as e:
        print("Error " + type(e).__name__);
    
    else: 
        print('Su operacion fue exitosa');
        break;