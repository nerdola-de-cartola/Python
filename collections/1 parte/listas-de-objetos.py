class ContaCorrente:
    def __init__(self, codigo):
        self.codigo = codigo
        self.saldo = 0

    def deposita(self, valor):
        self.saldo += valor
    
    def __str__(self):
        return f"[>>Codigo {self.codigo} Saldo {self.saldo}<<]"

conta_do_matheus = ContaCorrente(500)
conta_do_joao = ContaCorrente(1000)
contas = [conta_do_matheus, conta_do_joao]

print(conta_do_matheus)
print(conta_do_joao)
