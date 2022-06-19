from tkinter import *
from tkinter import messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from Interfaz_Agregar_Relacion import *
from Interfaz_Agregar_Nodo import *
from Interfaz_Eliminar_Nodo import *
from Interfaz_Eliminar_Relacion import *
from Interfaz_Modificar_Costo import *
from Interfaz_Cambiar_Final import *
from Interfaz_Cambiar_Inicial import *

class Editar_Grafo(Frame):
    def __init__(self, parent,controller):
        super().__init__(parent)
        ancho_ventana = 900
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
        self.botonCambiarInicial = Button(text="CAMBIAR INICIAL", command=lambda:Cambiar_Nodo_Inicial(controller, master=self))
        self.botonCambiarInicial.place(x=650,y=20)
        self.botonCambiarFinal = Button(text="CAMBIAR FINAL", command=lambda:Cambiar_Nodo_Final(controller, master=self))
        self.botonCambiarFinal.place(x=780,y=20)
        self.botonVolverPantallaAnterior = Button(text="VOLVER", command=lambda:self.volverPantallaAnterior(parent, controller))
        self.botonVolverPantallaAnterior.place(x=265,y=450)

        self.f=controller.getFigura()
        self.canvas1 = FigureCanvasTkAgg(self.f, self)
        self.canvas1.draw()
        self.canvas1.get_tk_widget().place(x=230,y=60)

    def set_controller(self, controller):
        self.controller = controller

    def refrescarFigura(self,controller):
        self.f=controller.getFigura()
        self.canvas1 = FigureCanvasTkAgg(self.f, self)
        self.canvas1.draw()
        self.canvas1.get_tk_widget().place(x=230,y=60)

    def volverPantallaAnterior(self, parent,controller):
        banderaVolver = controller.comprobarRelaciones()
        if(banderaVolver==1):
            controller.LimpiarArbol()
            parent.mostrarFrameMostrar_Solucion()
        else:
            messagebox.showwarning("Advertencia","No puede dejar NODOS sin RELACIONES")
