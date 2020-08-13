#%%
#Capturar excepciones y manejo de errores  en codigo suseptible a fallos

try:
    nombre = input("Ingrese nombre: ")

    if len(nombre)>1:
        nombre_usuario = "Nombre: " + nombre
    print (nombre_usuario)
except:
    print("Ha ocurrido un error, mete bien el nombre")

else:
    print("Todo ha funcionado correctamente")

finally: 
    print("fin de la iteración")    #Si hay error o no, esta sección se ejecuta

# %% Multiples excepciones
try:
    numero = int (input("Introduce numero para elevarlo al cuadrado: "))
    print("El cuadrado es "+str(numero**2))

except TypeError:
    print("Convierte tus cadenas a entero")
except ValueError:
    print("Introduce un numero")
except Exception as e:
    print(type(e))
    print ("Ha ocurrido un error: ",type(e).__name__)

# %% Excepciones Personalizadas
try:
    nombre = input("Introduce el nombre: ")
    edad = int(input("Introduce edad: "))

    if edad<5 or edad>100:
        raise ValueError("La edad introducida es real")
    elif len(nombre) <=1:
        raise ValueError("El nombre no está completo")
    else:
        print("Bienvenido")
except ValueError:
    print("Introduce los datos correctamente")

except Exception as e:
    print("Existe un error")


# %%
