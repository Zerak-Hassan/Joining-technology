import math
import matplotlib.pyplot as plt
import numpy as np
import statistics
q=1100
v=0.005
iterations=10000
cooling_rates=list()
initial_temp=20
thermal_conductivity=10
T=1700
temp=list()
change=1700/iterations
for d in range(0,iterations):
    temp.append(T)
    cooling_rates.append((2*math.pi*thermal_conductivity*((T-initial_temp)**2))/(q/v))
    T=T-change

plt.plot(temp,cooling_rates)
plt.gca().invert_xaxis()
plt.xlabel("Tempreature [deg C]")
plt.ylabel("Cooling Rate [deg C/s]")
plt.show()
print(statistics.mode(cooling_rates),max(cooling_rates),statistics.mean(cooling_rates))