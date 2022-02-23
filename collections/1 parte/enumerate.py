idades = [11, 43, 55, 41, 85, 43, 43, 5]

# Forma manual
for indice in range(len(idades)):
    print(indice, "|", idades[indice])

print()

# Forma com tuplas usando enumerate
for tupla in enumerate(idades):
    print(tupla)

print()

# Forma com desempacotamento de tuplas
for indice, idade in enumerate(idades):
    print(indice, "|", idade)

print()

# Forma com desempacotamento e ignorando posições
for indice, _ in enumerate(idades):
    print(indice)