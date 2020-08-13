#Listas
peliculas = ["Batman","Superman","Spider-man"]

#Tuplas 
cantantes = ("kanyie","Tupac","J Lo")
cantantes = list(cantantes)

#Indices

print(peliculas[1]) #Superman
print(peliculas[2]) #Spiderman
print(cantantes[1:3]) #Ultimos 2

#Agregar elementos  a una lista
cantantes.append("Ricky martin")
print(cantantes)

#Recorrer y mostrar lista
print ("----- Lista Peliculas ----")
for pelicula in peliculas:
    print (f"{peliculas.index(pelicula)}. {pelicula} \n")


#Listas Multidimencionales
contactos = [   ["Jesus",23],
                ["Juan",34],
                ["Ana",21] ]
for contacto in contactos:
    print(contacto[0])
    print(contacto[1])
    print(contacto)