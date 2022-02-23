class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self._ano = ano
        self._likes = 0

    @property
    def nome(self):
        return self._nome

    @property
    def ano(self):
        return self._ano

    @property
    def likes(self):
        return self._likes

    def darLike(self, quantidade):
        self._likes += quantidade

    def __str__(self):
        return f"{self.nome} - {self.ano} - {self.likes}"


class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self._duracao = duracao

    @property
    def duracao(self):
        return self._duracao

    def __str__(self):
        return f"{self.nome} - {self.ano} - {self.duracao} min - {self.likes}"


class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self._temporadas = temporadas

    @property
    def temporadas(self):
        return self._temporadas

    def novaTemporada(self):
        self._temporadas += 1

    def __str__(self):
        return f"{self.nome} - {self.ano} - {self.temporadas} temporadas - {self.likes}"


class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome
        self.programas = programas

    def __getitem__(self, item):
        return self.programas[item]

    def __len__(self):
        return len(self.programas)


vingadores = Filme("vingadores guerra infinita", 2018, 160)
vingadores.darLike(3)
avatar = Serie("Avatar o último mestre do ar", 2003, 3)
avatar.darLike(12)
star_wars = Filme("Star wars episódio V o imperio contra ataca", 1988, 180)
star_wars.darLike(200)
arcane = Serie("Arcane", 2021, 1)
arcane.darLike(5)

playlist_fim_de_semana = Playlist(
    "Fim de semana",
    [vingadores, avatar, star_wars, arcane]
)

print(f"Tamanho da playlist: {len(playlist_fim_de_semana)} filmes e series")

for programa in playlist_fim_de_semana:
    print(programa)
