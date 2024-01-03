import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from Signal import Signal


def first_signal():
    formulas = []
    function_interval = []
    while True:
        formula = input("Insira a formula do sinal(caso seja o final da descrição, digite 0): ")
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
    original_formula = signal.get_values()
    formulas.append(original_formula)
    while not select:
        operation = input("Deseja fazer um Deslocamento Temporal: ")
        operation = operation.lower()

        if operation == "sim":
            parameter = int(input("Insira o parametro da operação: "))
            new_signal = signal.time_shifting(parameter)
            formulas.append(new_signal)
            signal.plot('first_signal.png', 'First Signal')
            signal.plot('shifted_first_signal.png', 'Shifted First Signal', new_signal)
            break
        elif operation == "não":
            signal.plot("first_signal.png", "First Signal")
            break
        else:
            print("Responda com sim ou não!")

    print(' ')
    return formulas


def second_signal():
    formulas = []
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
    original_formula = signal.get_values()
    formulas.append(original_formula)
    while not select:
        operation = input("Deseja fazer um Deslocamento Temporal: ")
        operation = operation.lower()

        if operation == "sim":
            parameter = int(input("Insira o parametro da operação: "))
            new_signal = signal.time_shifting(parameter)
            formulas.append(new_signal)
            signal.plot('second_signal.png', 'Second Signal')
            signal.plot('shifted_second_signal.png', 'Shifted Second Signal', new_signal)
            break
        elif operation == "não":
            signal.plot("second_signal.png", "Second Signal")
            break
        else:
            print("Responda com sim ou não!")

    return formulas


def convolution(first, second, title=None, save_file=None):
    conv_signal = np.convolve(first, second)
    print(conv_signal)
    plot_size = len(conv_signal)
    t_values = np.linspace(-10, 10, plot_size)

    plt.stem(t_values, conv_signal, label='Signal')
    plt.xlabel('t')
    plt.ylabel('Amplitude')
    plt.legend()
    plt.title(title)

    if save_file:
        plt.savefig("output/" + save_file)
        plt.close()
    else:
        plt.show()


first = first_signal()
second = second_signal()

signal_indices = 0

for x in first:
    convolution(first[signal_indices], second[signal_indices], "Original Signals Convolution", "original_signals_convolution.png")
    signal_indices = signal_indices + 1
