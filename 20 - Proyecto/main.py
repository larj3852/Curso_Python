"""
Proyecto Python+sql:
    -Abrir asistente
    -Login o Registro
- Si elegimos registro,creará usuarioen la bbdd
- Si elegimos login, identificará al usuario y nos preguntará
    -Crear nota
    -Mostrar notas
    -Borrar
"""
#MENU
print("""
ACCIONES DISPONIBLES:
    - Registro
    - Login
""")
accion = input("¿Qué quieres hacer?")

from Usuarios import acciones

HazEl = acciones.Acciones()

#Registro
if accion == "registro":
    HazEl.registro()
#Login
elif accion == "login":
    HazEl.login()

