# Listas são passadas para funções por referencia
# Então elas podem ser alteradas dentro das funções
def imprimeLista(lista = []):
    print(lista)
    print(len(lista))
    lista.append(13)

idades = [16, 27, 30, 42]
print("Lista antes da função: ")
imprimeLista(idades)
print(f"Lista depois da função: {idades}")
print()

# Quando se usa uma lista como o valor padrão de uma função essa lista automatica é cacheada na memória para a próxima vez que a função for chamada
print("Lista padrão da função")
imprimeLista()
imprimeLista()
imprimeLista()
imprimeLista()
imprimeLista()
print()

# Para resolver esse problema devemos definir a função da seguinte forma
def novaImprimeLista(lista = None):
    if lista == None:
        lista = []

    print(lista)
    print(len(lista))
    lista.append(13)

print("Lista padrão da maneira correta")
imprimeLista()
imprimeLista()
imprimeLista()
imprimeLista()
imprimeLista()