from tkinter import *
import tkinter as tk

class Principal(tk.Frame):
    #Constructor de Principal
    def __init__(self, parent):
        
        super().__init__(parent)
        ancho_ventana = 500
        alto_ventana = 500
        x_ventana = parent.winfo_screenwidth() // 2 - ancho_ventana // 2
        y_ventana = parent.winfo_screenheight() // 2 - alto_ventana // 2
        posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
        parent.geometry(posicion)
        parent.resizable(0,0)
        #Frames

        self.pack(expand=True,fill="x")
        self.config(width="500",height="500")
        #Label
        lbl1=Label(text="BIENVENIDO",font=("Comic Sans MS",28)).place(x=130,y=200)

    #Obtiene el controlador
    def set_controller(self, controller):
        self.controller = controller

    







