from tkinter import *
from tkinter import messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class Cambiar_Nodo_Inicial(Toplevel):
     
    def __init__(self, controller, master = None):
        
        super().__init__(master = master)
        self.title("Cambiar Nodo Inicial")
        self.geometry("500x250")

        lbl1=Label(self,text="Ingrese el nuevo NODO INICIAL:")
        lbl1.place(x=5,y=40)
        nuevoNodoInicial=Entry(self)
        nuevoNodoInicial.place(x=170,y=40)

        botonCreacion=Button(self,text="CAMBIAR NODO INICIAL",command=lambda:self.cambiarNodoInicial(nuevoNodoInicial.get(), controller, master)).place(x=330,y=70)

    def cambiarNodoInicial(self, nuevoNodoInicial, controller, master):
        if(not(nuevoNodoInicial.isdecimal())):
            messagebox.showwarning("Advertencia","Por favor ingresar solo números enteros")
        else:
            if(str(nuevoNodoInicial)==""):
                messagebox.showwarning("Advertencia","Ingrese el NUEVO INICIAL por favor")
            else:
                bandera = controller.cambiarNodoInicial(int(nuevoNodoInicial))
                if(bandera==2):
                    messagebox.showwarning("Advertencia","Ingrese unicamente un NODO VALIDO")
                else:
                    master.refrescarFigura()