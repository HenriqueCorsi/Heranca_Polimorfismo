# Superclass
class Catalogo:
    def __init__(self, nome, ano):  # Atributos privados da superclass
        self._nome = nome
        self._ano = ano
        self._likes = 0

    # Property -> Basicamente tem a mesma função de um gett
    @property
    def nome(self):
        return self._nome

    @property
    def ano(self):
        return self._nome

    @property
    def likes(self):
        return self._likes

    # Método/Função para dar like
    def add_likes(self):
        self._likes = self.likes + 1

    # Método/Função que faz a representação textual dos parametros do objeto
    def __str__(self):
        return f'\nNome: {self._nome}\nAno: {self._ano}\nLikes: {self._likes}'


# Subclass
class Filmes(Catalogo):
    def __init__(self, nome, ano, tempo_duracao):  # Definindo os atributos da subclass
        super().__init__(nome, ano)  # Chamando os atributos da superclass
        self._tempo_duracao = tempo_duracao  # Atributo 'exclusivo' dessa classe

    @property
    def tempo_duracao(self):
        return self.tempo_duracao

    # Método/Função que faz a representação textual dos parametros do objeto
    def __str__(self):
        return f'\nFilme: {self._nome}\nDuração: {self._tempo_duracao} min.\nAno: {self._ano}\nLikes: {self._likes}'


# Subclass
class Serie(Catalogo):
    def __init__(self, nome, ano, temporadas):  # Definindo os atributos da subclass
        super().__init__(nome, ano)  # Chamando os atributos da superclass
        self._temporadas = temporadas  # Atributo 'exclusivo' dessa classe

    @property
    def temporadas(self):
        return self.temporadas

    # Método/Função que faz a representação textual dos parametros do objeto
    def __str__(self):
        return f'\nSérie: {self._nome}\nTemporadas: {self._temporadas}\nAno: {self._ano}\nLikes: {self._likes}'


