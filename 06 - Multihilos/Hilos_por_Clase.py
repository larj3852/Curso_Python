"""
* Se hereda la clase threading.Thread como padre de las clases a declarar
* Se debe incluir un método "def run(self):" para que el hilo corra

* Si se quisiera evitar escribir la funcion run  
* NOTA-> Se debe agregar el self ya que se está dentro de una clase
* SINTAXIS:
    #threading.Thread.__init__(self,name=nombre_hilo,target=Hilo1.consultar,args(self, id,data))
"""
import threading
import time
import datetime
import logging
from HilosC import Hilo1,Hilo2



#Tiempo Inicio
tiempo_init = datetime.datetime.now()

#%%Hilos mediante clasescle

t1 = Hilo1("Hilo_1",1,"")
t2 = Hilo2("Hilo_2",1,"Hola Mundo")

t1.start() #Para que funcione este método debe declararse la fución RUN
t2.start()

t1.join()
t2.join()


#%% Tiempo Final
tiempo_fin = datetime.datetime.now()

#Impresion Tiempo transcurrido
print(f"Tiempo transcurrido: {tiempo_fin-tiempo_init}")