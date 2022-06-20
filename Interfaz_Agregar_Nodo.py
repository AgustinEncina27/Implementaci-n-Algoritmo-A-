from tkinter import *
from tkinter import messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class Agregar_Nodo(Toplevel):
     
    def __init__(self, controller, master = None):
        
        super().__init__(master = master)
        self.title("Agregar Nodo")
        x_ventana = master.winfo_screenwidth() // 2 - 500 // 2
        y_ventana = master.winfo_screenheight() // 2 - 125 // 2
        posicion = str(500) + "x" + str(125) + "+" + str(x_ventana) + "+" + str(y_ventana)
        self.geometry(posicion)

        lbl1=Label(self,text="Ingrese el nuevo NODO:")
        lbl1.grid(row=1,column=1,padx=10,pady=15)
        nodoNuevo=Entry(self)
        nodoNuevo.grid(row=1,column=2,padx=20,pady=15)

        lbl2=Label(self,text="Ingrese la heuristica:")
        lbl2.grid(row=2,column=1,padx=10,pady=10)
        heurisitca=Entry(self)
        heurisitca.grid(row=2,column=2,padx=20,pady=10)

        botonCreacion=Button(self,text="AGREGAR NODO",command=lambda:self.cargarNuevoNodoEditar(nodoNuevo.get(), heurisitca.get(),controller, master)).grid(row=2,column=3,padx=20,pady=10)

    def cargarNuevoNodoEditar(self, nuevoNodo, heuristica, controller, master):
        if(not(nuevoNodo.isdecimal()) or not(heuristica.isdecimal())):
            messagebox.showwarning("Advertencia","Por favor ingresar solo números enteros")
        else:
            if(str(nuevoNodo)=="" or str(heuristica)==""):
                messagebox.showwarning("Advertencia","Ingrese el NUEVO NODO y la heuristica por favor")
            else:
                bandera = controller.agregarNuevoNodo(int(nuevoNodo),int(heuristica))
                if(bandera==2):
                    messagebox.showwarning("Advertencia","El NODO ingresado ya EXISTE, ingrese uno NUEVO")
                else:
                    master.refrescarFigura(controller)
        self.destroy()
        self.update()