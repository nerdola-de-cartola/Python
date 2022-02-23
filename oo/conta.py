class Conta:
    def __init__(self, numero, titular, saldo, limite):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    @property
    def numero(self):
        return self.__numero

    @property
    def titular(self):
        return self.__titular

    @property
    def saldo(self):
        return self.__saldo

    @property
    def limite(self):
        return self.__limite

    @saldo.setter
    def saldo(self, valor):
        print(f"atualizando saldo {valor}")
        self.__saldo = valor

    @limite.setter
    def limite(self, valor):
        self.__limite = valor

    @staticmethod
    def codigoBanco():
        return "001"

    @staticmethod
    def codigosBancos():
        return {
            "BB": "001",
            "Caixa": "104",
            "Bradesco": "237"
        }

    def __podeSacar(self, valor):
        if valor <= (self.saldo + self.limite):
            return True
        else:
            return False

    def saca(self, valor):
        if self.__podeSacar(valor):
            self.saldo -= valor
            print("Saque realizado")
        else:
            print("O valor do saque passou o limite permitido")

    def deposita(self, valor):
        self.__saldo += valor

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)

    def extrato(self):
        print(
            f"A conta {self.numero} do titular {self.titular} possui R${self.saldo} de saldo e R${self.limite} de limite")
