import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
from public_func import *
import tkinter as tk
from tkinter import ttk
import numpy as np
from math import pi, acos, asin, sqrt


LARGE_FONT= ("Verdana", 12)
style.use("ggplot")
class my_figure():
    '''
    my_figure is a polar-plot figure that can represent the data from the mqtt client.
    '''
    def __init__(self):
        '''
        Constructs a new 'my_figure' object.
        Initializes it as a polar plot and updates the settings.

        :return: Returns nothing.
        '''
        self.f, self.a = plt.subplots(subplot_kw={'projection': 'polar'})
        self.a.set_rmax(2)
        self.a.set_rticks([1, 2, 3, 4,5,6])  # Less radial ticks
        self.a.set_rlabel_position(0)
        self.a.grid(True)
        self.a.set_title("Radar data on polar plot", va='bottom')
   
    def animate(self, i):
        '''
        The animate function extracts all the information from the specified textfile.
        It uses the data to put points on the polar plot. If the target is an updated one, it draws arrows from the old location to the new.

        :return: Returns nothing.
        '''
        pullData = open("radarData.txt","r").read()
        dataList = pullData.split('\n')
        xList = []
        yList = []
        zList = []
        velList = []
        angleList = []
        distList = []
        old_angle_list = []
        old_r_list = []
        for eachLine in dataList:
            if len(eachLine) > 1:
                x, y, z, vel, old_angle, old_r = eachLine.split(',')
                #print("Old angle: ", old_angle, "old radius:", old_r)
                xList.append(float(x))
                yList.append(float(y))
                zList.append(float(z))
                velList.append(float(vel))
                old_angle_list.append(float(old_angle)-np.deg2rad(45))
                old_r_list.append(float(old_r))
                angle, dist = extract_angle_and_dist(float(x), float(y))
                angleList.append(angle-np.deg2rad(45))
                distList.append(dist)
                

        dist = np.array(distList)
        angle = np.array(angleList)
        self.a.clear()
        self.a.scatter(angle, dist)
        #xy = (old target angle, old target radius)
        #xytext = (new target angle, new target radius)
        #print(old_angle_list)
        #print(old_r_list)
        #print(angleList)
        #print(distList)
        for a in range(len(old_angle_list)):
            if float(old_angle_list[a]) != 0 and float(old_r_list[a]) != 0:
                self.a.annotate("",
                    xytext=(old_angle_list[a], old_r_list[a]),
                    xy=(angleList[a],distList[a]),
                    xycoords='data',
                    arrowprops=dict(facecolor='red', shrink=0.05),
                    )
        
         #Sets the height of the target besides teh point
        for a in range(len(zList)):
            self.a.annotate(zList[a], (angle[a], dist[a]))
        
        return self.a
    def get_f(self):
        return self.f
    

    #TODO move extraction of targets here
    def extract_targets(self):
        pass

class gui(tk.Tk):
    '''
    gui is a graphical user interface that holds a my_figure and a button to terminate.
    The class inherits from tkinter.
    '''
    def __init__(self, *args, **kwargs):
        '''
        Constructs a new 'gui' and 'my_figure' object. The function proceds to create the buttons and pages for the whole gui.

        :return: Returns nothing.
        '''
        self.figure = my_figure()
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.iconbitmap(self)
        tk.Tk.wm_title(self, "Radar Reconnaissance Robot")
       # tk.Tk.wm_attributes("-fullscreen",True)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)
        
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, PageOne):
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        '''
        Function to show the specified frame.

        :return: Returns nothing.
        '''
        frame = self.frames[cont]
        frame.tkraise()

    def update(self) -> None:
        '''
        Function to update the polar plot. Needs to be called after each new data entry or change.
        '''
        self.frames[StartPage].update()
        self.figure.animate(1)
        return super().update()
    
class StartPage(tk.Frame):
    '''
    StartPage encapsulates the polar plot and a button to terminate the system.
    The class inherits from tkinter Frame.
    '''
    def __init__(self, parent, controller):
        '''
        Constructs a new 'StartPage' object including a terminate button and graph.

        :return: Returns nothing.
        '''
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
        '''
        Function to update the canvas contained in the class.

        :return: Returns nothing.
        '''
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
