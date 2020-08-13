
#CONSTRUCTOR --> Metodo especial en una clase y se suele utilziar para dar atributos al
#                crearlo
#%% DECLARACION DE LA CASE---------------------------------------------
class Coche:
    # ATRIBUTOS {Caracteristicas del coche} (valores establecidos por defecto)
    color = "Rojo"  
    marca = "Ferrari"
    modelo = "Aventador"
    velocidad = 300
    caballaje = 500
    plazas = 2
    __atributoprivado = 34  #ATRIBUTO PRIVADO
    
    #Sintaxis Constructor
    def __init__ (self,color,marca,modelo,velocidad,caballaje,plazas):
        self.color = color
        self.marca = marca
        self.modelo = modelo
        self.velocidad = velocidad
        self.caballaje = caballaje
        self.plazas = plazas


    #Metodos --> Acciones que hace el objeto (Coche)
    def acelerar(self):     #Self--> palabra reservada para acceder a todos los atributos
        self.velocidad += 1
    
    def frenar(self):
        self.velocidad -= 1
    
    def getVelocidad (self):
        return self.velocidad
    
    #Metodos getter setter
    def setColor(self, color):
        self.color = color

    def getColor(self):
        return self.color
    
    def setModelo(self,modelo):
        self.modelo = modelo

    def getModelo(self):
        return  self.modelo
    
    def getMarca(self):
        return self.marca
    def setMarca(self,marca):
        self.marca = marca
    
    def getInfo(self):
        info = "---- Informacion Coche ----"
        info += "\n Color "+ self.getColor()
        info += "\n Marca "+ self.getMarca()
        info += "\n Modelo " + self.getModelo()
        info += "\n Velocidad " + str(self.getVelocidad())

        return info
    
    def getPrivado (self):
        return self.__atributoprivado

# fin de la definició de la clase