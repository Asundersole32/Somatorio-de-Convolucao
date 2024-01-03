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

    def time_shifting(self, shift_amount):
        shifted_signal = self.formula.subs(self.t, self.t - shift_amount)
        return shifted_signal

    def get_values(self, signal=None):
        t_values = np.linspace(-20, 20, 40)
        if signal is None:
            signal_function = sp.lambdify(self.t, self.formula, 'numpy')
            original_signal = signal_function(t_values)
            return original_signal
        else:
            signal_function = sp.lambdify(self.t, signal, 'numpy')
            new_signal = signal_function(t_values)
            return new_signal

    def plot(self, save_file=None, title=None, signal=None):
        t_values = np.linspace(-20, 20, 40)
        if signal is None:
            signal_func = sp.lambdify(self.t, self.formula, 'numpy')
        else:
            signal_func = sp.lambdify(self.t, signal, 'numpy')

        plt.stem(t_values, signal_func(t_values), label='Signal')
        plt.xlabel('t')
        plt.ylabel('Amplitude')
        plt.legend()
        plt.title(title)

        if save_file:
            plt.savefig("output/" + save_file)
            plt.close()
        else:
            plt.show()
