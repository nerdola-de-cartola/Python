import adivinhacao
import forca
from helpers import imprimeInicio

def escolherJogo():
    imprimeInicio("Escolha seu jogo!")
    print("(1) Forca (2) Adivinhação")
    jogo = int(input("Qual jogo você deseja jogar? ").strip())
    print()

    if jogo == 1:
        forca.jogar()
    elif jogo == 2:
        adivinhacao.jogar()

if __name__ == "__main__":
    escolherJogo()