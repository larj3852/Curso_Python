from io import open


#Abrir archivo
archivo = open("fichero_texto.txt","a+")

#Ruta absoluta
import pathlib
ruta = str(pathlib.Path().absolute())+"/fichero_texto.txt"
print(ruta)
archivo = open(ruta,"a")

#Escribir 
archivo.write("Texto introducido desde python\n")

archivo.close()

#Leer contenido
archivo = open(ruta,"r")
contenido = archivo.read()
archivo.close()
print(contenido)

#Extraer lista
archivo = open(ruta,"r")
lista = archivo.readlines()
print(lista)
archivo.close()

for frase in lista:
    if not frase.isnumeric():
        print("- "+frase.upper()) #Mayusculas

for frase in lista:
    lista_frase = frase.split() #Convertir en lista
    print(lista_frase)

for frase in lista:
    print(frase.center(50))     #ESPACIADO

#%% #Copiar archivos
import shutil
ruta_original = str(pathlib.Path().absolute())+"/fichero_texto.txt"     #Original
ruta_nueva =    str(pathlib.Path().absolute())+"/fichero_copiado.txt"   #Copiado
shutil.copyfile(ruta_original,ruta_nueva)
    #Ruta alternativa
ruta_alternativa = str(pathlib.Path().absolute())+"/07 - Ejercicios/fichero_alternativo.txt"
shutil.copyfile(ruta_original,ruta_alternativa)

#%% Mover archivo
        #Cambio: Se elimimna el archivo fichero_copiado.txt por el fichero_copiado_NUEVO.txt
ruta_original = str(pathlib.Path().absolute())+"/fichero_copiado.txt"
ruta_nueva =    str(pathlib.Path().absolute())+"/fichero_copiado_NUEVO.txt"
shutil.move(ruta_original,ruta_nueva)

#%% Eliminar
import os
ruta_nueva =    str(pathlib.Path().absolute())+"/fichero_copiado_NUEVO.txt"
os.remove (ruta_nueva)

#%% Comporbar si archivo existe
import os
#print(os.path.abspath("./"))  #-->Variante de ruta absoluta el # de puntos en el argumento
#Es para coletactar la ruta hasta una subcarpepta
ruta_comprobar = os.path.abspath("./")+"/fichero_texto.txt" 
if os.path.isfile(ruta_comprobar):
    print("El archivo existe")
else:
    print("El archivo no existe")


# %%
