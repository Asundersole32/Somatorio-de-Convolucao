import sympy as sp
import numpy as np
import matplotlib.pyplot as plt


class Signal:
    def __init__(self, function_interval):
        self.t = sp.symbols('t')
        self.expressions = []

        for function in function_interval:
            if function[0] == '0':
                self.expressions.append([0, True])
            else:
                start, end = function[1]
                expressions = function[0].simplify()
                self.expressions.append((expressions, (self.t >= start) & (self.t < end)))

        self.formula = sp.Piecewise(*self.expressions)
        print(self.formula)

    def plot(self, save_file=None):
        t_values = np.linspace(0, 20, 20)
        original_signal_func = sp.lambdify(self.t, self.formula, 'numpy')

        plt.stem(t_values, original_signal_func(t_values), label='Sinal')
        plt.xlabel('t')
        plt.ylabel('Amplitude')
        plt.legend()
        plt.title('Sinal Original')

        if save_file:
            plt.savefig("output/" + save_file)
            plt.close()
        else:
            plt.show()
