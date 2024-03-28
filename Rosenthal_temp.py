import math
import matplotlib.pyplot as plt
v=0.005
q=1100
thermal_conductivity=10
t=0.1
T=list()
times=list()
for i in range (0,10000):
    p=(q/(2*math.pi*thermal_conductivity*v*t))-20
    if p > 1700:
        T.append(1700)
        times.append(t+1)
    elif p < 500:
        exit
    else:
        T.append(p)
        times.append(t+1)
    
    t=t+0.001
plt.plot(times,T)
plt.xscale('log')
plt.show()