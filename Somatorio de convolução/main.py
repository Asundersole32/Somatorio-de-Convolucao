import sympy as sp
from plot import Signal

function_interval = []
while True:
    formula = input("Insira a formula do sinal(caso seja o final da descrição, digite 0): ");
    if formula != '0':
        formula_indicator = sp.sympify(formula)

        start = float(input('Inicio do intervalo: '))
        end = float(input('Fim do intervalo: '))

        function_interval.append([formula_indicator, [start, end]])
    else:
        function_interval.append('0')
        break

    signal = Signal(function_interval)
    select = False
    while not select:
        signal.plot("original.png")
        break

