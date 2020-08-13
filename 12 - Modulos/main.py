#https://docs.python.org/3/py-modindex.html
import Modulos
#from Modulos import calculadora
#from  Modulos import * #Todas las funciones
print (Modulos.calculadora(12,34))
print (Modulos.holamundo("Jesus"))

#Modulos Fechas
import datetime
print(datetime.date.today())
print(datetime.datetime.now())
fecha = datetime.datetime.now() #Devuelve objeto

print(fecha.year)
print(fecha.month)
print(fecha.day)
print(fecha.hour)
print(fecha.strftime("%d/%m/%Y, %H:%M:%S")) #Formato personalizado
print (datetime.datetime.now().timestamp())
