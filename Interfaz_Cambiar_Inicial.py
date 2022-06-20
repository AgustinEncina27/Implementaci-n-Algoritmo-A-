from tkinter import *
from tkinter import messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class Cambiar_Nodo_Inicial(Toplevel):
     
    def __init__(self, controller, master = None):
        
        super().__init__(master = master)
        self.title("Cambiar Nodo Inicial")
        x_ventana = master.winfo_screenwidth() // 2 - 600 // 2
        y_ventana = master.winfo_screenheight() // 2 - 100 // 2
        posicion = str(600) + "x" + str(100) + "+" + str(x_ventana) + "+" + str(y_ventana)
        self.geometry(posicion)

        lbl1=Label(self,text="Ingrese el nuevo NODO INICIAL:")
        lbl1.grid(row=1,column=1,padx=10,pady=15)
        nuevoNodoInicial=Entry(self)
        nuevoNodoInicial.grid(row=1,column=2,padx=20,pady=15)

        botonCreacion=Button(self,text="CAMBIAR NODO INICIAL",command=lambda:self.cambiarNodoInicial(nuevoNodoInicial.get(), controller, master)).grid(row=1,column=3,padx=20,pady=10)

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
                    master.refrescarFigura(controller)
        self.destroy()
        self.update()