#%% Crear carpeta
import os
#Creacion de carpeta
if not os.path.isdir("./micarpeta"):
    os.mkdir("./micarpeta") #. significa ruta actual

else:
    print("Ya existe directorio")

#%% Eliminar directorio

os.rmdir("./micarpeta")

# %% Copiar una carpeta

import shutil
ruta_original = "./micarpeta"     #Original
ruta_nueva =    "./micarpeta_COPIADA"   #Copiado
shutil.copytree(ruta_original,ruta_nueva)

#os.rmdir 
# %% Contenido de la carpeta
import os
print("Contenido de carpeta:")
contenido = os.listdir('./micarpeta')
print(contenido)

for fichero in contenido:
    print(f"fichero: {fichero}\n")

# %%
