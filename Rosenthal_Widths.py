import math
v=0.005
q=1100
initial_temp=0
fusion_temp=1700
haz_temp=550
r=math.sqrt((2*(q/v))/((haz_temp-initial_temp)*670*4420*math.pi*math.e))
print(r*1000)
