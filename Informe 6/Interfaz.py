import operator
from collections import defaultdict
from heapq import *
from pyroutelib3 import Router # Import the router
router = Router("car", "map2.osm") # Initialise it
import tkinter
from tkinter import *
import os
import sys
sys.setrecursionlimit(2000)


##------------- PRIMERO SE EJECUTA EL DIJKSTRA ---------------
##-- Para obtener un camino hacia el destino -------------

def dijkstra(edges, f, t):
    g = defaultdict(list)
    for l,r,c in edges:
        g[l].append((c,r))

    q, seen = [(0,f,())], set()
    while q:
        (cost,v1,path) = heappop(q)
        if v1 not in seen:
            seen.add(v1)
            path = (v1, path)
            if v1 == t: return (cost, path)

            for c, v2 in g.get(v1, ()):
                if v2 not in seen:
                    heappush(q, (cost+c, v2, path))

    return float("inf")

edges=[]

for nodos, dic in router.data.routing.items():
   for item in dic:
        edges.append((nodos, item, dic[item]))


## -------------------------
##--------------------------


##---------------------------- ALGORITMO DE ORDENACION TOPOLOGICA --------------




class Vertice:
    def __init__(self,n):
        self.nombre = n
        self.vecinos = list()

        self.d = 0
        self.f = 0
        self.color = 'white'
        self.pred = -1

    def agregarVecino(self, v):
        if v not in self.vecinos:
            self.vecinos.append(v)
            self.vecinos.sort()

class Grafo:
    vertices = {}
    tiempo = 0

    def agregarVertice(self, vertice):
        if isinstance(vertice, Vertice) and vertice.nombre not in self.vertices:
            self.vertices[vertice.nombre] = vertice
            return True
        else:
            return False

    def agregarArista(self, u, v):
        if u in self.vertices and v in self.vertices:
            for key, value in self.vertices.items():
                if key == u:
                    value.agregarVecino(v)
                #if key == v: #Se comenta porque es grafo dirigido
                 #   value.agregarVecino(u)
            return True
        else:
            return False

    def imprimeGrafo(self):
        for key in sorted(list(self.vertices.keys())):
            print("Vertice: "+key )
            print("Descubierto/termino: "+str(self.vertices[key].d)+ "/"+ str(self.vertices[key].f))

    def imprimeOrdenado(self, atributo, invertida = False):
        archivo = open("ordenamiento.txt", "w")
        cadena = str()
        for vertice in (sorted(self.vertices.values(), key=operator.attrgetter(atributo), reverse= True)):
            print("Vertice: {}".format(vertice.nombre))
            cadena = cadena + str("Vertice: {}".format(vertice.nombre)) + '\n'
            print("Descubierto/termino: {}/{}".format(vertice.d, vertice.f))
            cadena = cadena + str("Descubierto/termino: {}/{}".format(vertice.d, vertice.f)) + '\n'
        archivo.write(cadena)
        archivo.close()

    def dfs(self, vert):
        self.tiempo = 0
        for v in sorted(list (self.vertices.keys())):
            if self.vertices[v].color == 'white':
                self.dfsVisitar (self.vertices[v])

    def dfsVisitar(self, vert):
        self.tiempo += 1
        vert.d = self.tiempo
        vert.color = 'gris'

        for v in vert.vecinos:
            if self.vertices[v].color == 'white':
                self.vertices[v].pred = vert
                self.dfsVisitar(self.vertices[v])
        vert.color = 'black'
        self.tiempo += 1
        vert.f = self.tiempo

class Controladora:
    def main(self):
        g = Grafo()
        a = Vertice(int(309998765))
        g.agregarVertice(a)

        camino = open("Camino.txt", "r")
        for item in camino:
            g.agregarVertice(Vertice(int(item)))

        grafo = open("Grafo.txt", "r")
        for item in grafo:
            n1,n2=item.split()
            g.agregarArista(int(n1),int(n2))

        g.dfs(a)
        g.imprimeOrdenado('f', invertida = True)
        grafo.close()
        camino.close()

## -------------------------
##--------------------------

##--------------- INTERFAZ----------------

    ##----------------------------------------------------
window = Tk()
window.geometry("450x200")
window.title("Ordenamiento topológico")

e = Entry(window)
e.grid(row = 1, columnspan=4)

b_calcular = Button(window, text = "CALCULAR RUTA", anchor="w", width=13, command = lambda:ejecutar(int(e.get())))
b_calcular.grid(row=7, column=2)


def ejecutar(coordenada):

    #-------------- ("=== Dijkstra ===")
    camino = (str(dijkstra(edges, coordenada, 2981919237)))
    for char in '(),\n':
        camino = camino.replace(char, ' ')

    camino = camino.split()[1:]

    archivo = open("Camino.txt", "w")
    for elem in camino:
        cadena = str(elem) + '\n'
        archivo.write(cadena)
    archivo.close()

    ##------------------------

    ## --- EMPEZAMOS A PARSEAR PARA OBTENER LOS ARCHIVOS----------

    file1 = open("Camino.txt", "r")
    file2 = open("Aristas.txt", "r")
    grafo = open("Grafo.txt", "w")

    for item in file1:
        item = item.replace("\n", "")
        file2 = open("Aristas.txt", "r")
        for lista in file2:
            n1, n2 = lista.split()
            n1 = n1.replace("\n", "")
            if (int(item) == int(n1)):
                cadena = str(n1) + ' ' + str(n2) + '\n'
                # print(cadena)
                grafo.write(cadena)
    grafo.close()
    file1.close()
    file2.close()

    obj = Controladora()
    obj.main()


########################################## MAIN ##########################################
if __name__ == "__main__":
    window.mainloop()










