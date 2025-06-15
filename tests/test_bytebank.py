from codigo.bytebank import Funcionario # Linha alterada


class TestClass:
    # Nome do teste agora corresponde ao ano de entrada
    def test_quando_idade_recebe_13_03_2003_deve_retornar_22(self):
        entrada = '13/03/2003'
        esperado = 22

        funcionario_test = Funcionario("Leonardo", entrada, 5000)
        resultado = funcionario_test.idade()

        assert resultado == esperado