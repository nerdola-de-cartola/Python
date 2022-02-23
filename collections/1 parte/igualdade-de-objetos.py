class ContaSalario:
    def __init__(self, codigo, saldo):
        self.codigo = codigo
        self.saldo = saldo

    def deposita(self, valor):
        self.saldo += valor
    
    def __str__(self):
        return f"[>>Codigo {self.codigo} Saldo {self.saldo}<<]"

conta1 = ContaSalario(1, 1000.0)
conta2 = ContaSalario(1, 1000.0)

print(conta1 == conta2) # False

class ContaCorrente:
    def __init__(self, codigo, saldo):
        self.codigo = codigo
        self.saldo = saldo

    def deposita(self, valor):
        self.saldo += valor
    
    def __str__(self):
        return f"[>>Codigo {self.codigo} Saldo {self.saldo}<<]"

    def __eq__(self, outro):
        if type(outro) != ContaCorrente:
            return False

        return self.codigo == outro.codigo

conta3 = ContaCorrente(1, 1000.0)
conta4 = ContaCorrente(1, 1000.0)

print(conta3 == conta4) # True
print(conta1 == conta3) # False, poque são de classes diferentes