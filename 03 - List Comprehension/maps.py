"""
maps

@description        map() function returns a map object(which is an iterator) of the results 
                    after applying the given function to each item of a given iterable 
                    (list, tuple etc.)
"""

# Ejemplo 1-->  Python program to demonstrate working of map. 
def addition(n): # Return double of n 
    return n + n 
# We double all numbers using map() 
numbers = (1, 2, 3, 4) 
result = map(addition, numbers) 
print(list(result)) #[2, 4, 6, 8]

#   Ejemplo 2 --> Double all numbers using map and lambda 
numbers = (1, 2, 3, 4) 
result = map(lambda x: x + x, numbers) 
print(list(result)) #[2, 4, 6, 8]

#   Ejemplo 3 --> Add two lists using map and lambda 
numbers1 = [1, 2, 3] 
numbers2 = [4, 5, 6] 
result = map(lambda x, y: x + y, numbers1, numbers2) 
print(list(result))    #[5, 7, 9]

# Ejemplo 4 -->  List of strings 
l = ['sat', 'bat', 'cat', 'mat'] 
  
# map() can listify the list of strings individually 
test = list(map(list, l)) 
print(test) #[['s', 'a', 't'], ['b', 'a', 't'], ['c', 'a', 't'], ['m', 'a', 't']]