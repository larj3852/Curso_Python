"""
ARGUMENTOS OPCIONALES

Tipos de argumentos --> Para trabajar con los decoradores
Para que nuestra función acepte cualquier cantidad de parametros

*args        Argumentos
**kwargs      Key word argument
            Nos va a regresar un diccionario variables con un valor por defecto
"""
#%%
def suma(*args, **kwargs):
    return kwargs,args

print(suma("argumentos",23.33,21,a="Hola k ace?",c=True,d=45333))
#Devuelve una tupla con *args y un diccionario con **kwargs
#({'a': 'Hola k ace?', 'c': True, 'd': 45333}, ('argumentos', 23.33, 21))

#%% *args for variable number of arguments 
def myFun(arg1, *argv): 
    print ("First argument :", arg1) 
    for arg in argv: 
        print("Next argument through *argv :", arg) 
  
myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')  
#%% *kargs for variable number of keyword arguments 
  
def myFun(**kwargs):  
    for key, value in kwargs.items(): 
        print ("%s == %s" %(key, value)) 
  
# Driver code 
myFun(first ='Geeks', mid ='for', last='Geeks') 

# %%
