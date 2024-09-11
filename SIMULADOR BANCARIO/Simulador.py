__autor__ = "Gabriel Esteban Paz Guerrero"
__license__ = "GPL"
__version__ = "1.0.0"
__email__ = "gabriel.pazg@campusucc.edu.com"

'''----------------------------------------------------------------
#Importaciones
----------------------------------------------------------------'''
from Ahorros import CuentaAhorros
from CDT import CDT
from Corriente import CuentaCorriente

class Simulador: 
    # Aquí inicia mi clase
    """#--------------------------------------------------------------------------------------
    # Atributos
    --------------------------------------------------------------------------------------#"""
    __Nombre = ""
    __Cedula = ""

    """#--------------------------------------------------------------------------------------
    # Dias, meses y años
    --------------------------------------------------------------------------------------#"""

    __mesActual = 0

    """#--------------------------------------------------------------------------------------
    # Asociaciones (cuentas)
    --------------------------------------------------------------------------------------#"""

    __CuentaCorriente = CuentaCorriente()
    __CDT = CDT()
    __CuentaAhorros = CuentaAhorros()

    """#---------------------------------------------------------------------------------------------------
    # Métodos
    ---------------------------------------------------------------------------------------------------#"""
    
    __method__="ConsignarCuentaCorriente"
    __params__="Monto"
    __returns__="nada"
    __descriptions__="Este metodo permite consignar un m onto a la cuenta corriente"
    def ConsignarCuentaCorriente(self, monto):
        # Aquí inicia mi metodo
        #self.__CuentaCorriente.Saldo=self.__CuentaCorriente.Saldo+monto #metodo no recomendado
        self.__CuentaCorriente.ConsignarValor(monto)
        
    __method__="CalcularSaldoTotal"
    __params__="Ninguno"
    __returns__="SaldoTotal"
    __descriptions__="Este metodo suma el saldo de todas las cuentas"
    def CalcularSaldoTotal(self):
        # Aquí inicia mi metodo
        total = self.__CuentaAhorros.DarSaldo() + self.__CuentaCorriente.DarSaldo()
        return total
    
    __method__="PasarAhorrosACorriente"
    __params__="Ninguno"
    __returns__="nada"
    __descriptions__="Este metodo transfiere el saldo de Ahorros a corriente"
    def PasarAhorrosACorriente (self):
        #aqui empieza mi método
        SaldoTemporal = self.__CuentaAhorros.DarSaldo()
        self.__CuentaAhorros.RetirarValor(SaldoTemporal)
        self.__CuentaCorriente.ConsignarValor(SaldoTemporal)
    
    __method__="Ahorrar"
    __params__="Monto"
    __returns__="Ninguno"
    __descriptions__="Permite ahorrar un monto de la cuenta corriente a la cuenta de ahorros"
    def Ahorrar(self, monto):
        #aqui empieza mi método
        self.__CuentaCorriente.RetirarValor(monto)
        self.__CuentaAhorros.ConsignarAhorro(monto)
        
    __method__="RetirarAhorro"
    __params__="monto"
    __returns__="Ninguno"
    __descriptions__="Permite retirar un monto de ahorro"
    def RetirarAhorro (self, monto):
        #aqui empieza mi método
        self.__CuentaAhorros.RetirarValor(monto)
    
    __method__="DarSaldoCorriente"
    __params__="ninguno"
    __returns__="Saldo de la cuenta corriente"
    __descriptions__="Retorna el saldo de la cuenta corriente"
    def DarSaldoCorriente (self):
        return self.__CuentaCorriente.DarSaldo()

    __method__="RetirarTodo"
    __params__="ninguno"
    __returns__="Nuevo Saldo"
    __descriptions__="Permite retirar todo el saldo de la cuenta de ahorros y cuenta corriente"

    def RetirarTodo (self):
        #aqui empieza mi método
        SaldoTotal = self.__CuentaAhorros.DarSaldo() + self.__CuentaCorriente.DarSaldo()
        self.__CuentaAhorros.RetirarSaldo(self.__CuentaAhorros.DarSaldo())
        self.__CuentaCorriente.RetirarSaldo(self.__CuentaCorriente.DarSaldo())
        return SaldoTotal
    
    __method__="DuplicarAhorro"
    __params__= "Ninguno"
    __returns__="Ahorros duplicados"
    __descriptions__="Este metodo permite duplicar los ahorros de la cuenta"
    def DuplicarAhorro(self):
        #aqui empieza mi método
        return self.__Saldo*2