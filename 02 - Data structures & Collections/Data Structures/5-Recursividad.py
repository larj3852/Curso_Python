"""
RECURSIVIDAD
En programación es una función que se llama así misma
"""

def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)


print(factorial(7))