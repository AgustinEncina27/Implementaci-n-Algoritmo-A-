from tkinter import *
from tkinter import messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class Eliminar_Nodo(Toplevel):
     
    def __init__(self, controller, master = None):
        
        super().__init__(master = master)
        self.title("Eliminar Nodo")
        self.geometry("500x250")

        lbl1=Label(self,text="Ingrese el NODO a ELIMINAR:")
        lbl1.place(x=5,y=40)
        nodoAEliminar=Entry(self)
        nodoAEliminar.place(x=170,y=40)

        botonCreacion=Button(self,text="ELIMINAR NODO",command=lambda:self.eliminarNodo(nodoAEliminar.get(),controller, master)).place(x=330,y=70)

    def eliminarNodo(self, nodoAEliminar, controller, master):
        if(not(nodoAEliminar.isdecimal())):
            messagebox.showwarning("Advertencia","Por favor ingresar solo números enteros")
        else:
            if(str(nodoAEliminar)==""):
                messagebox.showwarning("Advertencia","Ingrese el NODO a ELIMINAR por favor")
            else:
                controller.eliminarNodo(int(nodoAEliminar))
                master.refrescarFigura()