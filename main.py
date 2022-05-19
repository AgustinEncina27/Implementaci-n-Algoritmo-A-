from algoritmo_A import *
from crearGrafo import *
import tkinter as tk

if __name__ == '__main__':
    root = tk.Tk()
    root.wm_title("Ventana Resultado")
    T = tk.Text(root, height = 20, width = 52) 
    while(seleccionarGrafo()):
        print('Ingrese una opcion correcta')
    iniciarAlgoritmo()
    T.pack()
    T.insert(tk.END, mostrarTextoSolucion())
    root.mainloop()