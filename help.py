# =======================MATPLOT CLICK & DRAW POINTS=========================
# import matplotlib.pyplot as plt
# from matplotlib.widgets import TextBox
# import numpy as np

# fig = plt.Figure(figsize=(5, 4), dpi=100)
# # fig = plt.figure()
# ax = fig.add_subplot(111)
# ax.set_xlim([0, 10])
# ax.set_ylim([0, 10])

# # t = np.arange(-2.0, 2.0, 0.001)
# # s = t ** 2
# # initial_text = "t ** 2"
# # l, = plt.plot(t, s, lw=2)

# def onclick(event):
#     # print('%s click: button=%d, x=%d, y=%d, xdata=%f, ydata=%f' %
#     #       ('double' if event.dblclick else 'single', event.button,
#     #        event.x, event.y, event.xdata, event.ydata))
#     plt.plot(event.xdata, event.ydata, 'ro')
#     fig.canvas.draw()

# # def submit(text):
# #     ydata = eval(text)
# #     l.set_ydata(ydata)
# #     ax.set_ylim(np.min(ydata), np.max(ydata))
# #     plt.draw()

# # axbox = plt.axes([0.1, 0.05, 0.8, 0.075])
# # text_box = TextBox(axbox, 'W1', initial="")
# # text_box.on_submit(submit)

# cid = fig.canvas.mpl_connect('button_press_event', onclick)
# plt.show()

# ===========================MATPLOT INPUT BOX==============================

# import numpy as np
# import matplotlib.pyplot as plt
# from matplotlib.widgets import TextBox

# fig, ax = plt.subplots()
# plt.subplots_adjust(bottom=0.2)
# t = np.arange(-2.0, 2.0, 0.001)
# s = t ** 2
# initial_text = "t ** 2"
# l, = plt.plot(t, s, lw=2)

# def submit(text):
#     ydata = eval(text)
#     l.set_ydata(ydata)
#     ax.set_ylim(np.min(ydata), np.max(ydata))
#     plt.draw()

# axbox = plt.axes([0.1, 0.05, 0.8, 0.075])
# text_box = TextBox(axbox, 'Evaluate', initial=initial_text)
# text_box.on_submit(submit)

# plt.show()

# ==========================TKINTER DRAG & DRAW==========================

# from tkinter import *

# canvas_width = 500
# canvas_height = 150

# def paint( event ):
#    python_green = "#476042"
#    x1, y1 = ( event.x - 1 ), ( event.y - 1 )
#    x2, y2 = ( event.x + 1 ), ( event.y + 1 )
#    w.create_oval( x1, y1, x2, y2, fill = python_green )

# master = Tk()
# master.title( "Painting using Ovals" )
# w = Canvas(master,
#            width=canvas_width,
#            height=canvas_height)
# w.pack(expand = YES, fill = BOTH)
# w.bind( "<B1-Motion>", paint )

# message = Label( master, text = "Press and Drag the mouse to draw" )
# message.pack( side = BOTTOM )

# mainloop()

# =====================POLYGON LINE CLICKABLE CHART=====================

# from matplotlib import pyplot as plt

# class LineBuilder:
#     def __init__(self, line):
#         self.line = line
#         self.xs = list(line.get_xdata())
#         self.ys = list(line.get_ydata())
#         self.cid = line.figure.canvas.mpl_connect('button_press_event', self)

#     def __call__(self, event):
#         print('click', event)
#         if event.inaxes!=self.line.axes: return
#         self.xs.append(event.xdata)
#         self.ys.append(event.ydata)
#         self.line.set_data(self.xs, self.ys)
#         self.line.figure.canvas.draw()

# fig = plt.figure()
# ax = fig.add_subplot(111)
# ax.set_title('click to build line segments')
# line, = ax.plot([0], [0])  # empty line
# linebuilder = LineBuilder(line)

# plt.show()

# =========== Cartesian plane tkinter ===========

# import tkinter as tk
# from PIL import Image, ImageTk

# root = tk.Tk()

# img_path = 'water-drop-splash.png'
# img = ImageTk.PhotoImage(Image.open(img_path).resize((400,400), Image.ANTIALIAS))

# canvas = tk.Canvas(root, height=400, width=400)
# canvas.create_image(200, 200, image=img)
# canvas.create_line(0, 200, 399, 200, dash=(2,2))  # x-axis
# canvas.create_line(200, 0, 200, 399, dash=(2,2))  # y-axis
# canvas.pack()

# root.mainloop()

# =========== tkinter form example ===========

# from tkinter import *
# class MyWindow:
#     def __init__(self, win):
#         self.lbl1=Label(win, text='First number')
#         self.lbl2=Label(win, text='Second number')
#         self.lbl3=Label(win, text='Result')
#         self.t1=Entry(bd=3)
#         self.t2=Entry()
#         self.t3=Entry()
#         self.btn1 = Button(win, text='Add')
#         self.btn2=Button(win, text='Subtract')
#         self.lbl1.place(x=100, y=50)
#         self.t1.place(x=200, y=50)
#         self.lbl2.place(x=100, y=100)
#         self.t2.place(x=200, y=100)
#         self.b1=Button(win, text='Add', command=self.add)
#         self.b2=Button(win, text='Subtract')
#         self.b2.bind('<Button-1>', self.sub)
#         self.b1.place(x=100, y=150)
#         self.b2.place(x=200, y=150)
#         self.lbl3.place(x=100, y=200)
#         self.t3.place(x=200, y=200)
#     def add(self):
#         self.t3.delete(0, 'end')
#         num1=int(self.t1.get())
#         num2=int(self.t2.get())
#         result=num1+num2
#         self.t3.insert(END, str(result))
#     def sub(self, event):
#         self.t3.delete(0, 'end')
#         num1=int(self.t1.get())
#         num2=int(self.t2.get())
#         result=num1-num2
#         self.t3.insert(END, str(result))

# window=Tk()
# mywin=MyWindow(window)
# window.title('Hello Python')
# window.geometry("400x300+10+10")
# window.mainloop()

# =============== embending matplot in tkinter ===============
