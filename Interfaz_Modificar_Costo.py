from tkinter import *
from tkinter import messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class Modificar_Costo_Relacion(Toplevel):
     
    def __init__(self, controller, master = None):
        
        super().__init__(master = master)
        self.title("Modificar Costo de la Relacion")
        x_ventana = master.winfo_screenwidth() // 2 - 500 // 2
        y_ventana = master.winfo_screenheight() // 2 - 250 // 2
        posicion = str(500) + "x" + str(250) + "+" + str(x_ventana) + "+" + str(y_ventana)
        self.geometry(posicion)

        lbl1=Label(self,text="Ingrese el NODO 1:")
        lbl1.place(x=5,y=40)
        nodo1=Entry(self)
        nodo1.place(x=170,y=40)

        lbl2=Label(self,text="Ingrese el NODO 2:")
        lbl2.place(x=5,y=70)
        nodo2=Entry(self)
        nodo2.place(x=170,y=70)

        lbl2=Label(self,text="Ingresar NUEVO COSTO de la relación:")
        lbl2.place(x=5,y=100)
        nuevoCosto=Entry(self)
        nuevoCosto.place(x=250,y=100)

        botonCreacion=Button(self,text="MODIFICAR COSTO",command=lambda:self.modificarCostoRelacionGrafica(nodo1.get(), nodo2.get(),nuevoCosto.get(),controller, master)).place(x=330,y=70)

    def modificarCostoRelacionGrafica(self, nodo1, nodo2, nuevoCosto, controller, master):
        if(not(nodo1.isdecimal()) or not(nodo2.isdecimal()) or not(nuevoCosto.isdecimal())):
            messagebox.showwarning("Advertencia","Por favor ingresar solo números enteros")
        else:
            if(str(nodo1)=="" or str(nodo2)=="" or str(nuevoCosto)==""):
                messagebox.showwarning("Advertencia","Ingrese los NODOS y el COSTO de la RELACION por favor")
            else:
                if(int(nodo1)==int(nodo2)):
                    messagebox.showwarning("Advertencia","El NODO 1  y el NODO 2 tiene que ser diferentes")
                else:
                    bandera =controller.modificarCostoRelacion(int(nodo1),int(nodo2),int(nuevoCosto))
                    if(bandera==2):
                        messagebox.showwarning("Advertencia","Ingrese unicamente NODOS VALIDOS")
                    elif (bandera==3):
                        messagebox.showwarning("Advertencia","No existe RELACION entre los nodos ingresados")
                    else:
                        master.refrescarFigura(controller)
        self.destroy()
        self.update()