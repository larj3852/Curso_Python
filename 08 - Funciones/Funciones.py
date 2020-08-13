"""Funcion: Conjunto de instrucciones agrupadas con un nombre en concreto
que pueden utilizarse cuantas veces sean necesario
"""

def nombre():
    print("Lalo")
    print("Lalo")
    print("Lalo")

nombre()
print("------------------------")

#Parametros opcionales

def nombre2(nombre, dni = None,imprimir=False): #Variable Vacia / Valor Boleano
    print(nombre)
    if dni!=None:
        print(dni)

nombre2("Pedro")
nombre2("Pedro",123124)
print("------------------------")

#Funciones Lambda
""" Es una función anónima: Sin nombre 
    Sirve para tareas repetitivas que pueden ser pequeñas

"""
