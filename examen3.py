class cuentas:
    def __init__(self,saldo,anadirsaldo,restarSaldo):
       self.__capitalInicial = 0
       self.__Tasa = 0
       self.__Tiempo = 0
       self.saldo = saldo
       self.anadirsaldo = anadirsaldo
       self.restarSaldo = restarSaldo
       self.saldofinal = self.saldo + self.anadirsaldo
    #Metodos

    def consultarSaldo(self): #getter
        print('Su saldo es de: ',self.saldo)

    def depositarSaldo(self):
        saldoagregado = self.anadirsaldo + self.saldo
        saldo = saldoagregado
        print('se ha añadido un monto a su saldo ahora tiene un saldo de: ',saldo)
    
    def retirarSaldo(self):
        retirar = self.saldofinal - self.restarSaldo
        print('Acaba de hacer un retiro ahora su saldo es de: ',retirar)

    def abonarInteres(self,capitalInicial,tasa,tiempo):#setter
        self.__capitalInicial = capitalInicial
        self.__Tasa = tasa
        self.__tiempo = tiempo
        sacar = self.__capitalInicial*0.10
        interesapagar = self.__capitalInicial *self.__Tasa*self.__Tiempo
        total = sacar + interesapagar
        print('Su intreses simple son de: ',total)
class cuentasDeAhorro(cuentas):
        pass
class cuentasPlazoFijo(cuentas):
    def abonarInteres(self, capitalInicial, tasa, tiempo): #overriding
        self.__capitalInicial = capitalInicial
        self.__Tasa = tasa
        self.__tiempo = tiempo
        if self.__capitalInicial<0 and self.__Tasa<0 and self.__tiempo<0:
            print('No se aceptan valores negativos')
        else:
            print('sus valores son positivo y se aceptan')

cuenta = cuentasDeAhorro(100,10,1)
cuenta.abonarInteres(2, 2, 2)
cuenta.depositarSaldo()
cuenta.retirarSaldo()

cuenta1 = cuentasPlazoFijo(2, 2, 2)
cuenta1.abonarInteres(2, 2, 2)