from unittest import TestCase

from src.leilao.dominio import Usuario, Lance, Leilao, Avaliador


class TestAvaliador(TestCase):

    def test_deve_retornar_valores_corretos_ao_inserir_em_ordem_crescente(self):
        gui = Usuario('Gui')
        yuri = Usuario('Yuri')

        lance_gui = Lance(gui, 150.0)
        lance_yuri = Lance(yuri, 100.0)

        leilao = Leilao('Celular')

        leilao.lances.append(lance_gui)
        leilao.lances.append(lance_yuri)

        avaliador = Avaliador()
        avaliador.avalia(leilao)

        menor_valor_esperado = 100.0
        maior_valor_esperado = 150.0

        self.assertEqual(menor_valor_esperado, avaliador.menor_lance)
        self.assertEqual(maior_valor_esperado, avaliador.maior_lance)

    def test_deve_retornar_valores_corretos_ao_inserir_em_ordem_decrescente(self):
        yuri = Usuario('Yuri')
        gui = Usuario('Gui')

        lance_yuri = Lance(yuri, 100.0)
        lance_gui = Lance(gui, 150.0)

        leilao = Leilao('Celular')

        leilao.lances.append(lance_gui)
        leilao.lances.append(lance_yuri)

        avaliador = Avaliador()
        avaliador.avalia(leilao)

        menor_valor_esperado = 100.0
        maior_valor_esperado = 150.0

        self.assertEqual(menor_valor_esperado, avaliador.menor_lance)
        self.assertEqual(maior_valor_esperado, avaliador.maior_lance)
