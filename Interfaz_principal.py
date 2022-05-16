from tkinter import *
import tkinter as tk

class Principal(tk.Frame):
    
    def __init__(self, container, controller,*args, **kwargs):
        
        super().__init__(container, *args, **kwargs)

        self.entrada_usuario = tk.StringVar()

        #Frames
        self.miFrame=Frame(self)
        self.miFrame.pack(expand=True,fill="x")
        self.miFrame.config(width="1000",height="500",bg="red")
        print("hello1")
        #Label
        self.lbl1=Label(self.miFrame,text="BIENVENIDO",font=("Comic Sans MS",28)).place(x=370,y=200)


    







