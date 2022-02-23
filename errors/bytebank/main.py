from pprint import pprint

class Cliente:
    def __init__(self, nome, cpf, profissao):
        self.nome =  nome
        self.cpf = cpf
        self. profissao = profissao
    

cliente = Cliente("Matheus", "123.456.789-12", "programador")
pprint(cliente.__dict__, width=40)

cliente.idade = 20
print(cliente.idade)
