def imprimeSeparador():
    N = 20
    for count in range(N):
        print("*", end="")
    print("")

def imprimeInicio(message):
    imprimeSeparador()
    print(message)
    imprimeSeparador()
    print()