from unittest import TestCase
from src.leilao.dominio import Usuario, Lance, Leilao
from src.leilao.excecoes import LanceInvalido


class TestLeilao(TestCase):

    def setUp(self):
        self.gui = Usuario('Gui', 500.0)
        self.lance_gui = Lance(self.gui, 150.0)
        self.leilao = Leilao('Celular')

    def test_deve_retornar_valores_corretos_ao_inserir_em_ordem_crescente(self):
        yuri = Usuario('Yuri', 500.0)
        lance_yuri = Lance(yuri, 100.0)

        self.leilao.propor_lance(lance_yuri)
        self.leilao.propor_lance(self.lance_gui)

        menor_valor_esperado = 100.0
        maior_valor_esperado = 150.0

        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

    def test_nao_deve_permitir_propor_novo_lance_com_valor_menor_que_lance_anterior(self):
        yuri = Usuario('Yuri', 500.0)
        lance_yuri = Lance(yuri, 100.0)

        with self.assertRaises(LanceInvalido):
            self.leilao.propor_lance(self.lance_gui)
            self.leilao.propor_lance(lance_yuri)

    def test_deve_retornar_o_mesmo_valor_para_os_dois_lances_ao_inserir_um_lance(self):
        self.leilao.propor_lance(self.lance_gui)

        self.assertEqual(150.0, self.leilao.menor_lance)
        self.assertEqual(150.0, self.leilao.maior_lance)

    def test_deve_retornar_valores_corretos_ao_inserir_tres_lances(self):
        yuri = Usuario('Yuri', 500.0)
        vini = Usuario('Vini', 500.0)
        lance_yuri = Lance(yuri, 200.0)
        lance_vini = Lance(vini, 250.0)

        self.leilao.propor_lance(self.lance_gui)
        self.leilao.propor_lance(lance_yuri)
        self.leilao.propor_lance(lance_vini)

        self.assertEqual(150.0, self.leilao.menor_lance)
        self.assertEqual(250.0, self.leilao.maior_lance)

    def test_deve_permitir_propor_lance_caso_nao_exista_lances(self):
        self.leilao.propor_lance(self.lance_gui)
        quantidade_lances = len(self.leilao.lances)

        self.assertEqual(1, quantidade_lances)

    def test_deve_permitir_propor_lance_caso_ultimo_usuario_seja_diferente(self):
        yuri = Usuario('Yuri', 500.0)
        lance_yuri = Lance(yuri, 200.0)

        self.leilao.propor_lance(self.lance_gui)
        self.leilao.propor_lance(lance_yuri)

        quantidade_lances = len(self.leilao.lances)

        self.assertEqual(2, quantidade_lances)

    def test_nao_deve_permitir_propor_lance_caso_usuario_seja_o_mesmo(self):
        lance_gui_2 = Lance(self.gui, 200)

        with self.assertRaises(LanceInvalido):
            self.leilao.propor_lance(self.lance_gui)
            self.leilao.propor_lance(lance_gui_2)
