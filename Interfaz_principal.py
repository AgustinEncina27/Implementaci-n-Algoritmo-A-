from tkinter import *
import tkinter as tk

class Principal(tk.Frame):
    
    def __init__(self, parent):
        
        super().__init__(parent)

        self.entrada_usuario = tk.StringVar()

        #Frames

        self.pack(expand=True,fill="x")
        self.config(width="1000",height="500")
        #Label
        lbl1=Label(text="BIENVENIDO",font=("Comic Sans MS",28)).place(x=370,y=200)

    def set_controller(self, controller):
        self.controller = controller

    







