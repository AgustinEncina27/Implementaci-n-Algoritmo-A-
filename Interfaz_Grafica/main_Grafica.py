#Se importan librerias de trabajo
from tkinter import *
import tkinter as tk
from Interfaz_principal import Frame_1
from Interfaz_Cargar import Frame_2
from Interfaz_Aleatoria import Frame_3

#Se crea clase principal (tk.Tk), la cual es la encargada de manejar los Frames
class APP(tk.Tk): 
    #OJO: Notar que pasamos "*args" y "**kwargs", porque podrian ser necesarios (recordar pasarlos a inicializacion de tk.Tk)
    def __init__(self,*args,**kwargs):
        #Se inicializa ademas, con la herencia de tk.Tk, para tener todas estas disponibilidades en "self"
        super().__init__(*args,**kwargs)

        #Se aprovecha que "self" ya es la ventana principal y se agrega titulo respectivo
        self.title("Implementación Algoritmo A estrella")
        
        #Centrar la ventana
        ancho_ventana = 900
        alto_ventana = 900
        x_ventana = self.winfo_screenwidth() // 2 - ancho_ventana // 2
        y_ventana = self.winfo_screenheight() // 2 - alto_ventana // 2
        posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
        self.geometry(posicion)
        self.resizable(0,0)
        
        #OJO: Se crea el "CONTENEDOR PRINCIPAL", el cual es un Frame en donde se llamaran a los otros Frames de las otras clases...
        #...esto nos permitira tener el efecto de multiples ventanas segun la que se necesita (osea el frame respectivo)
        contenedor_principal = tk.Frame( self ,bg = "yellow")
        contenedor_principal.pack()
       
        #Menu de la ventana
        barraMenu=Menu(self)
        self.config(menu=barraMenu,width=300,height=300)
        creacionGrafo=Menu(barraMenu,tearoff=0)
        inicio=Menu(barraMenu,tearoff=0)
        inicio.add_command(label="Volver al Pricipal",command = lambda:self.show_frame( Frame_1 ) )
        creacionGrafo.add_command(label="Cargar datos(nodos y relaciones)",command = lambda:self.show_frame( Frame_2 ))
        creacionGrafo.add_command(label="Aleatorio",command = lambda:self.show_frame( Frame_3 ))
        barraMenu.add_cascade(label="Inicio",menu=inicio)
        barraMenu.add_cascade(label="Creación del grafo",menu=creacionGrafo)
        
        #IMPORTANTISIMO (CREACION DE DICCIONARIO CON FRAMES A UTILIZAR EN APP --> TODAS LAS FRAMES QUE SE TENGAN):
        #Recordar que este diccionario, almacena los frames y juega un papel esencial en indicar cual de todos mostrar.
        #Ademas, se vuelve util con metodo especial para acceder a otros frames (ver mas abajo)
        self.todos_los_frames = dict()

        #PARTE INDISPENSABLE DE TRABAJO CON MULTIPAGINAS (MULTIPLES FRAMES):
        #Se debe crear cada una de las clases de los frames (TODAS), de tal forma que se agregen al diccionario de estas...
        #...esto es fundamental, porque asi identificaremos a cual frame ir, segun algo interactivo para el usuario
        #OJO: se pasan TODAS las clases asociadas a las paginas con las que trabajaremos, y se agregan correctamente...
        #RECORDERIS: Se recorre tupla, de todas las clases (forma de ahorrar lineas de codigo)
        for F in (Frame_1, Frame_2,Frame_3):
            #Se ejecuta la labor de llamar a todas las clases asociadas a Frames_N (una a una)
            #NOTA: ver que se almacenan momentaneamente en frame, para simplificar labor
            #OJO: NECESARIO: Parametro "self", como encargado de ser el "controller", la razon es porque...
            #... desde TODAS las otras clases (Frames), se debe poder acceder a metododo "show_frame", y si...
            #...NO se pasa esta, implica que NO habra acceso a los metodos de la APP principal. Por esto se pasa self.
            frame = F( contenedor_principal , self)
            #Se agrega a diccionario de todos los frames la llave y su respectivo correspondiente:
            #LLAVE = "F"    ---> Cada llave es cada clase de Frame_1, Frame_2, etc...
            #OBJETO = frame, que es :"F(contenedor_principal)"   ---> Cada objeto es Frame_1(contenedor_principal), etc...
            self.todos_los_frames[F] = frame
            #Ahora, se agrega correctamente cada una de las Frames recorridas en la tupla de frames
            #NOTA: FUNDAMENTAL crear frames con sticky = "nsew", para que no aparezcan cosas de otros frames indeseadas
            frame.grid(row = 0, column = 0, sticky = "nsew")
        
        #OJO: luego se debe llamar al metodo "show_frame", creado por nosotros, para mostrar un frame deseado...
        #...en esencia, permite traer al primer plano, un frame del vector "self.todos+los_frames"
        self.show_frame( Frame_1 )

    #METODO PARA MOSTRAR UNICAMENTE FRAME DESEADO (controller = Clase que queremos obtener de diccionario de frames)
    def show_frame(self,contenedor_llamado):
        #Se selecciona el frame requerido por el controller, desde el diccionario de frames ya creado anteriormente
        #Recordemos que el controller, es simplemente el valor por defecto de la clase asociada a cada Frame...
        #...estos keys se crearon arriba al recorrer tupla de los frames de la app
        frame = self.todos_los_frames[contenedor_llamado]
   
        #Ahora se llama a funcion de tkinter heredada desde clase APP, la cual permite traer frame indicada a primer plano
        frame.tkraise()
    

#Se crea APP como tal (aprovechandonos de la clase creada)
root = APP()

#Se ejecuta la ventana principal, creada a traves de POO con las clases respectivas
root.mainloop()