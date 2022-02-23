idades = [11, 43, 55, 41, 85, 43, 43, 5]
print("Idades originais: ",idades)

print("Idades ordenadas: ", sorted(idades))
print("Idades ordenadas ao contrário: ", sorted(idades, reverse=True))
print("Idades de trás pra frente: ", list(reversed(idades)))

idades.sort()
print("Idades alteradas com sort: ",idades)
