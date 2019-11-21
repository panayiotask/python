import numpy as no
import matplotlib.pyplot as plt

# 1
#plt.plot(range(10))
#plt.show()

# 2
t=list(range(0,7))
co2=[250,265,272,260,300,320,389]
plt.plot(t, co2, 'b--')
plt.xlabel('Time (decade)')
plt.ylabel('CO2 concentration (ppm)')
plt.title('CO2 vs time')

temp=[14.1,15.5,16.3,18.1,17.3,19.1,20.2]
plt.plot(t, temp, 'r--')

plt.savefig('co2_temp.pdf')

plt.show()

