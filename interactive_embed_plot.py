import numpy as np
from matplotlib.widgets import Slider
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure


class CartesianPlane(object):
    def __init__(self, ax):
        self.ax = ax
        ax.set_title('Click on the canvas to draw a point')
        self.im = ax.imshow()
        self.update()

    def onclick(self, event):
        print('click: x=%d, y=%d' % (event.xdata, event.ydata))
        self.plt.plot(event.xdata, event.ydata, 'r*')
        self.fig.canvas.draw()

    def update(self):
        # self.fig.canvas.draw()
        self.im.set_data(self.X[:, :, self.ind])
        self.ax.set_ylabel('slice %s' % self.ind)
        self.im.axes.figure.canvas.draw()


import tkinter as tk
root = tk.Tk()
fig = Figure()
canvas = FigureCanvasTkAgg(fig, root)
canvas.get_tk_widget().pack(fill="both", expand=True)

ax = fig.subplots(1, 1)
ax.set_xlim([0, 10])
ax.set_ylim([0, 10])

tracker = CartesianPlane(ax)
canvas.mpl_connect('button_press_event', tracker.onclick)
root.mainloop()
