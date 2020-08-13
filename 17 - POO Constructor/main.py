#%%
from coche import Coche

carro = Coche("Amarillo","Renault","Clio",300,500,4)
carro2 = Coche("Rosa","Camaro","Camaro",211,233,2)
carro3 = Coche("Verde","Seat","Panda",235,352,3)
print(carro.getColor())

# %%
print(carro.getInfo())
print(carro2.getInfo())
print(carro3.getInfo())

#%% Detectar Tipo objeto

if type(carro3)==Coche:
    print("Es un objeto")

#%% Atributos Publicos y privados

print(carro.getPrivado())
