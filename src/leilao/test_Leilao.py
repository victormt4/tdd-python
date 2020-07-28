from unittest import TestCase

from src.leilao.dominio import Usuario, Lance, Leilao


class TestLeilao(TestCase):

    def setUp(self):
        self.gui = Usuario('Gui')
        self.lance_gui = Lance(self.gui, 150.0)
        self.leilao = Leilao('Celular')

    def test_deve_retornar_valores_corretos_ao_inserir_em_ordem_crescente(self):
        yuri = Usuario('Yuri')
        lance_yuri = Lance(yuri, 100.0)

        self.leilao.propor_lance(lance_yuri)
        self.leilao.propor_lance(self.lance_gui)

        menor_valor_esperado = 100.0
        maior_valor_esperado = 150.0

        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

    def test_deve_retornar_valores_corretos_ao_inserir_em_ordem_decrescente(self):
        yuri = Usuario('Yuri')
        lance_yuri = Lance(yuri, 100.0)

        self.leilao.propor_lance(self.lance_gui)
        self.leilao.propor_lance(lance_yuri)

        menor_valor_esperado = 100.0
        maior_valor_esperado = 150.0

        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

    def test_deve_retornar_o_mesmo_valor_para_os_dois_lances_ao_inserir_um_lance(self):
        self.leilao.propor_lance(self.lance_gui)

        self.assertEqual(150.0, self.leilao.menor_lance)
        self.assertEqual(150.0, self.leilao.maior_lance)

    def test_deve_retornar_valores_corretos_ao_inserir_tres_lances(self):
        yuri = Usuario('Yuri')
        vini = Usuario('Vini')
        lance_yuri = Lance(yuri, 100.0)
        lance_vini = Lance(vini, 200.0)

        self.leilao.propor_lance(self.lance_gui)
        self.leilao.propor_lance(lance_yuri)
        self.leilao.propor_lance(lance_vini)

        self.assertEqual(100.0, self.leilao.menor_lance)
        self.assertEqual(200.0, self.leilao.maior_lance)
