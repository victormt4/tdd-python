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

    def test_deve_retornar_o_mesmo_valor_para_os_dois_lances_ao_inserir_um_lance(self):
        gui = Usuario('Gui')
        lance_gui = Lance(gui, 150.0)

        leilao = Leilao('Celular')
        leilao.lances.append(lance_gui)

        avaliador = Avaliador()
        avaliador.avalia(leilao)

        self.assertEqual(150.0, avaliador.menor_lance)
        self.assertEqual(150.0, avaliador.maior_lance)

    def test_deve_retornar_valores_corretos_ao_inserir_tres_lances(self):
        gui = Usuario('Gui')
        yuri = Usuario('Yuri')
        vini = Usuario('Vini')

        lance_gui = Lance(gui, 150.0)
        lance_yuri = Lance(yuri, 100.0)
        lance_vini = Lance(vini, 200.0)

        leilao = Leilao('Celular')
        leilao.lances.append(lance_gui)
        leilao.lances.append(lance_yuri)
        leilao.lances.append(lance_vini)

        avaliador = Avaliador()
        avaliador.avalia(leilao)

        self.assertEqual(100.0, avaliador.menor_lance)
        self.assertEqual(200.0, avaliador.maior_lance)
