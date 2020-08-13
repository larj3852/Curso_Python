"""
DICCIONARIO --> Tipo de dato que almacena un conjunto de datos en formato clave->valor
                Es parecio a un array asociativo u objeo json
"""
persona = {"nombre":"victor","apellidos":"robles","web":"victorrobles.es"}
print(persona)
print(persona["web"])

#Combinacion de Lista con diccionarios
contactos = [{"nombre":"antonio","email":"antonio.com"},
            {"nombre":"Luis","email":"luis.com"},
            {"nombre":"salvador","email":"salvador.com"}]

print(contactos[0]['nombre'])

for contacto in contactos:
    print(f"Nombre: {contacto['nombre']}, email: {contacto['email']}")