from random import randrange
from helpers import imprimeInicio

def jogar():
    imprimeInicio("Bem vindo ao jogo da adivinhação!")

    MAX = 100
    MIN = 1
    NUMERO_SECRETO = randrange(MIN, MAX+1)
    pontos = 100

    print("Qual o nível de dificuldade você deseja?")
    print("(1) Fácil (2) Médio (3) Difícil")
    dificuldade = int(input("Nível : "))
    
    if dificuldade==1:
        CHANCES = 7
    elif dificuldade == 2:
        CHANCES = 5
    else:
        CHANCES = 3

    for rodada in range(1, CHANCES+1):
        print(f"Rodada {rodada} de {CHANCES}")

        chute = int(input(f"Digite o seu número entre {MIN} e {MAX}: "))
        if chute < MIN or chute > MAX:
            print(f"Você deve digitar um número entre {MIN} e {MAX}")
            continue

        acertou = (chute == NUMERO_SECRETO)
        maior = (chute > NUMERO_SECRETO)
        menor = (chute < NUMERO_SECRETO)

        print()

        if acertou:
            print("Você acertou")
            print(f"E fez {pontos} pontos!")
            break
        else:
            pontos -= abs(NUMERO_SECRETO-chute)
            print("Você errou")
            if maior:
                print("O seu chute foi maior que o número secreto")
            elif menor:
                print("O seu chute foi menor que o número secreto")

        print()

    print(f"O número secreto era {NUMERO_SECRETO}", end="\n\n")
    print("Fim do jogo")


if __name__ == "__main__":
    jogar()