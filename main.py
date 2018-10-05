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


def calcular_simples(montante, principal, taxa, periodos_decorridos):
    campos_vazios = 0
    opcao = 0
    if montante == "":
        montante = None
        campos_vazios += 1
        opcao = 0
    if principal == "":
        principal = None
        campos_vazios += 1
        opcao = 1
    if taxa == "":
        taxa = None
        campos_vazios += 1
        opcao = 2
    if periodos_decorridos == "":
        periodos_decorridos = None
        campos_vazios += 1
        opcao = 3

    if campos_vazios is not 1:
        print("numero de valores repassados não está correto")
        return

    if opcao is 0:
        input_montante.insert(0, (calc.calcular_juros_simples(
            valor_inicial=float(principal),
            taxa_de_juros=float(taxa) / 100,
            periodos=float(periodos_decorridos)
        ) + float(principal)))

    if opcao is 1:
        input_valor_inicial.insert(0, (calc.calcular_juros_simples(
            juros=float(montante),
            taxa_de_juros=float(taxa) / 100,
            periodos=float(periodos_decorridos)
        )))

    if opcao is 2:
        input_taxa_de_juros.insert(0, (calc.calcular_juros_simples(
            valor_inicial=float(principal),
            juros=float(montante) - float(principal),
            periodos=float(periodos_decorridos)
        )) * 100)

    if opcao is 3:
        input_periodos.insert(0, (calc.calcular_juros_simples(
            valor_inicial=float(principal),
            juros=float(montante) - float(principal),
            taxa_de_juros=float(taxa) / 100
        )))


def calcular_composto(montante, principal, taxa, periodos_decorridos):
    campos_vazios = 0
    opcao = 0
    if montante == "":
        montante = None
        campos_vazios += 1
        opcao = 0
    if principal == "":
        principal = None
        campos_vazios += 1
        opcao = 1
    if taxa == "":
        taxa = None
        campos_vazios += 1
        opcao = 2
    if periodos_decorridos == "":
        periodos_decorridos = None
        campos_vazios += 1
        opcao = 3

    if campos_vazios is not 1:
        print("numero de valores repassados não está correto")
        return

    if opcao is 0:
        input_montante.insert(0, (calc.calcular_juros_compostos(
            valor_inicial=float(principal),
            taxa_de_juros=float(taxa) / 100,
            periodos=float(periodos_decorridos)
        )))

    if opcao is 1:
        input_valor_inicial.insert(0, (calc.calcular_juros_compostos(
            montante=float(montante),
            taxa_de_juros=float(taxa) / 100,
            periodos=float(periodos_decorridos)
        )))

    if opcao is 2:
        input_taxa_de_juros.insert(0, (calc.calcular_juros_compostos(
            valor_inicial=float(principal),
            montante=float(montante),
            periodos=float(periodos_decorridos)
        )) * 100)

    if opcao is 3:
        input_periodos.insert(0, (calc.calcular_juros_compostos(
            valor_inicial=float(principal),
            montante=float(montante),
            taxa_de_juros=float(taxa)/100
        )))


tela.button(15, 175, "Calcular juros simples", command=lambda: (
    calcular_simples(
        input_montante.get(),
        input_valor_inicial.get(),
        input_taxa_de_juros.get(),
        input_periodos.get()
    )
))

tela.button(15, 200, "Calcular juros composto", command=lambda: (
    calcular_composto(
        input_montante.get(),
        input_valor_inicial.get(),
        input_taxa_de_juros.get(),
        input_periodos.get()
    )
))

tela.button(15, 225, "Limpar", command=lambda: (
    input_valor_inicial.delete(0, len(input_valor_inicial.get())),
    input_montante.delete(0, len(input_montante.get())),
    input_taxa_de_juros.delete(0, len(input_taxa_de_juros.get())),
    input_periodos.delete(0, len(input_periodos.get()))
))

tela.label(350,330, "Leonardo Meinerz Ramos")
tela.start()
