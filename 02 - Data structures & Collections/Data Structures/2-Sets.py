"""
Sets
@description    Son una colección de elementos desordenados que son unicos.
                Significa que incluso si la data se repite mas de una vez, estos entraran en el set
                solo una vez. 
"""

my_set = {1, 2, 3, 4, 5, 5, 5}      #   Creación de un set
my_set2 = {3, 4, 5, 6}
print(my_set)
my_set.add(6)                       #   Add element to set
print(my_set)
my_set.union(my_set2)               #   Union/concatenacion de sets
my_set.intersection(my_set2)        #   Conserva los valores que son comunes
my_set.difference(my_set2)          #   Conserva los valores que son diferentes del 1er set
my_set.symmetric_difference(my_set2)#   Hace lo mismo que diferencia
