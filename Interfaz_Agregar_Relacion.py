from doctest import master
from tkinter import *
from tkinter import messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class Agregar_Relacion(Toplevel):
     
    def __init__(self, controller, master = None):
        
        super().__init__(master = master)
        self.title("Agregar Relacion")
        x_ventana = master.winfo_screenwidth() // 2 - 500 // 2
        y_ventana = master.winfo_screenheight() // 2 - 200 // 2
        posicion = str(500) + "x" + str(200) + "+" + str(x_ventana) + "+" + str(y_ventana)
        self.geometry(posicion)

        lbl1=Label(self,text="Ingrese el NODO 1:")
        lbl1.grid(row=1,column=1,padx=10,pady=15)
        nodo1=Entry(self)
        nodo1.grid(row=1,column=2,padx=20,pady=15)

        lbl2=Label(self,text="Ingrese el NODO 2:")
        lbl2.grid(row=2,column=1,padx=10,pady=10)
        nodo2=Entry(self)
        nodo2.grid(row=2,column=2,padx=20,pady=10)

        lbl2=Label(self,text="Ingresar COSTO de la relación:")
        lbl2.grid(row=3,column=1,padx=10,pady=10)
        relaciones=Entry(self)
        relaciones.grid(row=3,column=2,padx=20,pady=10)

        botonCreacion=Button(self,text="AGREGAR RELACIÓN",command=lambda:self.cargarRelacionEditar(nodo1.get(), nodo2.get(),relaciones.get(),controller, master)).grid(row=3,column=3,padx=20,pady=10)

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
        self.destroy()
        self.update()
