from src.leilao.dominio import Usuario, Leilao


def test_deve_subtrair_valor_da_carteira_ao_propor_lance():
    vini = Usuario('Vini', 100.0)
    leilao = Leilao('Celular')

    vini.propor_lance(leilao, 50.0)

    assert vini.saldo == 50.0


def test_deve_permitir_propor_lance_caso_valor_seja_menor_que_saldo():
    vini = Usuario('Vini', 100.0)
    leilao = Leilao('Celular')

    vini.propor_lance(leilao, 1.0)

    assert vini.saldo == 99.0


def test_deve_permitir_propor_lance_caso_valor_seja_igual_ao_saldo():
    vini = Usuario('Vini', 100.0)
    leilao = Leilao('Celular')

    vini.propor_lance(leilao, 100.0)

    assert vini.saldo == 0.0


def test_nao_deve_permitir_propor_lance_caso_valor_seja_maior_que_saldo():
    vini = Usuario('Vini', 100.0)
    leilao = Leilao('Celular')

    vini.propor_lance(leilao, 200.0)

    assert vini.saldo == 100.0
