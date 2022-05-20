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
        botonSiguiente=Button(text="SIGUIENTE PASO",command=lambda:self.mostrarSolucionParcial(parent,controller))
        botonSiguiente.place(x=340,y=440)
        botonSolucionFinal=Button(text="MOSTRAR SOLUCIÓN FINAL",command=lambda:[self.mostrarSolucionTotal(parent,controller),botonSiguiente.place_forget(),botonSolucionFinal.place_forget()])
        botonSolucionFinal.place(x=50,y=440)
        
        controller.iniciarSolucion()
        
       
    
    def set_controller(self, controller):
        self.controller = controller
    
    def mostrarSolucionTotal(self,parent,controller):
        ancho_ventana = 800
        alto_ventana = 500
        x_ventana = parent.winfo_screenwidth() // 2 - ancho_ventana // 2
        y_ventana = parent.winfo_screenheight() // 2 - alto_ventana // 2
        posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
        parent.geometry(posicion)
        parent.resizable(0,0)
        T = tk.Text(self, height = 30, width = 36)
        T.place(x=500,y=0)
        T.insert(tk.END, controller.mostrarTextoSolucion())
        f=controller.mostrarSolucionTotal()
        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().place(x=0,y=0)


    def mostrarSolucionParcial(self,parent,controller):
        ancho_ventana = 700
        alto_ventana = 500
        x_ventana = parent.winfo_screenwidth() // 2 - ancho_ventana // 2
        y_ventana = parent.winfo_screenheight() // 2 - alto_ventana // 2
        posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
        parent.geometry(posicion)
        parent.resizable(0,0)
