from tkinter import *
from tkinter import messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class Modificar_Costo_Relacion(Toplevel):
     
    def __init__(self, controller, master = None):
        
        super().__init__(master = master)
        self.title("Modificar Costo de la Relacion")
        x_ventana = master.winfo_screenwidth() // 2 - 600 // 2
        y_ventana = master.winfo_screenheight() // 2 - 200 // 2
        posicion = str(600) + "x" + str(200) + "+" + str(x_ventana) + "+" + str(y_ventana)
        self.geometry(posicion)

        lbl1=Label(self,text="Ingrese el NODO 1:")
        lbl1.grid(row=1,column=1,padx=10,pady=15)
        nodo1=Entry(self)
        nodo1.grid(row=1,column=2,padx=20,pady=15)

        lbl2=Label(self,text="Ingrese el NODO 2:")
        lbl2.grid(row=2,column=1,padx=10,pady=10)
        nodo2=Entry(self)
        nodo2.grid(row=2,column=2,padx=20,pady=10)

        lbl2=Label(self,text="Ingresar NUEVO COSTO de la relación:")
        lbl2.grid(row=3,column=1,padx=10,pady=10)
        nuevoCosto=Entry(self)
        nuevoCosto.grid(row=3,column=2,padx=20,pady=10)

        botonCreacion=Button(self,text="MODIFICAR COSTO",command=lambda:self.modificarCostoRelacionGrafica(nodo1.get(), nodo2.get(),nuevoCosto.get(),controller, master)).grid(row=3,column=3,padx=20,pady=10)

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