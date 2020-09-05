"""
Estructuras definidas por usuario

@name           ARRAYS

@description    Extructuras y listas son definidas con la misma extructura, con una diferencia
                Las listas permiten almacenamiento de elementos heterogeneos mientras que arrays
                permiten solo elementos homogeneos.

@name           PILAS

@description    Son estructuras de datos lineales  basadas en el principio de  LIFO
                Son construidas usando la estructura de un array y tienen operaciones llamadas
                pushing (add) elementos, popping (deleting) elementos y accediendo a los elementos
                solo en un punto llamado TOP. El top es la posición actual de la pila.  

                Son usados en aplicaciones como programacion recursiva.

@name           COLAS

@description 
"""

class Pila():
    def __init_(self,size):
        self.lista = []
        self.tope = 0
        self.size = size
    
    def empty(self):
        if self.tope == 0:
            return True
        else:
            return False
    
    def push(self,dato):
        if  self.tope<self.size:
            self.lista += [dato]
            self.tope +=  1
        else:
            print("La pila esta llena")
    
    def pop(self):
        if self.empty():
            print("La pila esta vacia")
        else:
            self.tope -= 1
            self.lista = [self.lista[x] for x in range(self.tope)]
    
    def show(self):
        for i in range(self.tope):
            print("[%d] => %d"%(i,lista[i]))
    
    def size(self):
        return self.tope

    def top(self):
        return self.lista[-1]

"""
@name           COLAS
@description    Es una estructura lineal de datos basada en el principio FIFO
                Es construida utilizando un array
"""
