"""
Data Structures in Python

@description    Es una forma de organizar un conjunto de datos elementales con el objetivo de
                facilitar su manipulación
@Lineales       Arreglos (Java,C++), Listas (Python)
                Pilas
                Colas
                Listas Enlazadas
@NoLineales     Arboles
                Grafos     
@Ordenamientos  Burbuja, Seleccion, Insercion, Quicksort
@Busquedas      Lineal, Binaria
"""
#%% List
print("----------------Listas--------------------")
a = [1,2,3,4,2.31,2,2,True,'Olla']
""" Incertar elementos de la lista """
a.append(3)                 # Agregar elementos
a.insert(23.2,4)            # Insertar en espacios en el index n
a.extend(["Papa",False,33]) # Extender elementos
""" Extraer varios elementos """
a[-1]                       # Ultimo elemento de la lista
a[:4]                       # Del primer elemento al n-esimo elemento
a[::-1]                     # Lista al reves
""" Eliminar elementos """
del a[2]                    # Eliminar elemento 2 de la lista
a.remove(True)              # Remueve elementos iguales al argumento
x = a.pop(3)                # Elimina el elemento con index n y lo regresa a la variable x
a.clear                     # Vaciar lista
""" Otros metodos """
len(a)                      # Largo de la lista
a.index(True)               # Encuentra el numero de index del primera valor con el valor en el argumento
a.count(2)                  # Cuenta cuantasa veces se repite el elemento
sorted(a)                   # Ordena la lista sin generar cambio
a.sort(reverse=True)        # Ordena lista al reves

#LOOP Extraccion de 2 listas al mismo tiempo
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))

#LOOP Enumeracion
for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)

#%% Diccionarios
print("""---------------- Diccionarios --------------------
        Son usados para almacenar pares Key-values
""")

diccionario = {}            # Diccionario vacio
                            # Creacion Diccionario
diccionario = {'Uno':'Yoyo','Dos':'Pelota','Tres':[1,2,3,'Yoyo','Pato']}     
diccionario['Uno']          # Extraccion de elementos
diccionario['Tres']

b = diccionario.pop("Uno")  # Elimina elemento
b = diccionario.popitem()   # Extrae los valores pares
diccionario.clear()         # Diccionario vacio

diccionario.keys()          # Extrae las claves
diccionario.values()        # Extrae valores
diccionario.items()         # Extrae key-values pares
diccionario.get('Dos')      # Extrae el valor de la clave

#Tecnicas de loopeo para la extraccion de keys values por separado
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
        print(k, v)

#%% Tuplas
print("""---------------- Tuplas --------------------
        Son lo mismo que las listas, a excepción que una vez declaradas las tuplas
        estas no se pueden modificar""")
tupla = (1,2,3,"La Pistola")# Creacion Tupla
tupla[3][4]                 # Accediendo a los elementos
tupla = tupla + (4,5,6)     # Agregando elementos
tupla.count(3)              # Cuenta cuantas veces se repiten los valores
tupla.index("La Pistola")   # Regresa el index del elemento de la tupla

