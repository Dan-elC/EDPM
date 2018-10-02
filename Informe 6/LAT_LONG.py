from pyroutelib3 import Router # Import the router
router = Router("car", "map2.osm") # Initialise it
archivo = open("LAT_LONG.txt", "w")

archivo.write('LAT Y LON:\n')

for i in router.data.rnodes:
    cadena = 'Nodo ' + str(i) + ' -> ' + str(router.data.rnodes[i]) + '\n'
    archivo.write(cadena)
