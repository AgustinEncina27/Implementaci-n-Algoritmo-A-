from tkinter import *
from tkinter import messagebox
import tkinter as tk

class Aleatoria(tk.Frame):   
    
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
        c=controller.datosAleatorios()
        #Labels y cuadros de textos
        lbl1=Label(text="Nodos Generados:              "+str(c[0]))
        lbl1.place(x=150,y=170)

        lbl2=Label(text="Relaciones Generadas:         "+str(c[1]))
        lbl2.place(x=150,y=200)

        #Boton
        botonCreacion=Button(text="CREAR GRAFO",command=lambda:self.CargarGrafo(parent,c)).place(x=200,y=250)
        
    def set_controller(self, controller):
        self.controller = controller
    
    def CargarGrafo(self,parent,c):
        self.controller.CargarDatosGrafoAzar(c[0],c[1])
        parent.mostrarFrameMostrar_Grafo()