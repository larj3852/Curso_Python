"""
@name           ARBOLES
@description    Son estructuras de datos no lineales que tiene raiz y nodos. La raiz es es el nodo de donde
                la data se origina y los nodos son los otros puntos disponibles para nosotros. Llamados
                padre e hijo. Los ultimos nodos son llamados hojas
"""

#ARBOLES

class Arbol:
    def __init__(self, elemento):
        self.hijos = []
        self.elemento = elemento

#Agregar elementos

def agregarElemento(arbol, elemento, elementoPadre):
    subarbol = buscarSubarbol(arbol, elementoPadre);
    subarbol.hijos.append(Arbol(elemento))

def buscarSubarbol(arbol, elemento):
    if arbol.elemento == elemento:
        return arbol
    for subarbol in arbol.hijos:
        arbolBuscado = buscarSubarbol(subarbol, elemento)
        if (arbolBuscado != None):
            return arbolBuscado
    return None   

#Profundidad y grado

def profundidad(arbol):
    if len(arbol.hijos) == 0: 
        return 1
    return 1 + max(map(profundidad,arbol.hijos)) 

def grado(arbol):
    return max(map(grado, arbol.hijos) + [len(arbol.hijos)])

#Recorridos
def ejecutarProfundidadPrimero(arbol, funcion):
    funcion(arbol.elemento)
    for hijo in arbol.hijos:
        ejecutarProfundidadPrimero(hijo, funcion)

def printElement(element):
    print (element)

#Ejecucion
#ejecutarProfundidadPrimero(arbol, printElement)

def ejecutarAnchoPrimero(arbol, funcion, cola = deque()):
    funcion(arbol.elemento)
    if (len(arbol.hijos) > 0):
        cola.extend(arbol.hijos)
    if (len(cola) != 0):
        ejecutarAnchoPrimero(cola.popleft(), funcion, cola) 

def printElement(element):
    print (element)

#ejecutarAnchoPrimero(arbol, printElement)

#Ejemplo
abuela = "Jacqueline Gurney"
marge = "Marge Bouvier"
patty = "Patty Bouvier"
selma = "Selma Bouvier"
bart = "Bart Simpson"
lisa = "Lisa Simpson"
maggie = "Maggie Simpson"
ling = "Ling Bouvier"

arbol = Arbol(abuela)
agregarElemento(arbol, patty, abuela)
agregarElemento(arbol, selma, abuela)
agregarElemento(arbol, ling, selma)
agregarElemento(arbol, marge, abuela)
agregarElemento(arbol, bart, marge)
agregarElemento(arbol, lisa, marge)
agregarElemento(arbol, maggie, marge)

