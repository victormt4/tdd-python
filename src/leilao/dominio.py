from sys import float_info


class Usuario:

    def __init__(self, nome: str):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome


class Lance:

    def __init__(self, usuario: Usuario, valor: float):
        self.usuario = usuario
        self.valor = valor


class Leilao:

    def __init__(self, descricao: str):
        self.descricao = descricao
        self.__lances = []

    @property
    def lances(self):
        return self.__lances


class Avaliador:

    def __init__(self):
        self.maior_lance = float_info.min
        self.menor_lance = float_info.max

    def avalia(self, leilao: Leilao):

        for lance in leilao.lances:
            if lance.valor > self.maior_lance:
                self.maior_lance = lance.valor
            if lance.valor < self.menor_lance:
                self.menor_lance = lance.valor
