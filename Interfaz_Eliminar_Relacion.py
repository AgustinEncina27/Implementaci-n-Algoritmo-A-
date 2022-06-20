from tkinter import *
from tkinter import messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class Eliminar_Relacion(Toplevel):
     
    def __init__(self, controller, master = None):
        
        super().__init__(master = master)
        self.title("Eliminar Relacion")
        x_ventana = master.winfo_screenwidth() // 2 - 500 // 2
        y_ventana = master.winfo_screenheight() // 2 - 250 // 2
        posicion = str(500) + "x" + str(250) + "+" + str(x_ventana) + "+" + str(y_ventana)
        self.geometry(posicion)

        lbl1=Label(self,text="Ingrese el NODO 1:")
        lbl1.place(x=5,y=40)
        nodo1AEliminar=Entry(self)
        nodo1AEliminar.place(x=170,y=40)

        lbl2=Label(self,text="Ingrese el NODO 2:")
        lbl2.place(x=5,y=70)
        nodo2AEliminar=Entry(self)
        nodo2AEliminar.place(x=170,y=70)

        botonCreacion=Button(self,text="ELIMINAR RELACION",command=lambda:self.cargarNuevoNodoEditar(nodo1AEliminar.get(), nodo2AEliminar.get(),controller, master)).place(x=330,y=70)

    def cargarNuevoNodoEditar(self, nodo1AEliminar, nodo2AEliminar, controller, master):
        if(not(nodo1AEliminar.isdecimal()) or not(nodo2AEliminar.isdecimal())):
            messagebox.showwarning("Advertencia","Por favor ingresar solo números enteros")
        else:
            if(str(nodo1AEliminar)=="" or str(nodo2AEliminar)==""):
                messagebox.showwarning("Advertencia","Ingrese los NODOS de la RELACION a ELIMINAR por favor")
            else:
                if(int(nodo1AEliminar)==int(nodo2AEliminar)):
                    messagebox.showwarning("Advertencia","El NODO 1  y el NODO 2 tiene que ser diferentes")
                else:
                    bandera = controller.eliminarRelacion(int(nodo1AEliminar),int(nodo2AEliminar))
                    if(bandera==2):
                        messagebox.showwarning("Advertencia","Ingrese unicamente NODOS VALIDOS")
                    else:
                        if(bandera==3):
                            messagebox.showwarning("Advertencia","No existe RELACION entre los NODOS ingresados")
                        else:
                            master.refrescarFigura(controller)
        self.destroy()
        self.update()