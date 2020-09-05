"""
    Permiten agregarle mayor funcionaliad a una function
    Es una funcion que va a recibir una función como parametro,
    y creará otra funcion

"""
#%% STRUCTURA BASICA 
"""**********************DECORADOR SIN ARGUMENTOS I************************"""

#Funcion decoradora
def decoradora(func):
    def nueva_funcion(*args,**kwargs):  #Para que nuestra función pueda recibir parametros
        print("Primero hago algo")
        func()
        print("Hago otra cosa")
    return nueva_funcion

#Funcion normal ya decorada
@decoradora #Decoradors
def saludame():
    print("Hola mundo")

saludame()  #Ejecucion

#%% DECORADOR SIN ARGUMENTOS II
"""**********************DECORADOR SIN ARGUMENTOS II************************"""
# importing libraries 
import time 
import math 

# decorator to calculate duration 
# taken by any function. 
def calculate_time(func): 
	
	# added arguments inside the inner1, 
	# if function takes any arguments, 
	# can be added like this. 
	def inner1(*args, **kwargs): 

		# storing time before function execution 
		begin = time.time() 
		
		func(*args, **kwargs) 

		# storing time after function execution 
		end = time.time() 
		print("Total time taken in : ", func.__name__, end - begin) 

	return inner1 



# this can be added to any function present, 
# in this case to calculate a factorial 
@calculate_time
def factorial(num): 

	# sleep 2 seconds because it takes very less time 
	# so that you can see the actual difference 
	time.sleep(1) 
	print(math.factorial(num)) 

# calling the function. 
factorial(5) 

#%% DECORADOR CON ARGUMETOS
"""**********************DECORADOR CON ARGUMENTOS I************************"""

def decoradora(func):
    def nueva_funcion(*args,**kwargs):  #Para que nuestra función pueda recibir parametros
        print("Primero hago algo")
        print("Hago otra cosa")
        resultado = func(*args,**kwargs)
        return resultado
    return nueva_funcion

@decoradora
def operaciones(a,b):
    return a*b

print(operaciones(5,3))
# %% DECORADOR CON ARGUMENTOS II
"""**********************DECORADOR CON ARGUMENTOS II************************"""

def hello_decorator(func): 
	def inner1(*args, **kwargs): 
		
		print("before Execution") 
		
		# getting the returned value 
		returned_value = func(*args, **kwargs) 
		print("after Execution") 
		
		# returning the value to the original frame 
		return returned_value 
		
	return inner1 


# adding decorator to the function 
@hello_decorator
def sum_two_numbers(a, b): 
	print("Inside the function") 
	return a + b 

a, b = 1, 20

# getting the value through return of the function 
print("Sum =", sum_two_numbers(a, b)) 


# %%
