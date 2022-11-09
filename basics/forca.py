from helpers import imprimeInicio
from random import randrange


def jogar():
    imprimeInicio("Bem vindo ao jogo da forca!")

    PALAVRA_SECRETA = palavraSecreta()
    TOTAL_CHANCES = 7
    dica = ["_" for letra in PALAVRA_SECRETA]
    enforcou = False
    acertou = False
    chances = 7

    print(f"Começando o jogo! a palavra é {dica}")

    while not enforcou and not acertou:
        chute = input("Qual seu chute? ").strip().upper()

        if chute in PALAVRA_SECRETA:
            chuteCorreto(chute, PALAVRA_SECRETA, dica)
        else:
            chances -= 1
            print(f"Ops, você errou! Faltam {chances} tentativas.")
            imprimeForca(TOTAL_CHANCES - chances)

        if not chances:
            enforcou = True
        elif "_" not in dica:
            acertou = True
        else:
            print(f"A palavra é {dica}")

    imprimeResultado(acertou, PALAVRA_SECRETA)


def imprimeResultado(ganhou, palavra_secreta):
    resultado = "Você ganhou" if ganhou else "Você se enforcou"
    print(f"Fim de jogo! {resultado}, a palavra era {palavra_secreta}")

    if ganhou:
        imprimeTrofeu()
    else:
        imprimeCaveira()


def palavraSecreta():
    with open("palavras.txt", "r") as arquivo:
        palavras = [palavra.strip().upper() for palavra in arquivo]
        random_index = randrange(0, len(palavras))
        return palavras[random_index]


def chuteCorreto(chute, palavra, dica):
    for index, letra in enumerate(palavra):
        if chute == letra:
            print(f"Encontrado a letra {letra} na posição {index + 1}")
            print()
            dica[index] = letra


def imprimeForca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


def imprimeTrofeu():
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def imprimeCaveira():
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


if __name__ == "__main__":
    jogar()
