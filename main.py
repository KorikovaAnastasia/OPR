import matplotlib.pyplot as plt
from tkinter import *
from math import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np


def plot_function(f, x_range):
    x = np.linspace(x_range[0], x_range[1], 100)
    y = f(x)

    fig = Figure(figsize=(5, 4), dpi=100)
    ax = fig.add_subplot(111)
    ax.plot(x, y)

    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.draw()
    canvas.get_tk_widget().place(x=200, y=10)


def clicked():
    value_x0 = int(enter_x0.get())
    value_x1 = int(enter_x1.get())
    value_eps = float(enter_eps.get())

    result_output = Label(window)
    result_output.place(x=0, y=400)

    if selected.get() == 1:
        res = secant_method(f1, value_x0, value_x1, value_eps, it)
        output_result = "Ответ: {}".format(res)
        result_output.configure(text=output_result, font=("Arial", 14, "bold"))
        plot_function(f1, [value_x0, value_x1])
    elif selected.get() == 2:
        res = secant_method(f2, value_x0, value_x1, value_eps, it)
        output_result = "Ответ: {}".format(res)
        result_output.configure(text=output_result, font=("Arial", 14, "bold"))
        plot_function(f2, [value_x0, value_x1])
    elif selected.get() == 3:
        res = secant_method(f3, value_x0, value_x1, value_eps, it)
        output_result = "Ответ: {}".format(res)
        result_output.configure(text=output_result, font=("Arial", 14, "bold"))
        plot_function(f3, [value_x0, value_x1])
    else:
        result_output.configure(text='Вы должны выбрать функцию!')

window = Tk()
window.title("Метод секущих")
window.geometry('720x450')

h1 = Label(window, text="Метод секущих", font=("Arial", 16, "bold"))
h1.place(x=30, y=18, anchor="w")

lbl_x0 = Label(window, text="x0: ")
lbl_x0.place(x=10, y=50, anchor="w")
lbl_x1 = Label(window, text="x1: ")
lbl_x1.place(x=10, y=90, anchor="w")
lbl_eps = Label(window, text="epsilon: ")
lbl_eps.place(x=10, y=130, anchor="w")

fig = Figure(figsize=(5, 4), dpi=100)
ax = fig.add_subplot(111)
ax.plot(0, 0)

canvas = FigureCanvasTkAgg(fig, master=window)
canvas.draw()
canvas.get_tk_widget().place(x=200, y=10)

enter_x0 = Entry(window, width=10)
enter_x0.place(x=80, y=40)
enter_x1 = Entry(window, width=10)
enter_x1.place(x=80, y=80)
enter_eps = Entry(window, width=10)
enter_eps.place(x=80, y=120)

enter_x0.focus()

enter_x0.insert(0, "0")
enter_x1.insert(0, "1")
enter_eps.insert(0, "0.001")

selected = IntVar()

rad1 = Radiobutton(window, text='x^2 - 4', value=1, variable=selected)
rad2 = Radiobutton(window, text='x + 5', value=2, variable=selected)
rad3 = Radiobutton(window, text='2x^3 + 7', value=3, variable=selected)

rad1.select()

rad1.place(x=10, y=180, anchor="w")
rad2.place(x=10, y=205, anchor="w")
rad3.place(x=10, y=230, anchor="w")


btn = Button(window, text="Вычислить", command=clicked)
btn.place(x=10, y=260)


def f1(x):
    return x ** 2 - 4


def f2(x):
    return x + 5


def f3(x):
    return 2 * x**3 + 7


def secant_method(f, x0, x1, epsilon, max_iterations):
    x_prev = x0
    x_curr = x1
    iterations = 0
    x_range = [x_prev, x_curr]
    x = np.linspace(x_range[0], x_range[1], 100)
    y = f(x)

    fig = plt.figure(figsize=(5, 4), dpi=100)
    ax = fig.add_subplot(111)
    ax.plot(x, y)

    x_prev = x_range[0]
    x_curr = x_range[1]
    secant_x = np.array([x_prev, x_curr])
    secant_y = f(secant_x)
    ax.plot(secant_x, secant_y, color='red', linestyle='--')

    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.draw()
    canvas.get_tk_widget().place(x=200, y=10)

    while abs(f(x_curr)) > epsilon and iterations < max_iterations:
        x_next = x_curr - (f(x_curr) * (x_curr - x_prev)) / (f(x_curr) - f(x_prev))
        x_prev = x_curr
        x_curr = x_next
        iterations += 1

    if abs(f(x_curr)) <= epsilon:
        return x_curr
    else:
        return 0

it = 10000

window.mainloop()
