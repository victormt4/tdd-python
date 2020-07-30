from src.leilao.dominio import Usuario, Leilao
import pytest


@pytest.fixture
def vini():
    return Usuario('Vini', 100.0)


@pytest.fixture
def leilao():
    return Leilao('Celular')


def test_deve_subtrair_valor_da_carteira_ao_propor_lance(vini, leilao):
    vini.propor_lance(leilao, 50.0)

    assert vini.saldo == 50.0


def test_deve_permitir_propor_lance_caso_valor_seja_menor_que_saldo(vini, leilao):
    vini.propor_lance(leilao, 1.0)

    assert vini.saldo == 99.0


def test_deve_permitir_propor_lance_caso_valor_seja_igual_ao_saldo(vini, leilao):
    vini.propor_lance(leilao, 100.0)

    assert vini.saldo == 0.0


def test_nao_deve_permitir_propor_lance_caso_valor_seja_maior_que_saldo(vini, leilao):
    with pytest.raises(ValueError):
        vini.propor_lance(leilao, 200.0)
