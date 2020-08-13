#Funciones Predifinidas -----------------------------------------------

    #Detectar el tipo
print("#Detectar el tipo valor")
nombre = "Jesus"
comprobar = isinstance(nombre,str)
if comprobar:
    print("String")
else:
    print("No String")
    
    #Limpiar espacios
print("#Limpiar espacios")
frase = "       La pata del Mameitor    "
print(frase)
print(frase.strip())

    #Eliminar variables
print("#Eliminar variables")
year = 2020
print (year)
del year

    #Encontrar caracteres
print("Encontrar caracteres")
frase = "La pata del mameitor"
print(frase.find("pata"))

    #Remplazar palabras en un string
print("# Remplazar palabras en un string")
nuevafrase = frase.replace("pata","piel")
print(nuevafrase)

    #Mayusculas Minusculas
print("# Mayusculas/minuculas")
print(nombre.lower())
print(nombre.upper())