class rectangulo:
    # constructor de la clase.  Se ejecuta
    # cuando la instanciamos
    def __init__(self, altura, ancho):
        print("Instanciando esta clase")

        # Atributos
        self.altura = altura
        self.ancho = ancho

        # Metodos
    def muestraElAncho(self):
        print("el ancho del rectangulo es:", self.ancho)

    def muestraLaAltura(self):
        print("la altura del rectangulo es:", self.altura)

    def calculaLaSuperficie(self, altura, ancho):
        vResult = 0 
        # aqui va el codigo de la nueva
        # asignacion que me van a entregar
        vResult = altura*ancho
        vResult = print("la superficie del rectangulo es: ",vResult,"m2")
        return vResult

# class triangulo:
class triangulo:
#     # constructor
   def __init__(self,base,altura):
#     # atributos
     self.base = base
     self.altura = altura
#     # metodos
   def mostrarLaBase(self):
       print("la base del triangulo es: ",self.base)

   def mostrarLaAltura(self):
       print("la altura del triangulo es: ",self.altura)
     
   def calcularLasuperficiedelTriangulo(self,base,altura):
       xResultado = (base*altura)/2
       print("la superficie del triangulo es: ",xResultado)

triangulo1 = triangulo(12, 3)
triangulo1.mostrarLaBase()
triangulo1.mostrarLaAltura()
triangulo1.calcularLasuperficiedelTriangulo(12, 3)

triangulo2 = triangulo(4,9)
triangulo2.mostrarLaBase()
triangulo2.mostrarLaAltura()
triangulo2.calcularLasuperficiedelTriangulo(4, 9)

# vamos a instanciar la clase rectangulo
# tantas veces como rectangulos necesitemos
rectangulo1 = rectangulo(12, 3)
rectangulo1.muestraElAncho()
rectangulo1.muestraLaAltura()
rectangulo1.calculaLaSuperficie(12, 3)

# vamos a instanciar el
# segundo rectangulo
rectangulo2 = rectangulo(4, 9)
rectangulo2.muestraLaAltura()
rectangulo2.muestraElAncho()
rectangulo2.calculaLaSuperficie(4, 9)