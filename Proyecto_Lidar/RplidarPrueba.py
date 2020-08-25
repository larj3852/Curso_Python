#%%
from PaqueteLocal import rplidar
from time import sleep
import numpy as np
import matplotlib.pyplot as plt
#%%
lidar = rplidar.RPLidar('COM4')
sleep(1)
info =lidar.get_info()
print(info)

lidar.get_health()
# plt.figure(1)
# plt.scatter(0,0,cmap="red")
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(0, 0, 0, marker='.'); 
plt.grid(True)
process_scan = lambda scan: None
#Angulos en Z
a=np.arange(90,30,-5)
b=['Orig']
for i in a: b.append(str(i))
phi=a*np.pi/180 #90 a 60
print(b)

#%%
for j in range(0,10):
    lidar.connect()
    lidar._serial_port.flushInput()
    print(len(lidar._serial_port.read_all()))
    
    i=0
    for scan in lidar.iter_scans():
        process_scan(scan)
        i+=1

        if i>= 3:
            break
    print(len(scan))
    scan=np.array(scan)
    x = np.cos(np.pi-scan[:,1]*(np.pi/180))*np.sin(phi[j])*scan[:,2]/10
    y = np.sin(np.pi-scan[:,1]*(np.pi/180))*np.sin(phi[j])*scan[:,2]/10
    #Nota, como el lidar está en 90° se le inverte la función sin(phi)
    z = np.cos(phi[j])*scan[:,2]/10
    #plt.scatter(x,y)
    ax.scatter(x, y, z, marker='.')
    lidar.stop()
    lidar.stop_motor()
    lidar.disconnect()
    entrada = input("Pausa Presiona tecla")

ax.legend(b)
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
ax.set_ylim(-1,300)
fig.show()
"""
1.5+np.pi-scan[:,1]*(np.pi/180)

fig=plt.figure()
ax = fig.add_subplot(111, projection='polar')
#ax.set_rorigin(-2.5)
c=ax.scatter(1.5*np.pi-scan[:,1]*(np.pi/180),scan[:,2])
#plt.polar(+np.pi/2-scan[:,1]*(np.pi/180),scan[:,2],label="Lidar 90°",linestyle="dashed")
"""
# %%
fig
# %% Terminar conexion
# lidar.stop_motor()
# lidar.disconnect()
lidar._serial_port._close()
del(lidar)
del(fig)

# %%
