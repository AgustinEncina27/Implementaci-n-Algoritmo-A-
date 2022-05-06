class Nodo:
    
    def __init__(self, numeroId, h, inicial=False, final=False):
        self.id = numeroId #Numero para identificar el nodo
        self.g = float('inf') #Diccionario con los arcos a otros nodos
        self.h = h #Distancia al nodo final
        self.f = float('inf') #Sumatoria
        self.posX = 0
        self.posY = 0 #Dos valores que nos indicaran la posicion del nodo en la grilla
        self.inicial = inicial
        self.final = final
        self.nodosRelacionados = []
        self.padre = None
        self.sucesores=[]
    
    def calcularF(self):
        self.f = self.g + self.h

    def calcularDistanciaAlNodoFinal(self):
        pass

    def mostrarNodo(self):
        strNodo =''
        strNodo = strNodo + 'ID:' + str(self.id) + ' G:' + str(self.g) + ' F:' + str(self.f) + ' H:' + str(self.h)
        if(self.padre!=None):
            strNodo = strNodo + ' Padre:' + str(self.padre.id)
        return strNodo

    def mostrarId(self):
        strId = str(self.id)
        return strId
    