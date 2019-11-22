import numpy as np
import matplotlib.pyplot as plt

# 1
fig, ax1=plt.subplots()
t=list(range(0,7))
co2=[250,265,272,260,300,320,389]
ax1.plot(t, co2, 'b--')
ax1.set_xlabel('x axis')
ax1.set_ylabel("[CO2]")
ax2=ax1.twinx()
temp=[14.1,15.5,16.3,18.1,17.3,19.1,20.2]
ax2.plot(t, temp, 'r--')
ax2.set_ylabel("Temp (degC)")
plt.show()
plt.savefig('co2_temp_2.pdf')

# 2
plt.subplot(1,3,1)
plt.plot(range(0,10,1))
plt.subplot(1,3,2)
plt.plot(range(10,0,-1))
plt.subplot(1,3,3)
z=[4]*10
plt.plot(z)
plt.show()
