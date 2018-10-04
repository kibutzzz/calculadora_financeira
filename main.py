from Calculadora import Calculadora as calc

calc = calc()

print(calc.calcular_juros_simples(valor_inicial=1000, taxa_de_juros=0.10, periodos=3))
print(calc.calcular_juros_simples(juros=300, taxa_de_juros=0.10, periodos=3))
print(calc.calcular_juros_simples(juros=300, valor_inicial=1000,  periodos=3))
print(calc.calcular_juros_simples(juros=300, valor_inicial=1000, taxa_de_juros=0.10))

print(calc.calcula_juros_compostos(valor_inicial=1000, taxa_de_juros=0.05, periodos=3))
print(calc.calcula_juros_compostos(montante=1157.63, taxa_de_juros=0.05, periodos=3))
print(calc.calcula_juros_compostos(valor_inicial=1000, montante=1157.63, periodos=3))

