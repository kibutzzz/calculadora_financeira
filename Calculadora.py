import math

class Calculadora:

    def calcular_juros_simples(self, juros=None, valor_inicial=None, taxa_de_juros=None,
                               peridos=None):
        opcao = 0
        parametros_nulos = 0
        if juros is None:
            parametros_nulos += 1
        if valor_inicial is None:
            parametros_nulos += 1
            opcao = 1
        if taxa_de_juros is None:
            parametros_nulos += 1
            opcao = 2
        if peridos is None:
            parametros_nulos += 1
            opcao = 3

        if parametros_nulos > 1:
            return None

        if opcao == 0:
            return self.__calcula_juros_simples(valor_inicial, taxa_de_juros, peridos)
        if opcao == 1:
            return self.__calcula_valor_inicial_simples(juros, taxa_de_juros, peridos)
        if opcao == 2:
            return self.__calcula_taxa_de_juros_simples(juros, valor_inicial, peridos)
        if opcao == 3:
            return self.__calcula_periodos_simples(juros, valor_inicial, taxa_de_juros)

    def __calcula_juros_simples(self, valor_inicial, taxa_de_juros, periodos):
        return valor_inicial * taxa_de_juros * periodos

    def __calcula_valor_inicial_simples(self, juros, taxa_de_juros, periodos):
        return juros / (taxa_de_juros * periodos)

    def __calcula_taxa_de_juros_simples(self, juros, valor_inicial, periodos):
        return juros / (valor_inicial * periodos)

    def __calcula_periodos_simples(self, juros, valor_inicial, taxa_de_juros):
        return juros / (valor_inicial * taxa_de_juros)

