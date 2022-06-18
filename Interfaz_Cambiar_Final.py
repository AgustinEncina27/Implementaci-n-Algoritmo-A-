from tkinter import *
from tkinter import messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class Cambiar_Nodo_Final(Toplevel):
     
    def __init__(self, controller, master = None):
        
        super().__init__(master = master)
        self.title("Cambiar Nodo Final")
        self.geometry("500x250")

        lbl1=Label(self,text="Ingrese el nuevo NODO FINAL:")
        lbl1.place(x=5,y=40)
        nuevoNodoFinal=Entry(self)
        nuevoNodoFinal.place(x=170,y=40)

        botonCreacion=Button(self,text="CAMBIAR NODO FINAL",command=lambda:self.cambiarNodoFinal(nuevoNodoFinal.get(), controller, master)).place(x=330,y=70)

    def cambiarNodoFinal(self, nuevoNodoFinal, controller, master):
        if(not(nuevoNodoFinal.isdecimal())):
            messagebox.showwarning("Advertencia","Por favor ingresar solo números enteros")
        else:
            if(str(nuevoNodoFinal)==""):
                messagebox.showwarning("Advertencia","Ingrese el NUEVO FINAL por favor")
            else:
                bandera = controller.cambiarNodoFinal(int(nuevoNodoFinal))
                if(bandera==2):
                    messagebox.showwarning("Advertencia","Ingrese unicamente un NODO VALIDO")
                else:
                    master.refrescarFigura()