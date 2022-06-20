from tkinter import *
from tkinter import messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class Eliminar_Nodo(Toplevel):
     
    def __init__(self, controller, master = None):
        
        super().__init__(master = master)
        self.title("Eliminar Nodo")
        x_ventana = master.winfo_screenwidth() // 2 - 500 // 2
        y_ventana = master.winfo_screenheight() // 2 - 250 // 2
        posicion = str(500) + "x" + str(250) + "+" + str(x_ventana) + "+" + str(y_ventana)
        self.geometry(posicion)

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
                bandera = controller.eliminarNodo(int(nodoAEliminar))
                if(bandera==2):
                    messagebox.showwarning("Advertencia","Ingrese unicamente un NODO VALIDO")
                else:
                    if(bandera==3):
                        messagebox.showwarning("Advertencia","No puede eliminar un NODO FINAL o INICIAL, antes debe cambiarlo")
                    else:
                        master.refrescarFigura(controller)
        self.destroy()
        self.update()