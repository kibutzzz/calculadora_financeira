import math


class Calculadora:

    def calcular_juros_simples(self, juros=None, valor_inicial=None, taxa_de_juros=None,
                               periodos=None):
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
        if periodos is None:
            parametros_nulos += 1
            opcao = 3

        if parametros_nulos > 1:
            return None

        if opcao == 0:
            return self.__calcula_juros_simples(valor_inicial, taxa_de_juros, periodos)
        if opcao == 1:
            return self.__calcula_valor_inicial_simples(juros, taxa_de_juros, periodos)
        if opcao == 2:
            return self.__calcula_taxa_de_juros_simples(juros, valor_inicial, periodos)
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

    def calcula_juros_compostos(self, montante=None, valor_inicial=None, taxa_de_juros=None,
                                periodos=None):
        opcao = 0
        parametros_nulos = 0
        if montante is None:
            parametros_nulos += 1
        if valor_inicial is None:
            parametros_nulos += 1
            opcao = 1
        if taxa_de_juros is None:
            parametros_nulos += 1
            opcao = 2
        if periodos is None:
            parametros_nulos += 1
            opcao = 3

        if parametros_nulos > 1:
            return None

        if opcao == 0:
            return self.__calcula_montante_composto(valor_inicial, taxa_de_juros, periodos)
        if opcao == 1:
            return self.__calcula_valor_inicial_composto(montante, taxa_de_juros, periodos)
        if opcao == 2:
            return self.__calcula_taxa_de_juros_composto(montante, valor_inicial, periodos)
        if opcao == 3:
            return self.__calcula_periodos_composto(montante, valor_inicial, taxa_de_juros)

    def __calcula_montante_composto(self, valor_inicial, taxa_de_juros, periodos):
        return valor_inicial * math.pow((1 + taxa_de_juros), periodos)

    def __calcula_valor_inicial_composto(self, montante, taxa_de_juros, periodos):
        return montante / math.pow((1 + taxa_de_juros), periodos)

    def __calcula_taxa_de_juros_composto(self, montante, valor_inicial, periodos):
        return

    def __calcula_periodos_composto(self, montante, valor_inicial, taxa_de_juros):
        return
