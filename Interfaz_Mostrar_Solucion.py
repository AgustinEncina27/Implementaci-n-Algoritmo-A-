from tkinter import *
from tkinter import messagebox
import tkinter as tk
from pandas import DataFrame
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class Mostrar_Solucion(tk.Frame):
    
    def __init__(self, parent,controller):
        super().__init__(parent)
        ancho_ventana = 500
        alto_ventana = 500
        x_ventana = parent.winfo_screenwidth() // 2 - ancho_ventana // 2
        y_ventana = parent.winfo_screenheight() // 2 - alto_ventana // 2
        posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
        parent.geometry(posicion)
        parent.resizable(0,0)

        self.pack(expand=True,fill="both")
        self.config(width="600",height="600")

        #Boton
        botonCreacion=Button(text="MOSTRAR SOLUCIÓN FINAL").place(x=50,y=440)
        botonCreacion=Button(text="SIGUIENTE PASO").place(x=340,y=440)
        
        #f=controller.obtenerDatosGrafoCargar()
        #canvas = FigureCanvasTkAgg(f, self)
        #canvas.draw()
        #canvas.get_tk_widget().pack(anchor=N)
       
    
    def set_controller(self, controller):
        self.controller = controller
    
    def generarGrafo(self):
        messagebox.showwarning("Advertencia","Ingrese la cantidad de nodos y relaciones por favor")