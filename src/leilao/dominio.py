from sys import float_info
from copy import deepcopy
from typing import List


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
        self.__lances: List[Lance] = []
        self.maior_lance = float_info.min
        self.menor_lance = float_info.max

    def propor_lance(self, lance: Lance):

        if len(self.__lances) == 0 or (self.__lances[-1].usuario != lance.usuario and lance.valor > self.__lances[-1].valor):
            if lance.valor > self.maior_lance:
                self.maior_lance = lance.valor
            if lance.valor < self.menor_lance:
                self.menor_lance = lance.valor

            self.__lances.append(lance)

        else:
            raise ValueError('O mesmo usuário nao pode propor dois lances seguidos')

    @property
    def lances(self):
        return deepcopy(self.__lances)
