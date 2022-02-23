class Conta:
    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def deposita(self, valor):
        self._saldo += valor
    
    def __str__(self):
        return f"[>>Codigo {self._codigo} Saldo {self._saldo}<<]"

class ContaCorrente(Conta):
    def passaMes(self):
        self._saldo -= 2

class ContaPoupança(Conta):
    def passaMes(self):
        self._saldo *= 1.01
        self._saldo -= 3

conta_do_matheus = ContaCorrente(500)
conta_do_joao = ContaPoupança(501)
conta_do_matheus.deposita(1000)
conta_do_joao.deposita(1000)
print(conta_do_matheus)
print(conta_do_joao)

conta_do_matheus.passaMes()
conta_do_joao.passaMes()
print(conta_do_matheus)
print(conta_do_joao)