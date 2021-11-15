class forma:
    #construtor de la clase. se ejecuta
    #cuando la instanciamos
    def __init__(self,tipofigura,area):
        print("instanciamos esta clase")
        #atributos
        self.figura = tipofigura
        self.area = area
        #metodos

class rectangulo(forma):
    def __init__(self, tipofigura,area):
        super().__init__(tipofigura,area)
        print("el tipo de figura es: ",self.figura,"y su formula para calcular area es: ",self.area)

class cuadrado(forma):
    def __init__(self, tipofigura,area):
     super().__init__(tipofigura,area)
     print("la figura es: ",self.figura,"y su formula para calcular area es: ",self.area)
class triangulo(forma):
     def __init__(self, tipofigura,area):
         super().__init__(tipofigura,area)
         print("la figura es: ",self.figura,"y su formula para calcular area es: ",self.area)
class circulo(forma):
    def __init__(self, tipofigura,area):
        super().__init__(tipofigura,area)
        print("la figura es:  ",self.figura,"y su formula para calcular area es: ",self.area)
recta1=rectangulo('rectangulo','base*altura')
cual=cuadrado('cuadrado','lado**2')
tria=triangulo('triangulo','(base*altuta)/2')
cir=circulo('circulo','pi*r**2')
