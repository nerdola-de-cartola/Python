from collections import defaultdict, Counter


def contaPalavras(texto):
    dicionario = {}

    for palavra in texto.split():
        repeticoes = dicionario.get(palavra, 0)
        dicionario[palavra] = repeticoes + 1

    return dicionario

def contaPalavrasDefault(texto):
    dicionario = defaultdict(int)

    for palavra in texto.split():
        dicionario[palavra] += 1

    return dicionario
    

def contaPalabraCounter(texto):
    return Counter(texto.split())

texto = "Queria mostrar agora para nós o poder de conhecermos a API e as coleções que uma linguagem nos oferece Então repara eu comentei aqui o defaultdict e eu estou utilizando ele com números inteiros e o meu código ainda está mais ou menos Vamos pegar esse mesmo código e tentar simplificar mais ainda"

texto = texto.lower()

dicionario_proprio = contaPalavras(texto)
dicionario_padrao = contaPalavrasDefault(texto)
dicionario_contador = contaPalabraCounter(texto)
print(dicionario_proprio)
print(dicionario_padrao)
print(dicionario_contador)



