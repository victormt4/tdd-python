from src.leilao.dominio import Usuario, Leilao


def test_deve_subtrair_valor_da_carteira_ao_propor_lance():
    vini = Usuario('Vini', 50.0)
    leilao = Leilao('Celular')

    vini.propor_lance(leilao, 50.0)

    assert vini.saldo == 50.0
