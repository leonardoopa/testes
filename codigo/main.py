from bytebank import Funcionario # Linha alterada

# funcionario = Funcionario("João", "1990/01/01", 3000)
# print(funcionario.nome)
# print(funcionario.idade())
# print(funcionario.calcular_bonus())



def test_idade():
    funcionario_test = Funcionario("Leonardo", "01/01/2003", 5000)
    print(f'Idade: {funcionario_test.idade()}')


test_idade()    