import operator

from pyroutelib3 import Router # Import the router
router = Router("car", "map2.osm") # Initialise it
archivo = open("ordenamiento.txt", "w")
camino = open("Camino.txt", "r")
grafo = open("Grafo.txt","r")
import sys
sys.setrecursionlimit(2000)


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
        cadena = str()
        for vertice in (sorted(self.vertices.values(), key=operator.attrgetter(atributo), reverse= True)):
            print("Vertice: {}".format(vertice.nombre))
            cadena = cadena + str("Vertice: {}".format(vertice.nombre)) + '\n'
            print("Descubierto/termino: {}/{}".format(vertice.d, vertice.f))
            cadena = cadena + str("Descubierto/termino: {}/{}".format(vertice.d, vertice.f)) + '\n'
        archivo.write(cadena)

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

        for item in camino:
            g.agregarVertice(Vertice(int(item)))


        for item in grafo:
            n1,n2=item.split()
            g.agregarArista(int(n1),int(n2))

        g.dfs(a)
        g.imprimeOrdenado('f', invertida = True)

obj = Controladora()
obj.main()
