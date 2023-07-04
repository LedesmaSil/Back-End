'''
Un supermercado nos pide que le desarrollemos un sistema 
para controlar su stock. 
El supermercado tiene 3 tipos de productos: adornos, libros y
algunos alimentos.
De todos ellos sabemos su codigo, nombre y precio. De los libros 
tambien sabemos el año y el autor, mientras que de los alimentos
sabemos su proveedor y fecha de expiracion.

Todas las clases deben saber mostrar su codigo, aumentar su 
precio y decirnos si debemos o no reponer stock. 
Segun los acuerdos con los proveedores, todos aumentan sus precios cada 4 meces, aumentando
cada uno el monto pactado. 
El limite de stock para saber si se debe o no reponer el producto varia segun el tipo de producto.

1. Desarrollar el diagrama de clases correspondiente.

2. Desarrollar los metodos en codigo.
'''
from clases.Supermercado import *
from clases.Producto import Producto
from clases.Herencia import *

sup = Supermercado()
p = Libro("111dddd", 'Producto gral', 300, 5, "Borges", 2000)
alim = Alimento("111dddd", 'Alim gral', 500,60, "Prov. Borges", "01/08/2023")
sup.agregarProducto(p)
#p.mostrarCodigo()
print(p.precio)
p.aumentarPrecio()
print(p.precio)

print(p.reponerStock())

print(alim.reponerStock())
print(alim.precio)
alim.aumentarPrecio()
print(alim.precio)


