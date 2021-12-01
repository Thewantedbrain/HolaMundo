from abc import (ABC, abstractmethod)
from pythonlangutil.overload import Overload, signature


class Vehiculo(ABC):  # clase mas abstracta
    # este es el constructor de la clase
    def __init__(self, marca, modelo, anio):
        self.marca = marca
        self. modelo = modelo
        self.anio = anio
        print("Vehiculo Creado")

    @abstractmethod
    def encender(self):
        print("Estoy listo para llevarte")


class Automovil(Vehiculo):  # herencia simple: Automovil extiende a Vehiculo
    __galonesGasolina = 0
    transmisionManual = True

    # def encender(self):  # ejemplo de Polimorfismo - overriding
    #     print("Listo para llevarte en este", self.modelo)

    def encender(self, modo=None):
        if modo is None:
            print("Listo para llevarte en este", self.modelo)
        elif modo == "Ignicion":
            print("Listo para llevarte en este",
                  self.modelo, "en modo Electrico")
        elif modo == "Inducción":
            print("Listo para llevarte en este", self.modelo, " con Gasolina")

    # polimorfismo implementado desde modulos
    @Overload
    @signature()
    def arrancar(self):
        print("raaahh rahh!!")

    @arrancar.overload
    @signature("str")
    def arrancar(self, forma):
        print("raaahh rahh!!", forma)

    def tocarCorneta(self):
        print("beep beep!")

    def echarGasolina(self, vGalones):  # Encapsulamiento - esto es un setter
        if vGalones <= 1:
            print("con un solo galon, no llegas a ninguna parte")
        else:
            self.__galonesGasolina = vGalones

    def cuantaGasolinaHay(self):  # Encapsulamiento - esto es un getter
        print("Ud. tiene:", self.__galonesGasolina, "galones de Gasolina")


# instanciando la clase Vehiculo-Automovil
miCarro = Automovil("Chevrolet", "Aveo", "2015")
miCarro.encender()
miCarro.tocarCorneta()
miCarro.cuantaGasolinaHay()
miCarro.echarGasolina(100)
miCarro.cuantaGasolinaHay()
miCarro.arrancar('hello')

ElCarroDeKenyer = Automovil("Toyota", "Corolla", "2020")
ElCarroDeKenyer.encender("Ignicion")
ElCarroDeKenyer.arrancar()
ElCarroDeKenyer.arrancar("Retroceso")