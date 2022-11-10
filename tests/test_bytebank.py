import pytest
from codigo.bytebank import Funcionario
from pytest import mark

class TestClass:

    def test_quando_data_recebe_13_03_2000_deve_retornar_22(self):
        entrada = "13/03/2000"
        esperado = 22

        funcionario_teste = Funcionario("Teste", entrada, 1111)
        resultado = funcionario_teste.idade()
        assert resultado == esperado

    def test_quando_o_nome_recebe_Lucas_Carvalho_deve_retornar_apenas_Carvalho(self):
        entrada = "Lucas Carvalho"
        esperado = "Carvalho"

        funcionario_teste1 = Funcionario("Lucas Carvalho", entrada, 1111)
        resultado = funcionario_teste1.sobrenome()

        assert resultado == esperado

    def test_quando_descrecimo_salario_recebe_100000_deve_retornar_90000(self):
            entrada = 100000
            esperado = 90000

            funcionario_teste2 = Funcionario("Teste Bragança", "11/11/2020", entrada)
            funcionario_teste2.decrescimo_salario()
            resultado = funcionario_teste2.salario

            assert resultado == esperado

    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_1000_deve_retornar_100(self):
        entrada = 1000
        esperado = 100

        funcionario_teste3 = Funcionario("Teste", "11/11/2020", entrada)
        resultado = funcionario_teste3.calcular_bonus()

        assert resultado == esperado

    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_100000000_deve_retornar_exception(self):
        with pytest.raises(Exception):
            entrada = 100000000

            funcionario_teste4 = Funcionario("Teste", "11/11/2020", entrada)
            resultado = funcionario_teste4.calcular_bonus()

            assert resultado
