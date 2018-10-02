from collections import defaultdict
from heapq import *
from pyroutelib3 import Router # Import the router
router = Router("car", "map2.osm") # Initialise it

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

if __name__ == "__main__":
    print ("=== Dijkstra ===")

    camino = (str(dijkstra(edges,309998765,2981919237 )))
    for char in '(),\n':
        camino=camino.replace(char,' ')

    camino = camino.split()[1:]

    archivo = open("Camino.txt", "w")
    for elem in camino:
        cadena=str(elem) + '\n'
        archivo.write(cadena)