from clases.Producto import Producto

class Libro(Producto):
    MIN_STOCK = 5
    PORC_AUMENTO = 10

    def __init__(self,codigo,nombre,precio,stock, autor,anio):
        self.autor = autor
        self.anio = anio
        Producto.__init__(self,codigo,nombre,precio,stock)

    def aumentarPrecio(self):
        self.precio *= ((Libro.PORC_AUMENTO / 100) +1)

    def reponerStock(self):
        reponer = False

        if self.stock <= Libro.MIN_STOCK:
            reponer = True
        
        return reponer


class Alimento(Producto):
    PORC_AUMENTO = 25
    MIN_STOCK = 15

    def __init__(self,codigo,nombre,precio,stock, proveedor, fecha):
        super().__init__(codigo,nombre,precio,stock)
        self.proveedor = proveedor
        self.fecha = fecha

    def aumentarPrecio(self):
        self.precio *= ((Alimento.PORC_AUMENTO / 100) +1)

    def reponerStock(self):
        reponer = False
        if self.stock <= Alimento.MIN_STOCK:
            reponer = True
        
        return reponer
    
