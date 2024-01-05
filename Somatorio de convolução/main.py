import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from Signal import Signal


def first_signal():
    formulas = []
    function_interval = []
    start_time = []
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
    start_time_value = signal.get_start()
    start_time.append(start_time_value)
    while not select:
        operation = input("Deseja fazer um Deslocamento Temporal: ")
        operation = operation.lower()

        if operation == "sim":
            parameter = int(input("Insira o parametro da operação: "))
            new_signal = signal.time_shifting(parameter)
            new_signal_values = signal.get_values(new_signal)
            formulas.append(new_signal_values)
            new_start_time_value = signal.get_start(parameter)
            start_time.append(new_start_time_value)
            signal.plot('first_signal.png', 'First Signal')
            signal.plot('shifted_first_signal.png', 'Shifted First Signal', new_signal)
            break
        elif operation == "não":
            signal.plot("first_signal.png", "First Signal")
            break
        else:
            print("Responda com sim ou não!")

    print(' ')
    formulas.append(start_time)

    return formulas


def second_signal():
    formulas = []
    function_interval = []
    start_time = []
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
    signal_formula = signal.get_values()
    formulas.append(signal_formula)
    start_time_value = signal.get_start()
    start_time.append(start_time_value)
    while not select:
        operation = input("Deseja fazer um Deslocamento Temporal: ")
        operation = operation.lower()

        if operation == "sim":
            parameter = int(input("Insira o parametro da operação: "))
            new_signal = signal.time_shifting(parameter)
            new_formula = signal.get_values(new_signal)
            formulas.append(new_formula)
            new_start_time_value = signal.get_start(parameter)
            start_time.append(new_start_time_value)
            signal.plot('second_signal.png', 'Second Signal')
            signal.plot('shifted_second_signal.png', 'Shifted Second Signal', new_signal)
            break
        elif operation == "não":
            signal.plot("second_signal.png", "Second Signal")
            break
        else:
            print("Responda com sim ou não!")

    print(" ")
    formulas.append(start_time)

    return formulas


def convolution(first_start, second_start, first_signal, second_signal, title=None, save_file=None):
    print(first_signal)
    print(second_signal)
    conv_signal = []
    for n in range(len(second_signal)):
        print("n: ", n)
        sum = 0
        for t in range(len(first_signal)):
            print("t: ", t)
            if first_signal[t] != 0:
                conv = first_signal[t]*second_signal[n - t]
                print("Conv: ", conv)
                sum = sum + conv
            print("Sum: ", sum)
        if sum != 0:
            conv_signal.append(sum)
            print("Conv_signal: ", conv_signal)

    conv_start = first_start + second_start
    conv_end = 10
    for i in range(conv_end-len(conv_signal)):
        conv_signal.append(0)
    plot_size = len(conv_signal)
    t_values = np.linspace(conv_start, 10, plot_size)

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

    print(" ")


first = first_signal()
second = second_signal()

first_signal_list = []
second_signal_list = []
for i in range(len(first)-1):
    first_signal_list.append(first[i])
    second_signal_list.append(second[i])

first_signals_starts = first[-1]
second_signals_starts = second[-1]

for x in range(len(first_signal_list)):
    print("Conv_process: ", x+1)
    convolution(first_signals_starts[x],
                second_signals_starts[x],
                first_signal_list[x],
                second_signal_list[x],
                "Convolution Signal "+str(x+1),
                "convolution_signal_"+str(x+1)+".png")
