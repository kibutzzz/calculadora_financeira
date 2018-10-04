from Calculadora import Calculadora as calc

calc = calc()

print(calc.calcular_juros_simples(valor_inicial=1000, taxa_de_juros=0.10, peridos=3))
print(calc.calcular_juros_simples(juros=300, taxa_de_juros=0.10, peridos=3))
print(calc.calcular_juros_simples(juros=300, valor_inicial=1000,  peridos=3))
print(calc.calcular_juros_simples(juros=300, valor_inicial=1000, taxa_de_juros=0.10))
