class Retangulo:
    def __init__(self, altura, largura):
        self.__altura = altura
        self.__largura = largura
        self.__area = altura * largura

    def area(self):
        print(f"A area do retangulo é igual a {self.__area}")
        return self.__area
