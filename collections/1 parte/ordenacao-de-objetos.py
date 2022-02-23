from operator import attrgetter
from functools import total_ordering

@total_ordering # Cria todas as comparações baseado no __eq__ e no __lt__
class ContaCorrente:
    def __init__(self, codigo, saldo):
        self._codigo = codigo
        self._saldo = saldo

    def __str__(self):
        return f"[>>Codigo {self._codigo} Saldo {self._saldo}<<]"

    def __eq__(self, outro):
        if type(outro) != ContaCorrente:
            return False

        return self._codigo == outro._codigo

    def __lt__(self, outro):
        if self._codigo != outro._codigo:
            return self._codigo < outro._codigo

        elif self._saldo != outro._saldo:
            return self._saldo < outro._saldo

    def deposita(self, valor):
        self._saldo += valor


contas = [
    ContaCorrente(2, 500.00),
    ContaCorrente(1, 999.00),
    ContaCorrente(3, 1000.00),
    ContaCorrente(1, 100.00)
]

print("Lista original")
for conta in contas:
    print(conta)

print()

print("Lista ordenada com função")
for conta in sorted(contas, key=lambda conta: conta._codigo):
    print(conta)    

print()

print("Lista ordenada com attrgetter")
for conta in sorted(contas, key=attrgetter("_codigo", "_saldo")):
    print(conta)

print()

print("Lista ordenada com critério do próprio objeto")
for conta in sorted(contas):
    print(conta)   