from Calculadora import Calculadora as calc
from Interface import Interface as GUI

calc = calc()
tela = GUI(500, 350)

tela.label(110, 10, "Calculadora Financeira", font=("Arial", 20))

tela.label(15, 75, "Valor inicial")
input_valor_inicial = tela.entry(125, 75, 20)

tela.label(15, 100, "Valor montante")
input_montante = tela.entry(125, 100, 20)

tela.label(15, 125, "Taxa de juros (%)")
input_taxa_de_juros = tela.entry(125, 125, 20)

tela.label(15, 150, "Periodos")
input_periodos = tela.entry(125, 150, 20)

def calcular():
    pass

tela.button(125, 175, "Calcular", command=lambda: (
    calcular()
))
tela.button(200, 175, "Limpar", command=lambda: (
    input_valor_inicial.delete(0, len(input_valor_inicial.get())),
    input_montante.delete(0, len(input_montante.get())),
    input_taxa_de_juros.delete(0, len(input_taxa_de_juros.get())),
    input_periodos.delete(0, len(input_periodos.get()))
))

print(calc.calcular_juros_simples(valor_inicial=1000, taxa_de_juros=0.10, periodos=3))
print(calc.calcular_juros_simples(juros=300, taxa_de_juros=0.10, periodos=3))
print(calc.calcular_juros_simples(juros=300, valor_inicial=1000, periodos=3))
print(calc.calcular_juros_simples(juros=300, valor_inicial=1000, taxa_de_juros=0.10))

print(calc.calcula_juros_compostos(valor_inicial=1000, taxa_de_juros=0.05, periodos=3))
print(calc.calcula_juros_compostos(montante=1157.63, taxa_de_juros=0.05, periodos=3))
print(calc.calcula_juros_compostos(valor_inicial=1000, montante=1157.63, periodos=3))
print(calc.calcula_juros_compostos(valor_inicial=1000, montante=1157.63, taxa_de_juros=0.05))

tela.start()
