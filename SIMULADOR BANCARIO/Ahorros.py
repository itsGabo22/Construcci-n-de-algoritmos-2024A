__autor__ = "Gabriel Esteban Paz Guerrero"
__license__ = "GPL"
__version__ = "1.0.0"
__email__ = "gabriel.pazg@campusucc.edu.com"

class CuentaAhorros: 
    # Aquí inicia mi clase
    
    """#--------------------------------------------------------------------------------------
    # Atributos
    --------------------------------------------------------------------------------------#"""

    __Saldo = 0
    __Interes = "0.6%"

    
    """#-------------------------------------------------------------------------------------------------
    # Métodos
    -------------------------------------------------------------------------------------------------#"""
    
    __method__="DarSaldo"
    __params__= "Ninguno"
    __returns__="Saldo"
    __descriptions__="Este metodo retorna el saldo de la cuenta"
    def DarSaldo(self):
        #Aqui inicia el metodo
        return self.__Saldo
    
    __method__="RetirarValor"
    __params__= "monto"
    __returns__="nada"
    __descriptions__="Este metodo permite retirar un monto a la cuenta"
    def RetirarValor(self, monto):
        #aqui empieza mi método
        self.__Saldo=self.__Saldo - monto
    
    __method__="ConsignarAhorro"
    __params__= "monto"
    __returns__="nada"
    __descriptions__="Este metodo permite consignar un ahorro a la cuenta"
    def ConsignarAhorro(self, monto):
        #aqui empieza mi método
        self.__Saldo=self.__Saldo + monto

    __method__="RetirarSaldo"
    __params__= "SaldoTotal"
    __returns__="nada"
    __descriptions__="Este metodo permite retirar todo el saldo de la cuenta"
    def RetirarSaldo(self, saldoTotal):
        #aqui empieza mi método
        self.DarSaldo()
        self.__Saldo=self.__Saldo - self.__Saldo(saldoTotal)
    