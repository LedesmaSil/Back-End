n = float(input("Ingrese un número: "));
m = 1000
print("{}/{} = {}".format(n,m,m/n));

#Hecho por mi en vivo
while(True): # Lo segundo que agrego - para que se repita hasta que el try no devuelva un error.
    try:
        n = float(input("Ingrese un número: "))
        m = 1000
        print("{}/{} = {}".format(n,m,m/n))
        #break; Importante romper la iteración si todo ha salido bien
    except:
        print("Ha ocurrido un error, introduzca un número")
    else:
        print("Todo ha funcionado correctamente")
        break # Importante romper la iteración si todo ha salido bien
    finally:
        print("Fin de la iteración") # Siempre se ejecuta