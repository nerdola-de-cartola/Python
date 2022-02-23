from abc import ABCMeta, abstractclassmethod


class Conta(metaclass=ABCMeta):
    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def deposita(self, valor):
        self._saldo += valor
    
    # O metodo abstrato faz com que um erro seja lançado sempre que instanciarmos uma classe filha sem o metodo "passaMes"
    # Se não usarmos isso o erro só será lançado quando tentarmos usar o metodo que não existe
    @abstractclassmethod
    def passaMes():
        pass

    def __str__(self):
        return f"[>>Codigo {self._codigo} Saldo {self._saldo}<<]"

class ContaCorrente(Conta):
    def passaMes(self):
        self._saldo -= 2

class ContaPoupança(Conta):
    def passaMes(self):
        self._saldo *= 1.01
        self._saldo -= 3

class ContaInvestimentos(Conta):
    pass

contas = [
    ContaCorrente(500),
    ContaPoupança(501),
    ContaInvestimentos(502)
]

for conta in contas:
    conta.deposita(1000)
    print(conta)
    conta.passaMes()
    print(conta)

