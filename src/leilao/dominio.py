from sys import float_info
from copy import deepcopy
from typing import List


class Usuario:

    def __init__(self, nome: str, saldo: float):
        self.__nome = nome
        self.__saldo = saldo

    @property
    def nome(self):
        return self.__nome

    @property
    def saldo(self):
        return self.__saldo

    def propor_lance(self, leilao, valor: float):
        leilao.propor_lance(Lance(self, valor))
        self.__saldo -= valor


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

        if len(self.__lances) == 0 or (
                self.__lances[-1].usuario != lance.usuario and lance.valor > self.__lances[-1].valor):
            if lance.valor > self.maior_lance:
                self.maior_lance = lance.valor
            if lance.valor < self.menor_lance:
                self.menor_lance = lance.valor

            self.__lances.append(lance)

        else:
            raise ValueError('Erro ao propor lance')

    @property
    def lances(self):
        return deepcopy(self.__lances)
