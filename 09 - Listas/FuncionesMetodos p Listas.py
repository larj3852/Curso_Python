#Listas
peliculas = ["Batman","Superman","Spider-man"]

#Tuplas 
cantantes = ("Drake","Tupac","J Lo")
cantantes = list(cantantes)

numeros = [1,2,5,8,3,4]

#Ordenar
print(numeros)
numeros.sort()
print(numeros)

#Añadir Elementos

cantantes.insert(1,"David Bisbal")
print(cantantes)

#Eliminar Elementos
cantantes.pop(2)
print (cantantes)
cantantes.remove("J Lo")
print (cantantes)

#Dar la vuelta
print(numeros)
numeros.reverse()
print(numeros)

#Buscar dentro de una lista
print("Drake" in cantantes)

#Contar numero elementos
print (len(cantantes))

#Cuantas veces se repite un elemento
numeros.append(8)
numeros.append(8)
numeros.append(8)
print(numeros)
print(numeros.count(8))

#Conseguir indice
print(cantantes.index("Drake"))

#Unir Listas
cantantes.extend(numeros)
print(cantantes)