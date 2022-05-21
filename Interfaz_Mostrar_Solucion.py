from tkinter import *
from tkinter import messagebox
import tkinter as tk
from pandas import DataFrame
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class Mostrar_Solucion(tk.Frame):
    
    def __init__(self, parent,controller):
        super().__init__(parent)
        ancho_ventana = 800
        alto_ventana = 500
        x_ventana = parent.winfo_screenwidth() // 2 - ancho_ventana // 2
        y_ventana = parent.winfo_screenheight() // 2 - alto_ventana // 2
        posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
        parent.geometry(posicion)
        parent.resizable(0,0)

        self.pack(expand=True,fill="both")
        self.config(width="600",height="600")

        #Boton
        self.botonSiguiente=Button(text="SIGUIENTE PASO",command=lambda:self.mostrarSolucionParcial(controller))
        self.botonSiguiente.place(x=340,y=440)
        self.botonSolucionFinal=Button(text="MOSTRAR SOLUCIÓN FINAL",command=lambda:[self.mostrarSolucionTotal(controller),self.botonSiguiente.place_forget()])
        self.botonSolucionFinal.place(x=50,y=440)
        
        
        controller.cargarDatosIniciales()
        controller.iniciarSolucionParcial()
        T = tk.Text(self, height = 30, width = 36)
        T.place(x=500,y=0)
        T.insert(tk.END, controller.mostrarTextoSolucion())
        f=controller.mostrarSolucionTotal()
        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().place(x=0,y=0)
       
    
    def set_controller(self, controller):
        self.controller = controller
    
    def mostrarSolucionTotal(self,controller):
        z=controller.iniciarSolucionTotal()
        if(z==0):
            self.botonSiguiente.place_forget()
            self.botonSolucionFinal.place_forget()
            messagebox.showwarning("Advertencia","Se encontró la solución")
            T = tk.Text(self, height = 30, width = 36)
            T.place(x=500,y=0)
            T.insert(tk.END, controller.mostrarTextoSolucion())
            f=controller.mostrarSolucionTotal()
            canvas = FigureCanvasTkAgg(f, self)
            canvas.draw()
            canvas.get_tk_widget().place(x=0,y=0)
        else:
            if(z==1):
                self.botonSiguiente.place_forget()
                self.botonSolucionFinal.place_forget()
                messagebox.showwarning("Advertencia","No se encontró la solución")
        
        


    def mostrarSolucionParcial(self,controller):
        z=controller.iniciarSolucionParcial()
        if(z==0):
            self.botonSiguiente.place_forget()
            self.botonSolucionFinal.place_forget()
            messagebox.showwarning("Advertencia","Se encontró la solución")
        else:
            if(z==2):
                messagebox.showwarning("Advertencia","No se encontró la solución")
            else:
                f=controller.mostrarSolucionTotal()
                canvas = FigureCanvasTkAgg(f, self)
                canvas.draw()
                canvas.get_tk_widget().place(x=0,y=0)
        T = tk.Text(self, height = 30, width = 36)
        T.place(x=500,y=0)
        T.insert(tk.END, controller.mostrarTextoSolucion())
            

