class forma:
    #construtor de la clase. se ejecuta
    #cuando la instanciamos
    def __init__(self,tipofigura):
        print("instanciamos esta clase")
        #atributos
        self.figura = tipofigura
        #metodos

class rectangulo(forma):
    def __init__(self, tipofigura):
        super().__init__(tipofigura)
        print("el tipo de figura es: ",self.figura)

class cuadrado(forma):
    def __init__(self, tipofigura):
     super().__init__(tipofigura)
     print("la figura es: ",self.figura)
class triangulo(forma):
     def __init__(self, tipofigura):
         super().__init__(tipofigura)
         print("la figura es: ",self.figura)
class circulo(forma):
    def __init__(self, tipofigura):
        super().__init__(tipofigura)
        print("la figura es:  ",self.figura)
recta1=rectangulo('rectangulo')
cual=cuadrado('cuadrado')
tria=triangulo('triangulo')
cir=circulo('circulo')
