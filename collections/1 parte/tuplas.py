def deposita(conta, valor):
    return (conta[0], conta[1] + valor)

contas = [
    ("matheus", 100),
    ("gabriel", 85)
]

contas[0] = deposita(contas[0], 900)

print(contas)
