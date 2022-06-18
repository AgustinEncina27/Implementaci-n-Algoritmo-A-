from tkinter import *
from tkinter import messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from Interfaz_Agregar_Relacion import *
from Interfaz_Agregar_Nodo import *
from Interfaz_Eliminar_Nodo import *
from Interfaz_Eliminar_Relacion import *
from Interfaz_Modificar_Costo import *

class Editar_Grafo(Frame):
    def __init__(self, parent,controller):
        super().__init__(parent)
        ancho_ventana = 750
        alto_ventana = 500
        x_ventana = parent.winfo_screenwidth() // 2 - ancho_ventana // 2
        y_ventana = parent.winfo_screenheight() // 2 - alto_ventana // 2
        posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
        parent.geometry(posicion)
        parent.resizable(0,0)

        self.pack(expand=True,fill="both")
        self.config(width="600",height="600")

        self.botonAgregarRelacion=Button(text="AGREGAR RELACION", command=lambda:Agregar_Relacion(controller,master=self))
        self.botonAgregarRelacion.place(x=20,y=20)
        self.botonAgregarNodo=Button(text="AGREGAR NODO", command=lambda:Agregar_Nodo(controller,master=self))
        self.botonAgregarNodo.place(x=150,y=20)
        self.botonEliminarNodo=Button(text="ELIMINAR NODO", command=lambda:Eliminar_Nodo(controller,master=self))
        self.botonEliminarNodo.place(x=265,y=20)
        self.botonEliminarRelacion=Button(text="ELIMINAR RELACION", command=lambda:Eliminar_Relacion(controller, master=self))
        self.botonEliminarRelacion.place(x=380,y=20)
        self.botonModificarCostoDeRelacion = Button(text="MODIFICAR COSTO", command=lambda:Modificar_Costo_Relacion(controller, master=self))
        self.botonModificarCostoDeRelacion.place(x=520,y=20)

        f=controller.getFigura()
        canvas1 = FigureCanvasTkAgg(f, self)
        canvas1.draw()
        canvas1.get_tk_widget().place(x=5,y=60)

    def set_controller(self, controller):
        self.controller = controller

    def refrescarFigura(self):
        f=self.controller.getFigura()
        canvas1 = FigureCanvasTkAgg(f, self)
        canvas1.draw()
        canvas1.get_tk_widget().place(x=-15,y=60)
