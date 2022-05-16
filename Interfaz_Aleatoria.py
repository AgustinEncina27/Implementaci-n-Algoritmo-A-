from tkinter import *
import tkinter as tk

class Aleatoria(tk.Frame):   
    def __init__(self, parent):
        
        super().__init__(parent)

        self.entrada_usuario = tk.StringVar()

        self.pack(expand=True,fill="both")
        self.config(width="600",height="600")

        #Label
        lbl1=Label(text="BIENVENIDO",font=("Comic Sans MS",64))
        lbl1.place(x=10,y=10)

    def set_controller(self, controller):
        self.controller = controller