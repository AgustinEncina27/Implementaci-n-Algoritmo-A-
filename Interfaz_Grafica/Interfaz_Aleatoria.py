from tkinter import *
import tkinter as tk

class Frame_3(tk.Frame):   
    def __init__(self, container, controller,*args, **kwargs):
        
        super().__init__(container, *args, **kwargs)

        self.entrada_usuario = tk.StringVar()

        #Frames
        self.miFrame=Frame(self)
        self.miFrame.pack(expand=True,fill="both")
        self.miFrame.config(bg="green")
        self.miFrame.config(width="600",height="600")

        #Label
        self.lbl1=Label(self.miFrame,text="BIENVENIDO",font=("Comic Sans MS",64)).pack()
