from datetime import date


class Funcionario:
    def __init__(self, nome, data_nascimento, salario):
        self._nome = nome
        self._data_nascimento = data_nascimento
        self._salario = salario

    @property
    def nome(self):
        return self._nome

    @property
    def salario(self):
        return self._salario

    def idade(self):
        partes_data = self._data_nascimento.split("/")
        ano_nascimento_str = partes_data[2]
        ano_atual = date.today().year

        return ano_atual - int(ano_nascimento_str)

    def sobrenome(self):
        nome_completo = self.nome.strip()
        nome_quebrado = nome_completo.split(" ")
        return nome_quebrado[-1]

    def _verificar_socio(self):
        sobrenomes = ["Gabriel", "Leandro", "Davi"]
        return self.salario >= 100000 and (self.sobrenome() in sobrenomes)

    def decrescimo_salario(self):
        if self._verificar_socio():
            decrescimo = self._salario * 0.1
            self._salario = self._salario - decrescimo
        return self._salario

    def calcular_bonus(self):
        valor = self._salario * 0.1
        if valor > 1000:
            raise Exception("Salario alto demais para receber bonus")
        return valor

    def __str__(self):
        return f"Funcionario({self._nome}, {self._data_nascimento}, {self._salario})"
