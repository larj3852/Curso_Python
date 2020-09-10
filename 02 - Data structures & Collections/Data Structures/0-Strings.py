"""
https://uniwebsidad.com/libros/python/capitulo-6/metodos-de-formato
"""

#%%                     Metodos de formato

"""====================================Metodos de Formato====================================="""
cadena = "bienvenido a mi aplicación" 

cadena.capitalize()     #   Primera letra en mayuscula
cadena.lower()          #   Todas minusculas
cadena.upper()          #   Todas mayusculas
cadena.swapcase()       #   Invertir mayusculas y minusculas
cadena.title()          #   Convertir cadena en titulo 1° letra de cada palabra en mayuscula
cadena.center(50, "=")  #   Centrar cadena      #Resultado "===========Bienvenido a mi aplicación============"
cadena.ljust(50, "=")   #   Alinear a la izquierdas
cadena.rjust(50, "=")   #   Alinear a la derecha

numero_factura = 1575   #   Rellenar un texto anteponiendo ceros
str(numero_factura).zfill(12) 

#%% 
"""====================================Metodos de busqueda====================================="""
cadena = "bienvenido a mi aplicación".capitalize()

#cadena.count("a", posicion_inicio, posicion_fin)
cadena.count("a")       #   Contar numero de repeticiones
cadena.find("mi")       #   Encontar la primera secuencia   

#%%                     Metodos validacion

"""====================================Metodos de Validacion====================================="""

cadena = "bienvenido a mi aplicación".capitalize() 
#startswith("subcadena" [, posicion_inicio, posicion_fin])

cadena.startswith("Bienvenido")         #   Saber si una cadena comienza con una subcadena
cadena.endswith("Bienvenido", 0, 10)    #   Saber si una cadena finaliza con una subcadena determinada
cadena = "pepegrillo75"
cadena.isalnum()                        #   Saber si una cadena es alfanumérica
cadena.isalpha()                        #   Saber si una cadena es Saber si una cadena es alfabética
cadena = "7584" 
cadena.isdigit()                        #   Saber si una cadena es numérica
cadena = "pepe grillo"                  
cadena.islower()                        #   Saber si una cadena contiene solo minúsculas
cadena.isupper()                        #   Saber si una cadena contiene solo mayúsculas
cadena.isspace()                        #   Saber si una cadena contiene solo espacios en blanco
cadena.istitle()                        #   Saber si una cadena tiene Formato De Título

#%%                                   Metodos Sustitucion

"""==================================Metodos Sustitucion====================================="""
#   Dar formato a una cadena, sustituyendo texto dinámicamente

cadena = "bienvenido a mi aplicación {0}"                                   #Caso 1
cadena.format("en Python")              

cadena = "Importe bruto: ${0} + IVA: ${1} = Importe neto: {2}"              #Caso 2
cadena.format(100, 21, 121)

cadena = "Importe bruto: ${bruto} + IVA: ${iva} = Importe neto: {neto}"     #Caso 3
cadena.format(bruto=100, iva=21, neto=121) 

"Estimado Sr. nombre apellido:".replace(buscar, reemplazar_por)             #   Reemplazar texto en una cadena
cadena = "   www.eugeniabahit.com   "
cadena.strip(' ')               #   Eliminar caracteres a la izquierda y derecha de una cadena
cadena.lstrip("w." )            #   Eliminar caracteres a la izquierda de una cadena
cadena.rstrip( )                #   Eliminar caracteres a la derecha de una cadena

formato_numero_factura = ("Nº 0000-0", "-0000 (ID: ", ")")  #   Unir una cadena de forma iterativa
numero = "275" 
numero_factura = numero.join(formato_numero_factura) 
# Resultado:    Nº 0000-0275-0000 (ID: 275)

"http://www.eugeniabahit.com".partition("www.")     #   Partir una cadena en tres partes, utilizando un separador
# Resultado:    ('http://', 'www.', 'eugeniabahit.com') 
"python, guia, curso, tutorial".split(", ")         #   Partir una cadena en varias partes, utilizando un separador

#   Partir una cadena en en líneas
texto = """Linea 1                                  
Linea 2
Linea 3
Linea 4
"""
texto.splitlines() 









