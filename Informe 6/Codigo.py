from pyroutelib3 import Router # Import the router
router = Router("car", "map2.osm") # Initialise it
archivo = open("Nodos.txt", "w")
archivo2 = open("Aristas.txt", "w")

## --- MUESTRA EN CONSOLA

for nodos, dic in router.data.routing.items():
    print(nodos, dic)
    for item in dic:
        print(nodos, item)
        #print(nodos, item, dic[item])

## --- Guarda en archivo los nodos

for nodos in router.data.routing.items():
    cadena = str(nodos[0]) + '\n'
    archivo.write(cadena)


## --- Guarda en archivo las aritas

for nodos, dic in router.data.routing.items():
    for item in dic:
        cadena2 = str(nodos) + ' ' + str(item) + '\n'
        archivo2.write(cadena2)
        #print(nodos, item)

'''
## --- ESCRIBE EN TXT

for i in router.data.routing:

    cadena = 'Nodo ' + str(i) + ' -> ' + str(router.data.routing[i]) + ' '
    #for j, valor in router.data.routing[i].items():
    #    cadena = cadena + str(router.data.routing[i].items()) + ' '
    cadena = cadena  + '\n'
    archivo.write(cadena)
'''
