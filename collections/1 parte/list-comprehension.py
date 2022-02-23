IDADES = [16, 27, 30, 42]
idades = IDADES
print("Idades originais")
print(idades)
print()

idades = [idade for idade in IDADES if idade > 21]
print("Idades maiores que 21")
print(idades)
print()

def dobraIdade(num):
    return num*2
    
idades = [dobraIdade(idade) for idade in IDADES]
print("Novas idades usando funções")
print(idades)
print()
