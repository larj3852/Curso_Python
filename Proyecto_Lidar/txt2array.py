#%%
import numpy as np
import matplotlib.pyplot as plt
import os
#%%
#   os.getcwd()
#   os.listdir('.')
#   cadena.startswith("Bienvenido") 
print(os.path.exists("txt2array.py"))

lista =[]
with open("Sets/prueba7.txt","r") as file:
    a=file.read()
    for linea in a.split("\n"):
        line = linea.split("\t")
        try:
            lista.append([float(line[0]),float(line[1]),float(line[2])])
        except ValueError:
            continue


    lista=np.array(lista)

print(np.shape(lista))
file.close()


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(0, 0, 0, marker='.')
plt.grid(True)

ax.scatter(lista[:,0], lista[:,1], lista[:,2], marker='.')

ax.set_zlim((-100,100))
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
ax.set_ylim(-1,300)
plt.show()
