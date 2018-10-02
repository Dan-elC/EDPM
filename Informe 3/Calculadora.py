import sys
from tkinter import *


class Stack:

    def __init__(self):
        self.top = None
        self.size = 0

    def isEmpty(self):
        return self.size is 0

    def len(self):
        return self.size

    def push(self, item):
        self.top = Node(item, self.top)
        self.size += 1

    def pop(self):
        assert not self.isEmpty(),  "PILA VACIA!!"
        node = self.top
        self.top = node.next
        self.size -= 1
        return node.item

    def peek(self):
        assert not self.isEmpty()
        node = self.top
        return node.item


class Node:
    def __init__(self, item, link):
        self.item = item
        self.next = link

############---------------CALCULADORA----------------################


class Calculadora():

    def calcular(self, cadena):
        self.symbol = Stack()
        self.numero = Stack()
        self.resultado = None

        for i in range(0, len(cadena)):
            c = self.convertir(cadena[i])
            if(c[1]==0):                        #Abre paréntesis
                self.symbol.push(c[0])
                continue

            elif(c[1]==2):                      #Si es un dígito
                n = cadena[i-1]
                if(48<= ord(n)  <= 57):
                    n = self.numero.pop()*10 + c[0]
                    self.numero.push(n)
                else:
                    self.numero.push(c[0])
                continue

            elif(c[1]==3):                      #Si es un operador
                #self.symbol.push(c[0])
                if(self.symbol.peek() == "("):
                    self.symbol.push(c[0])

                elif(self.prioridad(self.symbol.peek(),c[0]) == True):
                    op2 = self.numero.pop()
                    op = self.symbol.pop()
                    op1 = self.numero.pop()
                    self.resultado = self.operar(op1, op, op2)
                    self.numero.push(self.resultado)
                    self.symbol.push(c[0])
                else:
                    self.symbol.push(c[0])

            elif(c[1]==1):                          #Cierra paréntesis
                while(1):
                    op = self.symbol.pop()
                    if(op == "("):
                        break
                    else:
                        op2 = self.numero.pop()
                        op1 = self.numero.pop()
                        self.resultado = self.operar(op1, op, op2)
                        self.numero.push(self.resultado)

        #print(self.numero.pop())
        return self.numero.pop()



    def prioridad(self, p1, p2):                    #Si la prioridad es mayor o igual
        if((p1=="*" or p1=="/") and (p2=="-" or p2=="+")) or (p1==p2):
            return True
        elif((p1=="*" and p2=="/") or (p1=="/" and p2=="*")):
            return True
        return False


    def operar(self,op1,op,op2):
        if (op=="*"):
            return op1*op2
        if (op == "/"):
            return op1 // op2
        if (op == "+"):
            return op1 + op2
        if (op == "-"):
            return op1 - op2


    def convertir(self, item):

        if(item == "("):
            return item, 0                  #Abre paréntesis

        elif(item == ")"):
            return item, 1                  #Cierra paréntesis

        elif(48<= ord(item)  <= 57):
            return ord(item)-48, 2          #Si es un dígito

        else:
            return item, 3                  #Si es un operador


##########----------------INTERFACE--------------------###############



def set_text(num):
    if(num=="CE"):
        e.delete(0, END)
    elif(num=="EQUAL"):
        datos = e.get()
        C = Calculadora()
        resultado = C.calcular("(" + datos + ")")
        mLabel.config(text = resultado)
    else:
        e.insert(END, num)
    return


window = Tk()
window.geometry("250x200")
window.title("Calculadora")

e = Entry(window)
e.grid(row = 1, columnspan=4)

datos = StringVar()


b_0 = Button(window, text = "0", anchor="w", width=1, command = lambda:set_text("0"))
b_0.grid(row=7, column=2)
b_1 = Button(window, text = "1", anchor="w", width=1, command = lambda:set_text("1"))
b_1.grid(row=6, column=1)
b_2 = Button(window, text = "2", anchor="w", width=1, command = lambda:set_text("2"))
b_2.grid(row=6, column=2)
b_3 = Button(window, text = "3", anchor="w", width=1, command = lambda:set_text("3"))
b_3.grid(row=6, column=3)
b_4 = Button(window, text = "4", anchor="w", width=1, command = lambda:set_text("4"))
b_4.grid(row=5, column=1)
b_5 = Button(window, text = "5", anchor="w", width=1, command = lambda:set_text("5"))
b_5.grid(row=5, column=2)
b_6 = Button(window, text = "6", anchor="w", width=1, command = lambda:set_text("6"))
b_6.grid(row=5, column=3)
b_7 = Button(window, text = "7", anchor="w", width=1, command = lambda:set_text("7"))
b_7.grid(row=4, column=1)
b_8 = Button(window, text = "8", anchor="w", width=1, command = lambda:set_text("8"))
b_8.grid(row=4, column=2)
b_9 = Button(window, text = "9", anchor="w", width=1, command = lambda:set_text("9"))
b_9.grid(row=4, column=3)



b_clear = Button(window, text = "CE", anchor=CENTER, width=2,height=8, command = lambda:set_text("CE"))
b_clear.grid(row=4, column=5,rowspan=4)

b_mas = Button(window, text = "+", anchor=CENTER, width=2, command = lambda:set_text("+"))
b_mas.grid(row=4, column=4)
b_menos = Button(window, text = "-", anchor=CENTER, width=2, command = lambda:set_text("-"))
b_menos.grid(row=5, column=4)
b_multi = Button(window, text = "*", anchor=CENTER, width=2, command = lambda:set_text("*"))
b_multi.grid(row=6, column=4)
b_divi = Button(window, text = "/", anchor=CENTER, width=2, command = lambda:set_text("/"))
b_divi.grid(row=7, column=4)
b_oBra = Button(window, text = "(", anchor=CENTER, width=2, command = lambda:set_text("("))
b_oBra.grid(row=7, column=1)
b_cBra = Button(window, text = ")", anchor=CENTER, width=2, command = lambda:set_text(")"))
b_cBra.grid(row=7, column=3)

b_igual = Button(window, text = "=", anchor=CENTER, width=30, command = lambda:set_text("EQUAL"))
b_igual.grid(row=8, columnspan=15)

mLabel = Label(window, anchor = CENTER)
mLabel.grid(row = 9, column = 3)


window.mainloop()


#if __name__ == "__main__":

#    C= Calculadora()
#    C.calcular("((10*3+6)/(6))")