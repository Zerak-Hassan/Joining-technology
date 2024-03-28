import math
v=0.005
q=1100
thermal_conductivity=10
t=q/(2*math.pi*thermal_conductivity*v*(1660-20))
print(t*v*1000)