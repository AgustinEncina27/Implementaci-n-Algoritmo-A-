from tkinter import *
from tkinter import messagebox


class Aleatoria(Frame):   
    #Constructor Aleatoria
    def __init__(self, parent,controller): 
        super().__init__(parent)
        controller.limpiarTodo()
        controller.LimpiarArbol()
       
        ancho_ventana = 500
        alto_ventana = 500
        x_ventana = parent.winfo_screenwidth() // 2 - ancho_ventana // 2
        y_ventana = parent.winfo_screenheight() // 2 - alto_ventana // 2
        posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
        parent.geometry(posicion)
        parent.resizable(0,0)

        self.pack(expand=True,fill="both")
        self.config(width="600",height="600")

        #Labels y cuadros de textos
        lbl1=Label(text="Ingrese la cantidad de NODOS:")
        lbl1.place(x=50,y=170)
        self.nodos=Entry()
        self.nodos.place(x=300,y=170)

        lbl2=Label(text="Ingrese la cantidad de RELACIONES:")
        lbl2.place(x=50,y=200)
        self.relaciones=Entry()
        self.relaciones.place(x=300,y=200)

        #Boton
        botonCreacion=Button(text="CREAR GRAFO",command=lambda:self.CargarGrafo(parent)).place(x=200,y=250)
    
    #Obtiene el controlador 
    def set_controller(self, controller):
        self.controller = controller
    
    #Crea el grafo con los datos ingresados(nodos y relaciones)
    def CargarGrafo(self,parent):
        a= self.nodos.get()
        h=self.relaciones.get()
        if(not(a.isdecimal()) or not(h.isdecimal())):
            messagebox.showwarning("Advertencia","Por favor ingresar solo números enteros")
        else:
            if(a=="" or h==""):
                messagebox.showwarning("Advertencia","Ingrese la cantidad de nodos y relaciones por favor")
            else:
                if (int(h)<int(a)):
                    messagebox.showwarning("Advertencia","La cantidad de relaciones tienen que ser igual o mayor a la cantidad de nodos")
                else:
                    if(int(h)==0 or int(a)==0):
                        messagebox.showwarning("Advertencia","La cantidad de nodos o relaciones no pueden ser nulos")
                    else:
                        z=int(a)
                        x=int(h)
                        b=0
                        for c in range(z+1):
                            acum=c
                            if(c!=0): 
                                b+=acum-1 
                        if(x>b):
                            messagebox.showwarning("Advertencia","Por favor ingrese el rango permitido[0,"+str(b)+"]")
                        elif self.controller:
                            self.controller.CargarDatosGrafoAzar(z,x)
                            parent.mostrarFrameMostrar_Grafo()