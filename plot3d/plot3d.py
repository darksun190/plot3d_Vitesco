
import matplotlib.pyplot as plt
import  numpy as np
from mpl_toolkits.mplot3d import Axes3D




n_angles = 180
radius = 65
angles = np.linspace(0,np.pi / 6,n_angles)
x1 = radius * np.cos(angles)
y1 = radius * np.sin(angles)
n_z1 = 80
n_z2 = 40
n_z3 = 60
h_z1 = 10
h_z2 = 100
h_z3 = 120
z1 = np.concatenate((np.linspace(1,h_z1,n_z1) , np.linspace(h_z1,h_z2,n_z2),np.linspace(h_z2,h_z3,n_z3)),axis=0)

x2 = (radius-5) * np.cos(angles)
y2 = (radius-5) * np.sin(angles)
z2 = np.concatenate((np.linspace(1,h_z1,n_z1) , np.linspace(h_z1,h_z2,n_z2),np.linspace(h_z2,h_z3,n_z3)),axis=0)

fig = plt.figure()
ax = fig.gca(projection='3d')
ax.scatter(x1,y1,z1,linewidth=0.1)
ax.scatter(x2,y2,z2,linewidth=0.1)

plt.xlim(0,radius * 1.2)
plt.ylim(0,radius * 1.2)
plt.show()
