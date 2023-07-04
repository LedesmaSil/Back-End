
class Supermercado:
    def __init__(self, productos =[]):
        self.productos = productos
    
    def agregarProducto(self,producto):
        self.productos.append(producto)