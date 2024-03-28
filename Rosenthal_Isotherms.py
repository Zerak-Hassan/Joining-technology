#Rosenthal.py
import math
import matplotlib.pyplot as plt
import numpy as np
t_0=20
thermal_conductivity=10
v=0.005
q=1100
a=thermal_conductivity/(670*4420)
heat=list()
min_y=-0.03
max_y=0.03
min_x=-0.05
max_x=0.01
delta_x=0.0001
x_steps=int((max_x-min_x)/delta_x)
delta_y=0.0001
y_steps=int((max_y-min_y)/delta_y)
yi=np.linspace(min_y,max_y,y_steps)
xi=np.linspace(min_x,max_x,x_steps)
for y in range (0,y_steps):
    temp=list()
    for i in range(0,x_steps):
        R=math.sqrt(((xi[i])**2)+((yi[y])**2))
        try:
            temp.append((q/(2*(math.pi)*thermal_conductivity*R))*((math.e)**((-v/(2*a))*((xi[i])+R)))+t_0)
        except ZeroDivisionError:
            temp.append(100000000)
        if temp[i]>1700:
            temp[i]=1700
    heat.append(temp)
x = np.linspace(min_x*1000, max_x*1000,x_steps)
y = np.linspace(min_y*1000, max_y*1000,y_steps)
X, Y = np.meshgrid(x, y)
contour=plt.contourf(X,Y,heat, cmap="inferno", levels=50)
plt.colorbar(contour, label='Tempreature')
plt.xlabel("Distance from moving source along x axis [mm]")
plt.ylabel("Distance from y axis [mm]")
plt.plot(0,0,'bx')
plt.show()