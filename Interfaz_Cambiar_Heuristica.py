from tkinter import *
from tkinter import messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class Cambiar_Heuristica(Toplevel):
     
    def __init__(self, controller, master = None):
        
        super().__init__(master = master)
        self.title("Cambiar Heuristica")
        x_ventana = master.winfo_screenwidth() // 2 - 500 // 2
        y_ventana = master.winfo_screenheight() // 2 - 250 // 2
        posicion = str(500) + "x" + str(250) + "+" + str(x_ventana) + "+" + str(y_ventana)
        self.geometry(posicion)

        lbl1=Label(self,text="Ingrese el NODO:")
        lbl1.place(x=5,y=40)
        nodo=Entry(self)
        nodo.place(x=170,y=40)

        lbl1=Label(self,text="Ingrese la nueva HEURISTICA:")
        lbl1.place(x=5,y=70)
        nuevaHeuristica=Entry(self)
        nuevaHeuristica.place(x=170,y=70)

        botonCreacion=Button(self,text="CAMBIAR HEURISTICA",command=lambda:self.cambiarHeuristica(nodo.get(),nuevaHeuristica.get(),controller, master)).place(x=330,y=70)

    def cambiarHeuristica(self, nodo, nuevaHeuristica, controller, master):
        if(not(nodo.isdecimal()) or not(nuevaHeuristica.isdecimal())):
            messagebox.showwarning("Advertencia","Por favor ingresar solo números enteros")
        else:
            if(str(nodo)=="" or str(nuevaHeuristica)==""):
                messagebox.showwarning("Advertencia","Ingrese el NODO y la HEURISTICA por favor")
            else:
                bandera = controller.cambiarHGrafo(int(nodo), int(nuevaHeuristica))
                if(bandera==2):
                    messagebox.showwarning("Advertencia","Ingrese unicamente un NODO VALIDO")
                else:
                    master.refrescarFigura(controller)
        self.destroy()
        self.update()