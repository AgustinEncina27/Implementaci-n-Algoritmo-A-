from doctest import master
from tkinter import *
from tkinter import messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class Agregar_Relacion(Toplevel):
     
    def __init__(self, controller, master = None):
        
        super().__init__(master = master)
        self.title("Agregar Relacion")
        self.geometry("500x250")

        lbl1=Label(self,text="Ingrese el NODO 1:")
        lbl1.place(x=5,y=40)
        nodo1=Entry(self)
        nodo1.place(x=170,y=40)

        lbl2=Label(self,text="Ingrese el NODO 2:")
        lbl2.place(x=5,y=70)
        nodo2=Entry(self)
        nodo2.place(x=170,y=70)

        lbl2=Label(self,text="Ingresar COSTO de la relación:")
        lbl2.place(x=5,y=100)
        relaciones=Entry(self)
        relaciones.place(x=170,y=100)

        botonCreacion=Button(self,text="AGREGAR RELACIÓN",command=lambda:self.cargarRelacionEditar(nodo1.get(), nodo2.get(),relaciones.get(),controller, master)).place(x=330,y=70)

    def cargarRelacionEditar(self, nodo1, nodo2, relaciones, controller, master):
        if(not(nodo1.isdecimal()) or not(nodo2.isdecimal()) or not(relaciones.isdecimal())):
            messagebox.showwarning("Advertencia","Por favor ingresar solo números enteros")
        else:
            if(str(nodo1)=="" or str(nodo2)=="" or str(relaciones)==""):
                messagebox.showwarning("Advertencia","Ingrese los NODOS A RELACIONAR y el PESO por favor")
            else:
                if(int(nodo1)==int(nodo2)):
                    messagebox.showwarning("Advertencia","El NODO 1  y el NODO 2 tiene que ser diferentes")
                elif controller:
                    bandera = controller.agregarRelacionGrafo(int(nodo1),int(nodo2),int(relaciones))
                    if(bandera==2):
                        messagebox.showwarning("Advertencia","Ingrese unicamente NODOS VALIDOS")
                    else:
                        master.refrescarFigura(controller)
