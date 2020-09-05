"""
Listas Enlazadas

Son estructuras de datos lineales las cuales no son almacenadas consecutivamente, pero están linkeadas
una con otra usando punteros. El nodo de una lista entrelazdas estan compuestas de dato y un puntero
llamado siguiente NEXT.

Estas estructuras son continuamente usadas en vista de imagenes, aplicaciones, reproductores musica
"""

class Nodo():

    def __init__(self,dato):
        self.dato = dato
        self.siguiente = None #siguiente nodo

class ListaEnlazada():
    
    def __init__(self):
        self.primero = None
        self.ultimo = None
    
    def vacia(self):
        return self.primero == None
    
    def agregar_ultimo(self,dato):
        if self.vacia() == True:
            self.primero == Nodo(dato)
            self.primero = self.ultimo = Nodo(dato)
        else:
            aux = self.ultimo
            self.ultimo = self.siguiente = Nodo(dato)
    
    def recorrido(self):
        aux = self.primero
        while aux !=None:
            print(aux.dato)
            aux = aux.siguiente
    
    def eliminar_ultimo(self):
        aux = self.primero
        while aux.siguiente != self.ultimo:
            aux = aux.siguiente
        #print(aux.dato)
        aux.siguiente = None

    def agregar_inicio(self,dato):
        if self.vacia() == True:
            self.primero = self.ultimo = Nodo(dato)
        else:
            aux = Nodo(dato)
            aux.siguiente = self.primero
            self.primero = aux  
    
    def eliminar_inicio(self):
        self.primero = self.primero.siguiente

lista = ListaEnlazada()

lista.agregar_ultimo(12)
lista.agregar_ultimo(43)
lista.agregar_ultimo(2)
lista.agregar_ultimo(19)
lista.agregar_ultimo(30)
lista.agregar_inicio(1)
lista.agregar_inicio(100)
lista.eliminar_inicio()

lista.recorrido()
print("""******************************""")
print(lista.primero.dato)
print(lista.ultimo.siguiente)
lista.eliminar_ultimo()



"""
GRAFOS

Son usados para almacenar puntos de colecciones de datos  llamados vertices (NODOS) y esquinas (EDGES)
Los grafos son la mas acertada  de un mapa del mundo real. Son usados para encontar la variable costo-distancia
entre varios puntos de datos llamados nodos y por lo tanto encuentre el camino mas optimo
Apps--> Maps, uber,
"""
