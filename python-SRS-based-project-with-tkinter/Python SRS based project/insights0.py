# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 05:50:12 2020

@author: UPMANYU JHA
"""

from tkinter import*
from tkinter import ttk
import tkinter
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure




root=Tk()
root.iconbitmap("C:/Users/UPMANYU JHA/Desktop/Python SRS based project(Internship)/images/ag47f-whoaa-001.ico") #where ever any saves this folder plz make a not to change its addres accordingly

class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("SRS INSIGHTS WINDOW")
        self.root.geometry("415x415+535+250")
       
        
       
        
       #======Instights Frame=======
        frame1=Frame(self.root,bg="white")
        frame1.place(x=0,y=0,width=415,height=415)
        
        
        titel=Label(frame1,text="INSIGHTS HOME PAGE",font=("times new roman",25,"bold"),bd=12,relief=GROOVE,bg="#F0FFFF" ,fg="green",pady=2, padx=2).pack(fill=X)

        btn1_register=Button(frame1, text="A",cursor="hand2",command=self.graph_a,font=("arial",14,"bold"),bg="#32CD32",fg="white").place(x=40,y=90,width=150,height=35)
        btn2_cancle=Button(frame1, text="B",cursor="hand2",command=self.graph_b,font=("arial",14,"bold"),bg="red",fg="white").place(x=225,y=90,width=150,height=35)
        btn3_read=Button(frame1, text="C",cursor="hand2",command=self.graph_c,font=("arial",14,"bold"),bg="gray",fg="black").place(x=40,y=170,width=150,height=35)
        btn4=Button(frame1, text="D",cursor="hand2",command=self.graph_d,font=("arial",14,"bold"),bg="#FF8C00",fg="white").place(x=225,y=170,width=150,height=35)
        btn5=Button(frame1, text="E",cursor="hand2",command=self.graph_e,font=("arial",14,"bold"),bg="#DCDCDC",fg="black").place(x=40,y=250,width=150,height=35)
        btn6=Button(frame1, text="F",cursor="hand2",command=self.graph_f,font=("arial",14,"bold"),bg="#FF8C00",fg="white").place(x=225,y=250,width=150,height=35)
        btn7=Button(frame1, text="G",cursor="hand2",command=self.graph_g,font=("arial",14,"bold"),bg="#DCDCDC",fg="black").place(x=131,y=330,width=150,height=35)
        
        
    def graph_a(self):
        root = tkinter.Tk()
        root.wm_title("Embedding in Tk")
        
        fig = Figure(figsize=(5, 4), dpi=100)
        t = np.arange(0, 3, .01)
        fig.add_subplot(111).plot(t, 2 * np.sin(2 * np.pi * t))
        
        canvas = FigureCanvasTkAgg(fig, master=root)  # A tk.DrawingArea.
        canvas.draw()
        canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
        
        toolbar = NavigationToolbar2Tk(canvas, root)
        toolbar.update()
        canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)


        def on_key_press(event):
            print("you pressed {}".format(event.key))
            key_press_handler(event, canvas, toolbar)
        
        
        canvas.mpl_connect("key_press_event", on_key_press)
        
        
        def _quit():
            root.quit()     # stops mainloop
            root.destroy()  # this is necessary on Windows to prevent
                            # Fatal Python Error: PyEval_RestoreThread: NULL tstate
        
        
        button = tkinter.Button(master=root, text="Quit", command=_quit)
        button.pack(side=tkinter.BOTTOM)
        
        tkinter.mainloop()
        # If you put root.destroy() here, it will cause an error if the window is
        # closed with the window manager.
                
    def graph_b(self):
        root = tkinter.Tk()
        root.wm_title("Embedding in Tk")
        
        fig = Figure(figsize=(5, 4), dpi=100)
        t = np.arange(0, 3, .01)
        fig.add_subplot(111).plot(t, 2 * np.sin(2 * np.pi * t))
        
        canvas = FigureCanvasTkAgg(fig, master=root)  # A tk.DrawingArea.
        canvas.draw()
        canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
        
        toolbar = NavigationToolbar2Tk(canvas, root)
        toolbar.update()
        canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)


        def on_key_press(event):
            print("you pressed {}".format(event.key))
            key_press_handler(event, canvas, toolbar)
        
        
        canvas.mpl_connect("key_press_event", on_key_press)
        
        
        def _quit():
            root.quit()     # stops mainloop
            root.destroy()  # this is necessary on Windows to prevent
                            # Fatal Python Error: PyEval_RestoreThread: NULL tstate
        
        
        button = tkinter.Button(master=root, text="Quit", command=_quit)
        button.pack(side=tkinter.BOTTOM)
        
        tkinter.mainloop()
        # If you put root.destroy() here, it will cause an error if the window is
        # closed with the window manager.
                
        
    def graph_c(self):
        root = tkinter.Tk()
        root.wm_title("Embedding in Tk")
        
        fig = Figure(figsize=(5, 4), dpi=100)
        t = np.arange(0, 3, .01)
        fig.add_subplot(111).plot(t, 2 * np.sin(2 * np.pi * t))
        
        canvas = FigureCanvasTkAgg(fig, master=root)  # A tk.DrawingArea.
        canvas.draw()
        canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
        
        toolbar = NavigationToolbar2Tk(canvas, root)
        toolbar.update()
        canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)


        def on_key_press(event):
            print("you pressed {}".format(event.key))
            key_press_handler(event, canvas, toolbar)
        
        
        canvas.mpl_connect("key_press_event", on_key_press)
        
        
        def _quit():
            root.quit()     # stops mainloop
            root.destroy()  # this is necessary on Windows to prevent
                            # Fatal Python Error: PyEval_RestoreThread: NULL tstate
        
        
        button = tkinter.Button(master=root, text="Quit", command=_quit)
        button.pack(side=tkinter.BOTTOM)
        
        tkinter.mainloop()
        # If you put root.destroy() here, it will cause an error if the window is
        # closed with the window manager.
                
        
    def graph_d(self):
        root = tkinter.Tk()
        root.wm_title("Embedding in Tk")
        
        fig = Figure(figsize=(5, 4), dpi=100)
        t = np.arange(0, 3, .01)
        fig.add_subplot(111).plot(t, 2 * np.sin(2 * np.pi * t))
        
        canvas = FigureCanvasTkAgg(fig, master=root)  # A tk.DrawingArea.
        canvas.draw()
        canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
        
        toolbar = NavigationToolbar2Tk(canvas, root)
        toolbar.update()
        canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)


        def on_key_press(event):
            print("you pressed {}".format(event.key))
            key_press_handler(event, canvas, toolbar)
        
        
        canvas.mpl_connect("key_press_event", on_key_press)
        
        
        def _quit():
            root.quit()     # stops mainloop
            root.destroy()  # this is necessary on Windows to prevent
                            # Fatal Python Error: PyEval_RestoreThread: NULL tstate
        
        
        button = tkinter.Button(master=root, text="Quit", command=_quit)
        button.pack(side=tkinter.BOTTOM)
        
        tkinter.mainloop()
        # If you put root.destroy() here, it will cause an error if the window is
        # closed with the window manager.
                
        
    def graph_e(self):
        root = tkinter.Tk()
        root.wm_title("Embedding in Tk")
        
        fig = Figure(figsize=(5, 4), dpi=100)
        t = np.arange(0, 3, .01)
        fig.add_subplot(111).plot(t, 2 * np.sin(2 * np.pi * t))
        
        canvas = FigureCanvasTkAgg(fig, master=root)  # A tk.DrawingArea.
        canvas.draw()
        canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
        
        toolbar = NavigationToolbar2Tk(canvas, root)
        toolbar.update()
        canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)


        def on_key_press(event):
            print("you pressed {}".format(event.key))
            key_press_handler(event, canvas, toolbar)
        
        
        canvas.mpl_connect("key_press_event", on_key_press)
        
        
        def _quit():
            root.quit()     # stops mainloop
            root.destroy()  # this is necessary on Windows to prevent
                            # Fatal Python Error: PyEval_RestoreThread: NULL tstate
        
        
        button = tkinter.Button(master=root, text="Quit", command=_quit)
        button.pack(side=tkinter.BOTTOM)
        
        tkinter.mainloop()
        # If you put root.destroy() here, it will cause an error if the window is
        # closed with the window manager.
                
    def graph_f(self):
        root = tkinter.Tk()
        root.wm_title("Embedding in Tk")
        
        fig = Figure(figsize=(5, 4), dpi=100)
        t = np.arange(0, 3, .01)
        fig.add_subplot(111).plot(t, 2 * np.sin(2 * np.pi * t))
        
        canvas = FigureCanvasTkAgg(fig, master=root)  # A tk.DrawingArea.
        canvas.draw()
        canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
        
        toolbar = NavigationToolbar2Tk(canvas, root)
        toolbar.update()
        canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)


        def on_key_press(event):
            print("you pressed {}".format(event.key))
            key_press_handler(event, canvas, toolbar)
        
        
        canvas.mpl_connect("key_press_event", on_key_press)
        
        
        def _quit():
            root.quit()     # stops mainloop
            root.destroy()  # this is necessary on Windows to prevent
                            # Fatal Python Error: PyEval_RestoreThread: NULL tstate
        
        
        button = tkinter.Button(master=root, text="Quit", command=_quit)
        button.pack(side=tkinter.BOTTOM)
        
        tkinter.mainloop()
        # If you put root.destroy() here, it will cause an error if the window is
        # closed with the window manager.
                
    def graph_g(self):
        import tkinter

        from matplotlib.backends.backend_tkagg import (
            FigureCanvasTkAgg, NavigationToolbar2Tk)
        # Implement the default Matplotlib key bindings.
        from matplotlib.backend_bases import key_press_handler
        from matplotlib.figure import Figure
        
        import numpy as np
        
        
        root = tkinter.Tk()
        root.wm_title("Embedding in Tk")
        
        fig = Figure(figsize=(5, 4), dpi=100)
        t = np.arange(0, 3, .01)
        fig.add_subplot(111).plot(t, 2 * np.sin(2 * np.pi * t))
        
        canvas = FigureCanvasTkAgg(fig, master=root)  # A tk.DrawingArea.
        canvas.draw()
        canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
        
        toolbar = NavigationToolbar2Tk(canvas, root)
        toolbar.update()
        canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)


        def on_key_press(event):
            print("you pressed {}".format(event.key))
            key_press_handler(event, canvas, toolbar)
        
        
        canvas.mpl_connect("key_press_event", on_key_press)
        
        
        def _quit():
            root.quit()     # stops mainloop
            root.destroy()  # this is necessary on Windows to prevent
                            # Fatal Python Error: PyEval_RestoreThread: NULL tstate
        
        
        button = tkinter.Button(master=root, text="Quit", command=_quit)
        button.pack(side=tkinter.BOTTOM)
        
        tkinter.mainloop()
        # If you put root.destroy() here, it will cause an error if the window is
        # closed with the window manager.
                
        

obj=Register(root)
root.mainloop()