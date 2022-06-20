from tkinter import *
from tkinter import messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class Eliminar_Nodo(Toplevel):
     
    def __init__(self, controller, master = None):
        
        super().__init__(master = master)
        self.title("Eliminar Nodo")
        x_ventana = master.winfo_screenwidth() // 2 - 500 // 2
        y_ventana = master.winfo_screenheight() // 2 - 100 // 2
        posicion = str(500) + "x" + str(100) + "+" + str(x_ventana) + "+" + str(y_ventana)
        self.geometry(posicion)

        lbl1=Label(self,text="Ingrese el NODO a ELIMINAR:")
        lbl1.grid(row=1,column=1,padx=10,pady=15)
        nodoAEliminar=Entry(self)
        nodoAEliminar.grid(row=1,column=2,padx=20,pady=15)

        botonCreacion=Button(self,text="ELIMINAR NODO",command=lambda:self.eliminarNodo(nodoAEliminar.get(),controller, master)).grid(row=1,column=3,padx=20,pady=10)

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