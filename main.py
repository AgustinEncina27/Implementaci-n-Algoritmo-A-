from cProfile import label
import collections
from tkinter import *
from tkinter import ttk

raiz = Tk()
raiz.title('Aplicación')
raiz.eval('tk::PlaceWindow . center')
ttk.Label(raiz, text='Seleccione la forma \nde crear el espacio de busqueda').grid(padx=20, pady=20, row=2, column=1)
ttk.Button(raiz, text='Al azar').grid(row=4,column=0)
ttk.Button(raiz, text='Elegir todo').grid(row=4,column=1)
ttk.Button(raiz, text='Salir', command=quit).grid(row=4,column=2)
raiz.mainloop()


