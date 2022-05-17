from tkinter import *
from tkinter import messagebox
import tkinter as tk

class Cargar(tk.Frame):
    
    def __init__(self, parent):
        
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

        #Labels y cuadros de textos
        lbl1=Label(text="Ingrese la cantidad de NODOS:")
        lbl1.place(x=50,y=170)
        self.nodos=Entry()
        self.nodos.place(x=300,y=170)

        lbl2=Label(text="Ingrese la cantidad de RELACIONES:")
        lbl2.place(x=50,y=200)
        self.relaciones=Entry()
        self.relaciones.place(x=300,y=200)

        #Boton
        botonCreacion=Button(text="CREAR GRAFO",command=lambda:self.CargarGrafo(parent)).place(x=200,y=250)
        
    def set_controller(self, controller):
        self.controller = controller
    
    def CargarGrafo(self,parent):
        a=int(self.nodos.get())
        h=int(self.relaciones.get())
        b=0
        for c in range(a+1):
            acum=c
            if(c!=0): 
                b+=acum-1   
        if(self.nodos.get()=="" and self.relaciones.get()==""):
            messagebox.showwarning("Advertencia","Ingrese la cantidad de nodos y relaciones por favor")
        else:
            if(h>b):
                messagebox.showwarning("Advertencia","Por favor ingrese el rango permitido[1,"+str(b)+"]")
            elif self.controller:
                self.controller.CargarDatosGrafoAzar(int(self.nodos.get()),int(self.relaciones.get()))
                parent.mostrarFrameMostrar_Grafo()
            