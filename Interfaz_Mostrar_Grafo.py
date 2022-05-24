from tkinter import *
from tkinter import messagebox
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class Mostrar_Grafo(tk.Frame):
    #Constructor de Mostrar_Grafo
    def __init__(self, parent,controller):
        super().__init__(parent)
        controller.LimpiarGrafo()
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
        lbl1=Label(text="Indicar el NODO INICIAL:")
        lbl1.place(x=50,y=410)
        self.nodos=Entry()
        self.nodos.place(x=300,y=410)
        #300
        lbl2=Label(text="Indicar el NODO FINAL:")
        lbl2.place(x=50,y=440)
        self.relaciones=Entry()
        self.relaciones.place(x=300,y=440)
        #Boton
        botonCreacion=Button(text="MOSTRAR SOLUCIÓN",command=lambda:self.generarGrafo(parent,controller)).place(x=170,y=465)
        
        f=controller.obtenerDatosGrafoCargar()
        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().pack(anchor=N)
       
    #Obtiene el controlador
    def set_controller(self, controller):
        self.controller = controller
    
    #Carga los nodos iniciales y finales para luego utilizarlos para mostrar la solución
    def generarGrafo(self,parent,controller):
        inicial=self.nodos.get()
        final=self.relaciones.get()
        if(not(controller.busquedaDeNodo(int(inicial))) or not(controller.busquedaDeNodo(int(final)))):
            messagebox.showwarning("Advertencia","El nodo inicial o final ingresados no se encuentran en el grafo")
        else:
            if(not(inicial.isdecimal()) or not(final.isdecimal())):
                messagebox.showwarning("Advertencia","Por favor ingresar solo números enteros")
            else:
                if(inicial=="" or final==""):
                    messagebox.showwarning("Advertencia","Ingrese el NODO INICIAL y el NODO FINAL por favor")
                else:
                    if(int(inicial)==int(final)):
                        messagebox.showwarning("Advertencia","Usted ya se encuentra en el nodo objetivo")
                    elif self.controller:
                        self.controller.CargarElGrafoEnRegistros(int(inicial),int(final))
                        parent.mostrarFrameMostrar_Solucion()
        
            