from src.leilao.excecoes import LanceInvalido
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
        if not self.__valor_valido(valor):
            raise LanceInvalido('Valor proposto maior que saldo disponível')

        leilao.propor_lance(Lance(self, valor))
        self.__saldo -= valor

    def __valor_valido(self, valor: float):
        return valor <= self.__saldo


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

        if self.__lance_valido(lance):
            if not self.__possui_lances():
                self.menor_lance = lance.valor

            self.maior_lance = lance.valor

            self.__lances.append(lance)

    @property
    def lances(self):
        return deepcopy(self.__lances)

    def __possui_lances(self):
        return self.__lances

    def __usuarios_diferentes(self, lance):
        if self.__lances[-1].usuario != lance.usuario:
            return True

        raise LanceInvalido('O mesmo usuário não pode propor dois lances seguidos')

    def __lance_maior_que_anterior(self, lance):
        if lance.valor > self.__lances[-1].valor:
            return True

        raise LanceInvalido('O valor do lance deve ser maior do que o lance anterior')

    def __lance_valido(self, lance):
        return not self.__possui_lances() or (
                self.__usuarios_diferentes(lance) and self.__lance_maior_que_anterior(lance))
