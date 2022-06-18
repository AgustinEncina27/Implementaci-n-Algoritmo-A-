from tkinter import *
from tkinter import messagebox
from tkinter.tix import COLUMN
from turtle import right
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class Heuristicas(Frame):
    #Constructor de Cargar
    def __init__(self, parent,controller,final):
        super().__init__(parent)
        ancho_ventana = 500
        lista1 = {}
        alto_ventana = 600
        x_ventana = parent.winfo_screenwidth() // 2 - ancho_ventana // 2
        y_ventana = parent.winfo_screenheight() // 2 - alto_ventana // 2
        posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
        parent.geometry(posicion)
        parent.resizable(0,0)
        self.pack(expand=True,fill="both")
        self.config(width="600",height="600")

        nodos=controller.cantidadDeNodos()
       
        self.pack(fill=BOTH,expand=1)

        #Muestra el grafo con el que se esta trabajando
        f=controller.getFigura()
        canvas1 = FigureCanvasTkAgg(f, self)
        canvas1.draw()
        canvas1.get_tk_widget().pack()

        mi_canvas=Canvas(self)
        mi_canvas.pack(side=LEFT,fill=BOTH,expand=1)

        barra=Scrollbar(self,orient=VERTICAL,command=mi_canvas.yview)
        barra.pack(side=RIGHT,fill=Y)

        mi_canvas.configure(yscrollcommand=barra.set)
        mi_canvas.bind('<Configure>',lambda e:mi_canvas.configure(scrollregion=mi_canvas.bbox("all")))

        segundo_Frame=Frame(mi_canvas)

        mi_canvas.create_window((0,0),window=segundo_Frame,anchor="nw")

        cont=1
        #Botones
        botonMostrar=Button(segundo_Frame,text="MOSTRAR SOLUCIÓN",command=lambda:self.MostrarSolucion(parent,controller,lista1))
        botonMostrar.grid(row=cont,column=0,pady=10,padx=10)
        cont=cont+1
        #Labels y cuadros de textos
        for j in nodos:
            if(j!=final):
                Label(segundo_Frame,text=f'Ingrese la Euristica del NODO '+str(j)+' :').grid(row=cont,column=0,pady=10,padx=10)
                a=Entry(segundo_Frame)
                a.grid(row=cont,column=1,pady=10,padx=10)
                lista1[j]=a
                cont=cont+1
        
        

    #Obtiene el controlador 
    def set_controller(self, controller):
        self.controller = controller
    
    def validate_entry(self,text):
        return text.isdecimal()

    #Muestra como va quedando el grafo cada vez que se agrega una relacion
    def MostrarSolucion(self,parent,controller,lista1):
        contador=0
        for value in lista1.values():
            a=value.get()
            if(a=="" or not(a.isdecimal())):
                contador=contador+1
        if(contador>0):
            messagebox.showwarning("Advertencia","Tiene que ingresar todas las HEURISTICAS y las mismas tienen que ser decimales")
        else:
            for key, value in lista1.items():
                controller.cambiarHGrafo(int(key),int(value.get()))
            parent.mostrarFrameMostrar_Solucion()