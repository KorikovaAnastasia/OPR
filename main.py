import matplotlib.pyplot as plt
from tkinter import *
from math import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter.messagebox import showerror
import numpy as np


def plot_function(f, x_range):
    x = np.linspace(x_range[0], x_range[1], 100)
    y = f(x)

    fig = Figure(figsize=(5, 4), dpi=100)
    ax = fig.add_subplot(111)
    ax.plot(x, y)

    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.draw()
    canvas.get_tk_widget().grid(column=2, row=9)


def clicked():
    value_x0 = int(enter_x0.get())
    value_x1 = int(enter_x1.get())
    value_eps = float(enter_eps.get())

    result_output = Label(window)
    result_output.grid(column=2, row=8)

    if selected.get() == 1:

        res = secant_method(f1, value_x0, value_x1, value_eps, it)
        output_result = "ответ: {}".format(res)
        result_output.configure(text=output_result)
        plot_function(f1, [value_x0, value_x1])

    elif selected.get() == 2:
        res = secant_method(f2, value_x0, value_x1, value_eps, it)
        output_result = "ответ: {}".format(res)
        result_output.configure(text=output_result)
        plot_function(f2, [value_x0, value_x1])

    elif selected.get() == 3:
        res = secant_method(f3, value_x0, value_x1, value_eps, it)
        output_result = "ответ: {}".format(res)
        result_output.configure(text=output_result)
        plot_function(f3, [value_x0, value_x1])

    else:
        result_output.configure(text='вы должны выбрать функцию!')


window = Tk()
window.title("Метод секущих")
window.geometry('1000x800')  # указание размеров окна
lbl_x0 = Label(window, text="x0: ")
lbl_x0.grid(column=0, row=0, sticky="w")
lbl_x1 = Label(window, text="x1: ")
lbl_x1.grid(column=0, row=1, sticky="w")
lbl_eps = Label(window, text="epsilon: ")
lbl_eps.grid(column=0, row=2, sticky="w")

enter_x0 = Entry(window, width=10)
enter_x0.grid(column=1, row=0, sticky="w")
enter_x1 = Entry(window, width=10)
enter_x1.grid(column=1, row=1, sticky="w")
#
enter_eps = Entry(window, width=10)
#
enter_eps.grid(column=1, row=2)

enter_x0.focus()  # для автоматического наведения на окошко ввода

selected = IntVar()

rad1 = Radiobutton(window, text='x^2 - 4', value=1, variable=selected)
rad2 = Radiobutton(window, text='x + 5', value=2, variable=selected)
rad3 = Radiobutton(window, text='sin(x)', value=3, variable=selected)
rad1.grid(column=0, row=4, sticky="w")
rad2.grid(column=0, row=5, sticky="w")
rad3.grid(column=0, row=6, sticky="w")


btn = Button(window, text="Вычислить", command=clicked)
btn.grid(column=0, row=7)


def f1(x):
    return x ** 2 - 4


def f2(x):
    return x + 5


def f3(x):
    return sin(x)


def secant_method(f, x0, x1, epsilon, max_iterations):

    # Инициализация значений
    x_prev = x0
    x_curr = x1
    iterations = 0

    while abs(f(x_curr)) > epsilon and iterations < max_iterations:
        # Вычисление значения следующей итерации метода секущих
        x_next = x_curr - (f(x_curr) * (x_curr - x_prev)) / (f(x_curr) - f(x_prev))

        # Обновление значений для следующей итерации
        x_prev = x_curr
        x_curr = x_next
        iterations += 1

    # Проверка, достигнута ли допустимая погрешность или максимальное количество итераций
    if abs(f(x_curr)) <= epsilon:
        return x_curr
    else:
        return 0

it = 10000

window.mainloop()
