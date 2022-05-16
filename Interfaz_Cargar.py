from tkinter import *
from tkinter import messagebox
import tkinter as tk
from Grafica_Grafo import CrearGraficoCarga


#Se crea Frame_2 (similar a primera, pero con idioma ingles)
class Cargar(tk.Frame):
    def __init__(self, container,controller,*args, **kwargs):
        
        super().__init__(container, *args, **kwargs)

        self.entrada_usuario = tk.StringVar()
        #Frames
        self.miFrame1=Frame(self)
        self.miFrame1.pack(expand=True,fill="x")
        self.miFrame1.config(width="1000",height="500",bg="red")
        #Labels y cuadros de textos
        lbl1=Label(self.miFrame1,text="Ingrese la cantidad de NODOS:")
        lbl1.place(x=50,y=170)
        self.nodos=Entry(self.miFrame1)
        self.nodos.place(x=260,y=170)

        lbl2=Label(self.miFrame1,text="Ingrese la cantidad de RELACIONES:")
        lbl2.place(x=50,y=200)
        self.relaciones=Entry(self.miFrame1)
        self.relaciones.place(x=260,y=200)

        #Boton
        botonCreacion=Button(self.miFrame1,text="CREAR GRAFO",command=lambda:self.CrearGrafo(controller)).place(x=190,y=240)

    def CrearGrafo(self,controller):
        if(self.nodos.get()=="" and self.relaciones.get()==""):
            messagebox.showwarning("Advertencia","Ingrese la cantidad de nodos y relaciones por favor")   
        else:
            a=int(self.nodos.get())
            b=int(self.relaciones.get())
            CrearGraficoCarga(a,b)
            controller.show_frame(MostrarGrafo)

class MostrarGrafo(tk.Frame):
    
    def __init__(self, container,controller,*args, **kwargs):
        super().__init__(container, *args, **kwargs)
        self.entrada_usuario = tk.StringVar()
        #Frames    
        self.miFrame2=Frame(self)
        self.miFrame2.pack(expand=True,fill="x")
        self.miFrame2.config(width="500",height="400",bg="red")
        self.miFrame3=Frame(self)
        self.miFrame3.pack(expand=True,fill="x")
        self.miFrame3.config(width="500",height="400",bg="red")

        self.miFrame1=Frame(self)
        self.miFrame1.pack(expand=True,fill="x")
        self.miFrame1.config(width="1000",height="100",bg="green")
        

        #Boton
        botonCreacion=Button(self.miFrame1,text="CREAR GRAFO").pack


