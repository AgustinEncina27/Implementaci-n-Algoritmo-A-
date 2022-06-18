from tkinter import *
from tkinter import messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class Agregar_Nodo(Toplevel):
     
    def __init__(self, controller, master = None):
        
        super().__init__(master = master)
        self.title("Agregar Nodo")
        self.geometry("500x250")

        lbl1=Label(self,text="Ingrese el nuevo NODO:")
        lbl1.place(x=5,y=40)
        nodoNuevo=Entry(self)
        nodoNuevo.place(x=170,y=40)

        lbl2=Label(self,text="Ingrese la heuristica:")
        lbl2.place(x=5,y=70)
        heurisitca=Entry(self)
        heurisitca.place(x=170,y=70)

        botonCreacion=Button(self,text="AGREGAR NODO",command=lambda:self.cargarNuevoNodoEditar(nodoNuevo.get(), heurisitca.get(),controller, master)).place(x=330,y=70)

    def cargarNuevoNodoEditar(self, nuevoNodo, heuristica, controller, master):
        if(not(nuevoNodo.isdecimal()) or not(heuristica.isdecimal())):
            messagebox.showwarning("Advertencia","Por favor ingresar solo números enteros")
        else:
            if(str(nuevoNodo)=="" or str(heuristica)==""):
                messagebox.showwarning("Advertencia","Ingrese el NUEVO NODO y la heuristica por favor")
            else:
                controller.agregarNuevoNodo(int(nuevoNodo),int(heuristica))
                master.refrescarFigura()