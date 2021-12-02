from abc import(ABC, abstractmethod)
import math
class figuras(ABC):
    #constructor
    def __init__(self,altura,base,radio,ladoA,LadoB,LadoC):
        print("Instanciando esta clase")
        self.ladoA = ladoA
        self.ladoB = LadoB
        self.ladoC = LadoC
        self.radio = radio
        self.altura = altura
        self.base = base
        self.__color = ""
        self.__vertices = ""
    #metodos
    
    def mostrarColor(self):
          print("El color de la figura es: ",self.__color)
       
    def asignarColor(self,color):
        self.__color = color
    
    def Mostrarvertices(self):
      vertices = self.__vertices
      if vertices > 0:
        print("El vertice de la figura es: ",self.__vertices)
      else: 
          print("No se aceptan valores negativos")
    def asignarVertices(self,vertices):
        self.__vertices = vertices
    @abstractmethod
    def calculararea(self):
        pass
    @abstractmethod
    def calcularperimetro(self):
        pass
class Circulos(figuras):
     def calculararea(self):
        s = math.pi*self.radio**2
        print("El area del circulo es: ",s)
     
     def calcularperimetro(self):
         l = 2*math.pi*self.radio
         print("El perimetro del circulo es: ",l)

class triangulos(figuras):
    def calculararea(self):
        s = (self.base * self.altura)/2
        print("El area del triangulo es: ",s)

    def calcularperimetro(self):
        l = self.ladoA+self.ladoB+self.ladoC
        print("El perimetro del triangulo es: ",l)


figura1 = Circulos(2, 2, 2, 2, 2, 2)
figura1.calculararea()
figura1.calcularperimetro()
figura1.asignarColor("azul")
figura1.mostrarColor()



figura2 = triangulos(2, 2, 2, 2, 2, 2)
figura2.calculararea()
figura2.calcularperimetro()
figura2.asignarColor("verde")
figura2.mostrarColor()
figura2.asignarVertices(3)
figura2.Mostrarvertices()