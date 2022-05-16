#Se importan librerias de trabajo
from tkinter import *
import tkinter as tk
from Interfaz_principal import Principal
from Interfaz_Cargar import Cargar
from Interfaz_Cargar import MostrarGrafo
from Interfaz_Aleatoria import Aleatoria



class APP(tk.Tk): 
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.title("Implementación Algoritmo A estrella")
        
        #Centrar la ventana
        ancho_ventana = 1000
        alto_ventana = 500
        x_ventana = self.winfo_screenwidth() // 2 - ancho_ventana // 2
        y_ventana = self.winfo_screenheight() // 2 - alto_ventana // 2
        posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
        self.geometry(posicion)
        self.resizable(0,0)
        
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        contenedor_principal = tk.Frame( self ,bg = "yellow")
        contenedor_principal.pack()
       
        #Menu de la ventana
        barraMenu=Menu(self)
        self.config(menu=barraMenu,width=300,height=300)
        creacionGrafo=Menu(barraMenu,tearoff=0)
        inicio=Menu(barraMenu,tearoff=0)
        inicio.add_command(label="Volver al Pricipal",command = lambda:self.show_frame( Principal ) )
        creacionGrafo.add_command(label="Cargar datos(nodos y relaciones)",command = lambda:self.show_frame( Cargar ))
        creacionGrafo.add_command(label="Aleatorio",command = lambda:self.show_frame( Aleatoria ))
        barraMenu.add_cascade(label="Inicio",menu=inicio)
        barraMenu.add_cascade(label="Creación del grafo",menu=creacionGrafo)
        
      
        
        self.show_frame( Principal )


    def show_frame(self,contenedor_llamado):
        contenedor_principal = tk.Frame( self ,bg = "yellow")
        frame = Principal(contenedor_principal,self)
        frame.tkraise()
    
    
    

root = APP()
root.mainloop()