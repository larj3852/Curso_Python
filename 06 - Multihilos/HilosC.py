import threading
import time
import logging

logging.basicConfig(level=logging.INFO,format='[%(levelname)s] (%(threadName)-s) %(message)s')

class Hilo1(threading.Thread):
    def __init__(self, nombre_hilo,id_persona,data):
        #Se tiene que inicializar Thread para que funque
        threading.Thread.__init__(self,name=nombre_hilo,target=Hilo1.run)
        #Si se quisiera evitar escribir la funcion run  NOTA-> Se debe agregar el self ya que se está dentro de una clase
        #threading.Thread.__init__(self,name=nombre_hilo,target=Hilo1.consultar,args(self, id,data))
        self.nombre_hilo = nombre_hilo
        self.id_persona = id_persona
        self.data = data
    
    def run(self):
        self.consultar(self.id_persona)
    
    def consultar(self,id_persona):
        logging.info("Consultando para el id: "+str(id))
        time.sleep(2)
        return
#%% 

class Hilo2(threading.Thread):
    def __init__(self, nombre_hilo,id_persona,data):
        #Se tiene que inicializar Thread para que funque
        threading.Thread.__init__(self,name=nombre_hilo,target=Hilo2.run)
        self.nombre_hilo = nombre_hilo
        self.id_persona = id_persona
        self.data = data
    
    def run(self):
        self.guardar(self.id_persona)
    
    def guardar(self,id_persona):
        logging.info("Consultando para el id: "+str(id))
        time.sleep(5)
        return