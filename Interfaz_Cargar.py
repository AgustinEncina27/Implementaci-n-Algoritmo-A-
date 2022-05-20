from tkinter import *
from tkinter import messagebox
import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class Cargar(tk.Frame):
    def __init__(self, parent,controller):
        super().__init__(parent)
        controller.LimpiarGrafo()
        ancho_ventana = 500
        alto_ventana = 600
        x_ventana = parent.winfo_screenwidth() // 2 - ancho_ventana // 2
        y_ventana = parent.winfo_screenheight() // 2 - alto_ventana // 2
        posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
        parent.geometry(posicion)
        parent.resizable(0,0)

        self.pack(expand=True,fill="both")
        self.config(width="600",height="600")

        #Labels y cuadros de textos
        lbl0=Label(text="APARTADO PARA CREAR RELACIONES")
        lbl0.place(x=170,y=10)
        lbl1=Label(text="Ingrese el NODO 1:")
        lbl1.place(x=5,y=40)
        self.nodo1=Entry()
        self.nodo1.place(x=170,y=40)

        lbl2=Label(text="Ingrese el NODO 2:")
        lbl2.place(x=5,y=70)
        self.nodo2=Entry()
        self.nodo2.place(x=170,y=70)

        lbl2=Label(text="Ingresar PESO de la relación:")
        lbl2.place(x=5,y=100)
        self.relaciones=Entry()
        self.relaciones.place(x=170,y=100)

        lbl3=Label(text="Ingrese el NODO INICIAL:")
        self.inicial=Entry()

        lbl4=Label(text="Ingresar el NODO FINAL:")
        self.final=Entry()
        
        #Botones
        botonCreacion=Button(text="CREAR RELACIÓN",command=lambda:self.CargarGrafo(lbl3,self.inicial,lbl4,self.final,botonMostrar)).place(x=330,y=70)

        botonMostrar=Button(text="MOSTRAR SOLUCIÓN",command=lambda:self.MostrarSolucion(parent))

        
    def set_controller(self, controller):
        self.controller = controller
    
    def CargarGrafo(self,lbl3,inicial,lbl4,final,botonMostrar): 
        nodo1=self.nodo1.get()
        nodo2=self.nodo2.get()
        relaciones=self.relaciones.get()
        if(str(nodo1)=="" or str(nodo2)=="" or str(relaciones)==""):
            messagebox.showwarning("Advertencia","Ingrese los NODOS A RELACIONAR y el PESO por favor")
        elif self.controller:
            f=self.controller.CargarDatosGrafo(int(nodo1),int(nodo2),int(relaciones))
            canvas = FigureCanvasTkAgg(f, self)
            canvas.get_tk_widget().place(x=0,y=130)
            
            lbl3.place(x=5,y=500)
            inicial.place(x=170,y=500)
            lbl4.place(x=5,y=530)
            final.place(x=170,y=530)
            botonMostrar.place(x=200,y=560)
    
    def MostrarSolucion(self,parent): 
        inicial=self.inicial.get()
        final=self.final.get()
        if(inicial=="" or final==""):
            messagebox.showwarning("Advertencia","Ingrese el NODO INICIAL y el NODO FINAL por favor")
        elif self.controller:
            self.controller.CargarElGrafoEnRegistros(int(inicial),int(final))
            parent.mostrarFrameMostrar_Solucion()

                
                

            