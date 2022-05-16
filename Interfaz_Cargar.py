from tkinter import *
from tkinter import messagebox
import tkinter as tk



#Se crea Frame_2 (similar a primera, pero con idioma ingles)
class Frame_2(tk.Frame):
    
    def __init__(self, parent):
        
        super().__init__(parent)

        self.entrada_usuario = tk.StringVar()

        self.pack(expand=True,fill="both")
        self.config(width="600",height="600")

        #Labels y cuadros de textos
        lbl1=Label(text="Ingrese la cantidad de NODOS:")
        lbl1.place(x=10,y=10)
        self.nodos=Entry()
        self.nodos.place(x=220,y=10)

        lbl2=Label(text="Ingrese la cantidad de RELACIONES:")
        lbl2.place(x=10,y=40)
        self.relaciones=Entry()
        self.relaciones.place(x=220,y=40)

        #Boton
        botonCreacion=Button(text="CREAR GRAFO",command=self.generarGrafo).place(x=10,y=70)
        
    def set_controller(self, controller):
        self.controller = controller
    
    def generarGrafo(self):
        if(self.nodos.get()=="" and self.relaciones.get()==""):
            messagebox.showwarning("Advertencia","Ingrese la cantidad de nodos y relaciones por favor")
        elif self.controller:
            self.controller.obtenerDatosGrafoAzar(self.nodos,self.relaciones)


