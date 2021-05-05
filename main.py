from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from matplotlib.backend_bases import MouseButton
from tkinter import Button
import tkinter as tk
import matplotlib.pyplot as plt
import random

fig = None
ax = None
canvas = None


class Application(object):
    def __init__(self):
        self.perceptron = Perceptron()

    def create_window(self):
        global ax
        global fig
        global canvas
        fig = Figure(figsize=(5, 5))

        ax = fig.add_subplot(111)
        ax.set_xlim([-1, 1])
        ax.set_ylim([-1, 1])
        ax.grid(True)

        window = tk.Tk()
        window.wm_title("Luis Medina - IA2 - Practica 2")

        canvas = FigureCanvasTkAgg(fig, master=window)
        canvas.draw()

        wid = canvas.get_tk_widget()
        wid.grid(row=0, column=2, rowspan=50)

        # self.perceptron.setPlt(ax, fig)

        Button(window, text="Start",
               command=self.perceptron.train).grid(row=3,
                                                   column=0,
                                                   columnspan=2)
        Button(window, text="Reset", command=self.reset).grid(row=4,
                                                              column=0,
                                                              columnspan=2)

        canvas.mpl_connect('button_press_event', self.onclick)
        tk.mainloop()

    def reset(self):
        self.perceptron = Perceptron()
        ax.clear()
        ax.grid(True)
        ax.set_xlim([-10, 10])
        ax.set_ylim([-10, 10])
        fig.canvas.draw()

    def onclick(self, event):
        x, y = event.xdata, event.ydata
        if event.button == MouseButton.LEFT:
            self.perceptron.inputs.append([[1, x, y], 0])
            ax.plot(event.xdata, event.ydata, color='red', marker='o')
        elif event.button == MouseButton.RIGHT:
            self.perceptron.inputs.append([[1, x, y], 1])
            ax.plot(event.xdata, event.ydata, color='blue', marker='o')
        fig.canvas.draw()


class Perceptron:
    def __init__(self,
                 no_of_inputs=2,
                 learning_rate=0.1,
                 umbral=0,
                 max_epochs=50):
        self.inputs = []
        self.umbral = umbral
        self.max_epochs = max_epochs
        self.learning_rate = learning_rate  # ETA
        self.weights = [random.uniform(0, 1) for _ in range(no_of_inputs + 1)]
        # self.weights = [0, 0, 0]

    def predict(self, inputs):
        # summation = producto_punto(inputs, self.weights[1:]) + self.weights[0]
        summation = producto_punto(inputs, self.weights)
        if summation > self.umbral:
            activation = 1
        else:
            activation = 0
        return activation

    def train(self):
        # self.inputs = [((1, 0, 0), 1), ((1, 0, 1), 1), ((1, 1, 0), 1),
        #                ((1, 1, 1), 0)]

        epochs = 0
        while True:
            print('-' * 60)
            err_count = 0
            for vector_de_entrada, salida_deseada in self.inputs:
                print(self.weights)

                prediction = self.predict(vector_de_entrada)
                error = salida_deseada - prediction

                if error != 0:
                    err_count += 1
                    for idx, valor in enumerate(vector_de_entrada):
                        self.weights[idx] += self.learning_rate * error * valor

            if err_count == 0:
                print("Exito! Entrenamiento finalizado.")
                break

            if epochs > self.max_epochs:
                print("Limite de epocas alcanzado.")
                break

            # if epochs % 5 == 0:
            self.draw_line()

            epochs += 1

    def draw_line(self):
        global fig
        global ax

        ax.clear()
        ax.grid(True)
        ax.set_xlim([-1, 1])
        ax.set_ylim([-1, 1])

        x_list = []
        y_list = []

        for inp, exp in self.inputs:
            x = inp[1]
            y = inp[2]

            try:
                m = -self.weights[1] / self.weights[2]
                org_y = -self.weights[0] / self.weights[1]
            except ZeroDivisionError:
                continue

            x_list.append(x)
            y_list.append(m * x + org_y)

            if exp == 0:
                ax.plot(x, y, 'ro')
            else:
                ax.plot(x, y, 'bo')

        print(x_list, y_list)
        ax.plot(x_list, y_list, 'g')
        fig.canvas.draw()
        plt.pause(0.5)
        fig.canvas.flush_events()


def producto_punto(valores, pesos):
    return sum(valor * peso for valor, peso in zip(valores, pesos))


def main():
    app = Application()
    app.create_window()


if __name__ == "__main__":
    main()
