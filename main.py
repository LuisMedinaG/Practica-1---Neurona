from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np
import tkinter as tk
from tkinter import Label, Entry, Button


class Neuron:
    def __init__(self, point, w1, w2, bias):
        self.point = point
        self.w1 = w1
        self.w2 = w2
        self.bias = bias
        self.v = self.get_value()

    def get_value(self):
        a = np.array(self.point)
        b = np.array([self.w1, self.w2])
        return np.dot(a, b) - self.bias

    def __repr__(self):
        return str(self.point)


class Chart:
    def __init__(self, ax, fig):
        self.ax = ax
        self.fig = fig
        self.points = []

    def onclick(self, event):
        self.points.append([event.xdata, event.ydata])
        if event.button == 3:
            self.ax.plot(event.xdata, event.ydata, color='red', marker='o')
        elif event.button == 1:
            self.ax.plot(event.xdata, event.ydata, color='blue', marker='o')
        self.fig.canvas.draw()

    def drawChart(self, neurons, eval_func):
        x_list = []
        y_list = []

        for n in neurons:
            try:
                m = -(n.w1 / n.w2)
                a = n.bias / n.w2
                y = m * n.point[0] + a
            except ZeroDivisionError:
                print("ERROR: W2 no puede ser 0")

                x_list.append(n.point[0])
                y_list.append(y)

                if eval_func(n.v) == 0:
                    self.ax.plot(n.point[0], n.point[1], 'ro')
                else:
                    self.ax.plot(n.point[0], n.point[1], 'bo')

        self.ax.plot(x_list, y_list, 'g')
        self.fig.canvas.draw()


class Application(object):
    def __init__(self, chart, w1, w2, bias):
        self.chart = chart
        self.w1 = w1
        self.w2 = w2
        self.bias = bias
        self.neurons = []

    def start(self):
        w1 = int(self.w1.get())
        w2 = int(self.w2.get())
        bias = int(self.bias.get())
        eval_func = lambda v: 0 if v <= 0 else 1

        self.neurons = [Neuron(p, w1, w2, bias) for p in self.chart.points]
        self.chart.drawChart(self.neurons, eval_func)

    def reset(self):
        self.chart.points = []
        self.chart.ax.clear()
        self.chart.ax.set_xlim([-10, 10])
        self.chart.ax.set_ylim([-10, 10])
        self.chart.ax.grid(True)
        self.chart.fig.canvas.draw()


def main():
    fig = Figure(figsize=(5, 5))

    ax = fig.add_subplot(111)
    ax.set_xlim([-10, 10])
    ax.set_ylim([-10, 10])
    ax.grid(True)

    window = tk.Tk()
    window.wm_title("Practica 1")

    w1 = tk.IntVar()
    w2 = tk.IntVar()
    bias = tk.IntVar()

    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.draw()

    wid = canvas.get_tk_widget()
    wid.grid(row=0, column=2, rowspan=50)

    Label(window, text="W1").grid(row=0, column=0)
    Entry(window, textvariable=w1).grid(row=0, column=1, pady=5, padx=5)

    Label(window, text="W2").grid(row=1, column=0)
    Entry(window, textvariable=w2).grid(row=1, column=1, pady=5, padx=5)

    Label(window, text="Bias").grid(row=2, column=0)
    Entry(window, textvariable=bias).grid(row=2, column=1, pady=5, padx=5)

    # Create main app
    chart = Chart(ax, fig)
    app = Application(chart, w1, w1, bias)

    Button(window, text="Start", command=app.start).grid(row=3,
                                                         column=0,
                                                         columnspan=2)
    Button(window, text="Reset", command=app.reset).grid(row=4,
                                                         column=0,
                                                         columnspan=2)

    canvas.mpl_connect('button_press_event', chart.onclick)
    tk.mainloop()


if __name__ == "__main__":
    main()
