"""
PARAMETROS CON VALORES POR DEFECTO
Confeccionar una función que reciba un string como parámetro y de forma opcional un segundo
string con un caracter. La función debe mostrar el string subrayado con el caracter
que indica el segundo parámetro.
"""
def titulo_subrayado(titulo, caracter='-'):
    print(titulo);
    print(caracter*len(titulo))

#Programa principal
titulo_subrayado("Ventas", ".");
titulo_subrayado("Titulo2");

