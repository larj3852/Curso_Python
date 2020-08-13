"""
SET --> Tipo de dato para tener una colección de valores, pero no tienen indice
        ni orden
"""

personas = {"Victor","manolo","francisco"}
prin(type(personas))
print(personas)
#Agregar
personas.add("Pedro")
print(personas)
#Eliminar
personas.remove("Francisco")
