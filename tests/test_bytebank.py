from codigo.bytebank import Funcionario  # Linha alterada


class TestClass:
    # Nome do teste agora corresponde ao ano de entrada
    def test_quando_idade_recebe_13_03_2003_deve_retornar_22(self):
        entrada = "13/03/2003"
        esperado = 22

        funcionario_test = Funcionario("Leonardo", entrada, 5000)
        resultado = funcionario_test.idade()

        assert resultado == esperado

    def test_quando_sobrenome_recebe_Leonardo_Gabriel_deve_retornar_Gabriel(self):
        entrada = "Leonardo Gabriel"  # Given esperado
        esperado = "Gabriel"

        funcionario_test = Funcionario(entrada, "01/01/2003", 5000)
        resultado = funcionario_test.sobrenome()  # When ação

        assert resultado == esperado  # Then desfecho

    def test_decrescimo_salario_recebe_100000_deve_retornar_90000(self):
        entrada_salario = 100000
        entrada_nome = "Gabriel"
        esperado = 90000

        funcionario_test = Funcionario(entrada_nome, "01/01/2003", entrada_salario)
        resultado = funcionario_test.decrescimo_salario()

        assert resultado == esperado
