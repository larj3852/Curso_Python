#Programacion orientada a objetos

#Clase --> Molde para crear objetos tipo coche

#%% DECLARACION DE LA CASE---------------------------------------------
class Coche:
    # ATRIBUTOS {Caracteristicas del coche} (valores establecidos por defecto)
    color = "Rojo"  
    marca = "Ferrari"
    modelo = "Aventador"
    velocidad = 300
    caballaje = 500
    plazas = 2
    
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

# fin de la definició de la clase

#%% USO DE LA CLASE ------------------------------------------------------

coche=Coche()
print(coche)
print(coche.marca)
print(coche.color)
print(f"Velocidad actual: {coche.velocidad}")
coche.acelerar()
coche.acelerar()
print(f"Velocidad actual: {coche.velocidad}")
coche.frenar()
print(f"Velocidad actual: {coche.velocidad}")

    

# %% USO DE METODOS GET/SET --------------------------------------

coche = Coche()
coche.setColor("Amarillo")
coche.setModelo("Murcielago")
print(coche.getColor())
print(coche.getModelo())


# %% MULTIPLES OBJETOS --------------------------------------------
#Creacion de mas objetos
coche2 = Coche()
coche2.setModelo("Gallardo")
coche2.setColor("Rosa")
print(f"{coche2.getColor()} {coche2.getModelo()}")

coche3 = Coche()
coche3.setModelo("Mustang")
coche3.setColor("Dorado")
print(f"{coche3.getColor()} {coche3.getModelo()}")

# %% 

