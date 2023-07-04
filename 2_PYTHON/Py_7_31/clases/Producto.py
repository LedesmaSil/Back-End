from abc import ABC, abstractmethod
#ABC Abstract Base Classes

class Producto(ABC):

    def __init__(self,codigo,nombre,precio,stock):
        self.codigo = (codigo)
        self.nombre= (nombre)
        self.precio = (precio)
        self.stock = (stock)

    @abstractmethod
    def aumentarPrecio(self):
        pass

    @abstractmethod
    def reponerStock(self):
        pass

    def mostrarCodigo(self):
        print(self.__codigo)

    @property
    def precio(self):
        return self.__precio

    @precio.setter
    def precio(self,precio):
        if precio > 0:
            self.__precio = precio
    
    @property
    def stock(self):
        return self.__stock

    @stock.setter
    def stock(self,stock):
        if stock > 0:
            self.__stock = stock

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self,codigo):
        if len(codigo) > 0:
            self.__codigo = codigo
    
    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self,nombre):
        if len(nombre) > 0:
            self.__nombre = nombre
    
    def __str__(self):
        return "Codigo: {}".format(self.__codigo)