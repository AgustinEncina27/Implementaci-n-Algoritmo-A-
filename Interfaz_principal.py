from tkinter import *
import tkinter as tk

class Principal(tk.Frame):
    #Constructor de Principal
    def __init__(self, parent):
        
        super().__init__(parent)
        ancho_ventana = 500
        alto_ventana = 500
        x_ventana = parent.winfo_screenwidth() // 2 - ancho_ventana // 2
        y_ventana = parent.winfo_screenheight() // 2 - alto_ventana // 2
        posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
        parent.geometry(posicion)
        parent.resizable(0,0)
        #Frames

        self.pack(expand=True,fill="x")
        self.config(width="500",height="500")
        #Label
        lbl1=Label(text="BIENVENIDO",font=("Comic Sans MS",28)).place(x=130,y=5)
        lbl2=Label(justify=LEFT,text="""Guía del usuario:\n 
        En la esquina superior izquierda se encuentra el menu con las distintas funcionalidades\n
        que posee esta aplicación.\n
        1- Pestaña de "Inicio".\n
            Contiene la opción "Volver al Principal" para volver a la pestaña principal(Actual).\n
        2- Pestaña de "Creación del Grafo":\n
            Contine dos opciones.\n
                2.a- Cargar datos(nodos y costo de relaciones):\n
                    Podemos crear un grafo indicando las relaciones con los nodos y sus costos.\n
                2.b- Aleatorio:\n
                    Indicas la cantidad de nodos y relaciones para crear un grafo aleatorio con las\n
                    caracteristicas indicadas.""").place(x=0,y=80)

    #Obtiene el controlador
    def set_controller(self, controller):
        self.controller = controller

    







