class forma:
    #construtor de la clase. se ejecuta
    #cuando la instanciamos
    def __init__(self,altura,ancho):
        print("instanciamos esta clase")
        #atributos
        self.altura = altura
        self.ancho = ancho
        #metodos

class rectangulo(forma):
    def muestraElAncho(self):
        print("el ancho del rectangulo es: ",self.ancho)

    def muestraAltura(self):
        print("la altura del rectangulo es: ",self.altura)
class cuadrado(forma):
    def __init__(self, altura, ancho):
     super().__init__(altura,ancho)
     print("el ancho del cuadrado es: ",self.ancho)
class triangulo(forma):
     def __init__(self, altura, ancho):
         super().__init__(altura, ancho)
         print("la altura triangulo es: ",self.altura)
class circulo(forma):
    def __init__(self, altura, ancho):
        super().__init__(altura, ancho)
        print("el ancho ancho del circulo es: ",self.ancho)

cuadrado1=cuadrado(4, 4)
triangulo1=triangulo(4, 9)
circulo1=circulo(4, 9)
