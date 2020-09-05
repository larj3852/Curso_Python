"""
@description    List comprehensions are used for creating new lists from other iterables
                As list comprehensions return lists, they consist of brackets containing the expression, 
                which is executed for each element along with the for loop to iterate over each element.

@sintax         new_list = [expression for_loop_one_or_more conditions]
"""
#Ejemplo1 --> Finding squares using list comprehensions
print("Ejemplo1 --> Finding squares using list comprehensions")
numbers = range(10)
squares = [n**2 for n in numbers]
print(squares)

#Ejmplo 2 --> Find common numbers from two lists using list comprehension
print("Ejmplo 2 --> Find common numbers from two lists using list comprehension")
list_a = [1, 2, 3, 4];list_b = [2, 3, 4, 5]
common_num = [a for a in list_a for b in list_b if a == b]
print(common_num) # Output: [2, 3, 4]


#Ejemplo 3 --> Filtros
print("Ejemplo 3 --> Filtros")
list_a = ["Hello", "World", "In", "Python"]
small_list_a = [str.lower() for str in list_a]
print(small_list_a) # Output: ['hello', 'world', 'in', 'python']

#Ejemplo 4 --> Lista de listas
print("Ejemplo 4 --> Lista de listas")
list_a = [1, 2, 3]
square_cube_list = [ [a**2, a**3] for a in list_a]
print(square_cube_list) # Output: [[1, 1], [4, 8], [9, 27]]

#Ejemplo 5 -->  Iterating through a string Using for Loop
h_letters = []
for letter in 'human':
    h_letters.append(letter)
print(h_letters)    #['h', 'u', 'm', 'a', 'n']





