import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style

import tkinter as tk
from tkinter import ttk
import numpy as np
from math import sqrt

LARGE_FONT= ("Verdana", 12)
style.use("ggplot")

class my_figure():
    def __init__(self):
        #self.f = plt(figsize=(5,5), dpi=100)
       self.f, self.a = plt.subplots(subplot_kw={'projection': 'polar'})
       self.a.set_rmax(2)
       self.a.set_rticks([1, 2, 3, 4,5,6])  # Less radial ticks
       self.a.set_rlabel_position(0)
       self.a.grid(True)
       self.a.set_title("Radar data on polar plot", va='bottom')

    def animate(self, i):
        pullData = open("radarData.txt","r").read()
        dataList = pullData.split('\n')
        xList = []
        yList = []
        zList = []
        velList = []
        angleList = []
        for eachLine in dataList:
            if len(eachLine) > 1:
                x, y, z, vel = eachLine.split(',')
                #print("x =",x, "y= ", float(y))
                xList.append(float(x))
                yList.append(float(y))
                zList.append(float(z))
                velList.append(float(vel))
                angleList.append(float(x)/sqrt(float(x)*float(x)+float(y)*float(y)))   
        dist = np.array(xList)
        angle = np.array(np.arccos(angleList)-np.deg2rad(45))
        
        #print("här är angle efter arcsin:" ,angle)
        self.a.clear()
        self.a.scatter(angle, dist)
        return self.a
    def get_f(self):
        return self.f
    
class SeaofBTCapp(tk.Tk):
    def __init__(self, *args, **kwargs):
        self.figure = my_figure()
        tk.Tk.__init__(self, *args, **kwargs)

        tk.Tk.iconbitmap(self)
        tk.Tk.wm_title(self, "Sea of BTC client")
        
        
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, PageOne, PageTwo, PageThree):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

    def update(self) -> None:
        self.frames[StartPage].update()
        self.figure.animate(1)
        return super().update()
    
'''    
class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Start Page", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button = ttk.Button(self, text="Visit Page 1",
                            command=lambda: controller.show_frame(PageOne))
        button.pack()

        button2 = ttk.Button(self, text="Visit Page 2",
                            command=lambda: controller.show_frame(PageTwo))
        button2.pack()

        button3 = ttk.Button(self, text="Graph Page",
                            command=lambda: controller.show_frame(PageThree))
        button3.pack()
'''

    
class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Graph Page!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Terminate",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        self.canvas = FigureCanvasTkAgg(controller.figure.get_f(), self)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2Tk(self.canvas, self)
        toolbar.update()
        self.canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    def update(self):
        self.canvas.draw()
        

class PageOne(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        '''
        label = tk.Label(self, text="Page One!!!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = ttk.Button(self, text="Page Two",
                            command=lambda: controller.show_frame(PageTwo))
        button2.pack()
        '''

class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        '''
        label = tk.Label(self, text="Page Two!!!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = ttk.Button(self, text="Page One",
                            command=lambda: controller.show_frame(PageOne))
        button2.pack()
         ''' 

class PageThree(tk.Frame):

    def __init__(self, parent, controller):
        
        tk.Frame.__init__(self, parent)
        '''
        label = tk.Label(self, text="Graph Page!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        self.canvas = FigureCanvasTkAgg(controller.figure.get_f(), self)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2Tk(self.canvas, self)
        toolbar.update()
        self.canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    def update(self):
        self.canvas.draw()
        '''