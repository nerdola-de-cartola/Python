from collections import Counter


texto = """
    Heron de Alexandria no século primeiro inventou teatros automatizados que usavam programação análoga para controlar os fantoches, portas, luzes e efeitos de som.

    A mais antiga programadora de computadores que se conhece é Ada Lovelace, filha de Anabella e de Lord Byron (o poeta). Ao serviço do matemático Charles Babbage, traduziu e expandiu uma descrição da sua máquina analítica. Muito embora Babbage nunca tenha completado a construção de nenhuma das suas máquinas, o trabalho que ele e Ada desenvolveram sobre elas, garantiu a Ada o título de primeira programadora de computadores do mundo (veja as notas de Ada Byron sobre a máquina analítica). A linguagem de programação Ada recebeu o seu nome em homenagem à Ada.

    Um dos primeiros programadores que se tem notícia de ter completado todos os passos para a computação sem auxílio, incluindo a compilação e o teste, é Wallace J. Eckert. O trabalho deste homem antecede a ascensão das linguagens de computador, porque ele usou a linguagem da matemática para solucionar problemas astronômicos. No entanto, todos os ingredientes estavam lá: ele trabalhou um laboratório de computação para a Universidade de Colúmbia com equipamentos fornecidos pela IBM, completos com uma divisão de serviço de atendimento ao cliente, e consultores de engenharia para propósitos especiais, na cidade de Nova York, na década de 1930, usando cartões perfurados para armazenar os resultados intermediários de seus cálculos, e então formatando os cartões perfurados para controlar a impressão das respostas, igual ao trabalho para os censos décadas antes. Tinha técnicas de debug tais como códigos de cores, bases cruzadas, verificação e duplicação. Uma diferença entre Eckert e os programadores dos dias de hoje é que o exemplo do seu trabalho influenciou o projeto Manhattan. Seu trabalho foi reconhecido por astrônomos do Observatório da Universidade de Yale, Observatório da Universidade de Princeton, Observatório da Marinha dos EUA, Observatório da Faculdade Harvard, Observatório dos estudantes da Universidade da Califórnia, Observatório Ladd da Universidade de Brown e Observatório Sproul da Faculdade de Swarthmore.

    Alan Turing é frequentemente encarado como o pai da ciência de computadores e, por afinidade, da programação. Ele foi responsável por ajudar na elaboração e programação de um computador destinado a quebrar o código alemão ENIGMA durante a Segunda Guerra Mundial — ver Máquina Enigma.
    Aprendizagem da Programação
    Wikilivros
    O Wikilivros tem um livro chamado Introdução à programação

    A aprendizagem da programação tem enfrentado vários desafios. Por ser de difícil aprendizagem, vários estudos propõe soluções para ajudar no processo de aprendizagem da programação, quer a nível do ensino secundário, quer universitário por diversas razões. De entre as soluções, destacam-se sistemas de apoio, uns que permitem que os estudantes visualizem de imediato o resultado do código que vão escrevendo, outros estudos também sugerem o uso de artefatos como a robótica para que os alunos interajam com algo tangível como o robot, melhorando a interação e motivando ao mesmo tempo. Foram realizados estudos que provam que o uso da gamificação em contextos de aprendizagem da programação, produziu resultados com sucesso, aumentando o nível de interação dos alunos, bem como a motivação para continuar a aprender.
"""

aparicoes = Counter(texto.lower())
total_de_caracteres = sum(aparicoes.values())

proporcoes = [(letra, repeticoes/total_de_caracteres) for letra, repeticoes in aparicoes.items()]
proporcoes = Counter(dict(proporcoes))
mais_comuns = proporcoes.most_common(10)

print(aparicoes)
print()
print(total_de_caracteres)
print()
print(proporcoes)
print()
print(mais_comuns)
