file1 = open("Camino.txt", "r")
file2 = open("Aristas.txt", "r")
grafo = open("Grafo.txt", "w")

'''
for item in file1:
    #print(file.readline())
    a,b = item.split(" ")
    print(a,b)
'''
cadena=str()


for item in file1:
    item=item.replace("\n","")
    file2 = open("Aristas.txt", "r")
    for lista in file2:
        n1,n2=lista.split()
        n1=n1.replace("\n","")
        if(int(item) == int(n1)):
            cadena = str(n1) + ' ' + str(n2) + '\n'
            print(cadena)
            grafo.write(cadena)
