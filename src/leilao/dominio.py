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
        if valor > self.__saldo:
            raise ValueError('Valor proposto maior que saldo disponível')

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
        self.maior_lance = 0.0
        self.menor_lance = 0.0

    def propor_lance(self, lance: Lance):

        if not self.__lances or self.__lances[-1].usuario != lance.usuario and lance.valor > self.__lances[-1].valor:
            if not self.__lances:
                self.menor_lance = lance.valor

            self.maior_lance = lance.valor

            self.__lances.append(lance)

        else:
            raise ValueError('Erro ao propor lance')

    @property
    def lances(self):
        return deepcopy(self.__lances)
