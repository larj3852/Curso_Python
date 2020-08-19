"""
Modulo loggin: Informa de una manera mas eficiente lo que está pasando en la ejecucion
                En lugar de usar la ñerez del print
"""
import threading
import time
import datetime
import logging

logging.basicConfig(level=logging.INFO,format='[%(levelname)s] (%(threadName)-s) %(message)s')
#Definicion de funciones
def consultar(id):
    logging.info("Consultando para el id: "+str(id))
    time.sleep(2)
    pass

def guardar(id,valor):
    logging.info("Consultando para el id: "+str(id)+" data "+valor)
    time.sleep(5)
    pass

#Tiempo Inicio
tiempo_init = datetime.datetime.now()

#%% #Declaracion de hilos
t1 = threading.Thread(name="Hilo_1",target=consultar,args=(1, )) #NOTA: Para que respete el concepto de tupla
t2 = threading.Thread(name="Hilo_2",target=guardar,args=(1,"Ahora"))

#Ejecuciones en paralelo
t1.start()  #Hilo secundario 1 
t2.start()  #Hilo secundario 2

#Ejecuciones en serie
t1.join()   #Join adjunta la ejecución del hilo al hilo principal, haciendo lineal 
t2.join()   #El proceso

#%% Programación lineal
#consultar(1)
#guardar(1,"Ahora")

#%% Tiempo Final
tiempo_fin = datetime.datetime.now()

#Impresion Tiempo transcurrido
print(f"Tiempo transcurrido: {tiempo_fin-tiempo_init}")