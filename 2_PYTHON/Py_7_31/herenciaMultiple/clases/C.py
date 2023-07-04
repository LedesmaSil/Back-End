from clases.A import A;
from clases.B import B;


class C(B,A):
    def __init__(self):
        print("Soy de la clase C");


    def c(self):
        print("Este método es de C");
