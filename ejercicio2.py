class vehiculo: #clase mas abstrata
     #este es el constructor de la clase
     def __init__(self,marca,modelo,anio):
         self.marca = marca
         self.modelo = modelo
         self.anio = anio
         print("vehiculo Creado")

     def encender(self):
         print("Estoy listo para llevarte")

     def arrancar(self): #definiendo otro overrriden
         print("boom boomm")

class autmovil(vehiculo): #Herencia simple: Automovil extiende a vehiculo
    __galonesGasolina = 0
    transmisionManual = True
    __kmt = 0
    def encender(self): #ejemplo de polimorfismo-overriding
        print("listo para llevarte en este",self.modelo)
        
    def arrancar(self):
        print(self.modelo,"rahhhhh rahh!!")#overriding 2

    def tocarCorneta(self):
        print("beep beep")
    
    def echarGasolina(self,vGalones): #encapsulamiento - eso es getter
        if vGalones <= 1:
            print("con un solo galon, no llegas a ninguna parte")
        elif vGalones <= 5:
            print("Advertencia se esta quedando sin gasolina")
        else:
            self.__galonesGasolina = vGalones

    def cuantaGasolinaHay(self): #encapsulamiento- esto es setter
        print("ud. tiene: ",self.__galonesGasolina,"galones de gasolina")

    def kilometraje(self,km): #Getter 2
      if km==0:
          print("Este carro es nuevo")
      else:
         self.__kmt =km
    def cuantoKilometrajeHay(self):#Setter 2
        print("el carro tiene",self.__kmt,"kilometraje")

class vehiculo2(vehiculo):
    pass
#instanciando la clase Vehiculo-Automovil
micarro = autmovil("chevrolett", "aveo", "2015")
micarro.encender()
micarro.tocarCorneta()
micarro.echarGasolina(100)
micarro.cuantaGasolinaHay()

#instanciamos el segundo vehiculo
vehiculo2 = autmovil("Ford", "Fiesta", "2010")
vehiculo2.encender()
vehiculo2.tocarCorneta()
vehiculo2.echarGasolina(4)
vehiculo2.cuantaGasolinaHay()
vehiculo2.arrancar()
vehiculo2.kilometraje(0)
vehiculo2.cuantoKilometrajeHay()