from tkinter import *
from tkinter import messagebox
import tkinter as tk



#Se crea Frame_2 (similar a primera, pero con idioma ingles)
class Frame_2(tk.Frame):
    
    def __init__(self, container,controller,*args, **kwargs):
        
        super().__init__(container, *args, **kwargs)

        self.entrada_usuario = tk.StringVar()
        #Frames
        self.miFrame1=Frame(self)
        self.miFrame1.pack(expand=True,fill="x")
        self.miFrame1.config(bg="green")
        self.miFrame1.config(width="900",height="110")

        self.miFrame2=Frame(self)
        self.miFrame2.pack(expand=True,fill="both")
        self.miFrame2.config(bg="red")
        self.miFrame2.config(width="900",height="640")

        self.miFrame3=Frame(self)
        self.miFrame3.pack(expand=True,fill="both")
        self.miFrame3.config(bg="blue")
        self.miFrame3.config(width="900",height="250")

        #Labels y cuadros de textos
        lbl1=Label(self.miFrame1,text="Ingrese la cantidad de NODOS:")
        lbl1.place(x=10,y=10)
        self.nodos=Entry(self.miFrame1)
        self.nodos.place(x=220,y=10)

        lbl2=Label(self.miFrame1,text="Ingrese la cantidad de RELACIONES:")
        lbl2.place(x=10,y=40)
        self.relaciones=Entry(self.miFrame1)
        self.relaciones.place(x=220,y=40)

        #Boton
        botonCreacion=Button(self.miFrame1,text="CREAR GRAFO",command=self.CrearGrafo).place(x=10,y=70)

    def CrearGrafo(self):
        if(self.nodos.get()=="" and self.relaciones.get()==""):
            messagebox.showwarning("Advertencia","Ingrese la cantidad de nodos y relaciones por favor")   