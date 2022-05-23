import tkinter as tk
from ControladorGrafico import *
from Interfaz_Mostrar_Grafo import *
from Interfaz_Cargar import *
from Interfaz_Aleatoria import *
from Interfaz_Mostrar_Solucion import *
from Interfaz_principal import Principal

class App(tk.Tk):
    #Constructor del la App
    def __init__(self):
        super().__init__()

        self.title('Implementación Algoritmo A estrella')
        ancho_ventana = 500
        alto_ventana = 500
        x_ventana = self.winfo_screenwidth() // 2 - ancho_ventana // 2
        y_ventana = self.winfo_screenheight() // 2 - alto_ventana // 2
        posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
        self.geometry(posicion)
        self.resizable(0,0)

        # create a view and place it on the root window
        self.view = Principal(self)

        # create a controller
        self.controller = Controller(self, self.view)

        #Menu
        barraMenu=Menu(self)
        self.config(menu=barraMenu,width=300,height=300)
        creacionGrafo=Menu(barraMenu,tearoff=0)
        inicio=Menu(barraMenu,tearoff=0)
        inicio.add_command(label="Volver al Pricipal", command=lambda:self.mostrarFramePrincipal())
        creacionGrafo.add_command(label="Cargar datos(nodos y relaciones)", command=lambda:self.mostrarFrameCargar())
        creacionGrafo.add_command(label="Aleatorio", command=lambda:self.mostrarFrameAleatorio())
        barraMenu.add_cascade(label="Inicio",menu=inicio)
        barraMenu.add_cascade(label="Creación del grafo",menu=creacionGrafo)

        # set the controller to view
        self.view.set_controller(self.controller)
    
    #Muestra la interfaz_aleatoria
    def mostrarFrameAleatorio(self):
        self.view.pack_forget()
        self.view = Aleatoria(self,self.controller)
        self.view.set_controller(self.controller)
    
    #Muestra la Interfaz_principal
    def mostrarFramePrincipal(self):
        self.view.pack_forget()
        self.view = Principal(self)
        self.view.set_controller(self.controller)
    
    #Muestra la Interfaz_Carga
    def mostrarFrameCargar(self):
        self.view.pack_forget()
        self.view = Cargar(self,self.controller)
        self.view.set_controller(self.controller)
    
    #Muestra la Interfaz_Mostrar_Grafo
    def mostrarFrameMostrar_Grafo(self):
        self.view.pack_forget()
        self.view = Mostrar_Grafo(self,self.controller)
        self.view.set_controller(self.controller)
    
    #Muestra la Interfaz_Mostrar_Solución
    def mostrarFrameMostrar_Solucion(self):
        self.view.pack_forget()
        self.view = Mostrar_Solucion(self,self.controller)
        self.view.set_controller(self.controller)

#Inicializa  la ventana
if __name__ == '__main__':
    app = App()
    app.mainloop()

