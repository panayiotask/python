import numpy as np
import numpy.ma as MA

# 1
data=range(10)
m_array=MA.masked_array(data, fill_value=-999)

print(m_array)

print(m_array, m_array.fill_value)

m_array[2]=MA.masked

print(m_array)

print(m_array.mask)

narr=MA.masked_greater(m_array, 7)

print(narr)

print(narr.fill_value)

x=MA.filled(narr)
print(x)
print(type(x))

# 2
data=range(8)
m1=MA.masked_array(data)
print(m1)

m2=np.reshape(m1,(2,4))
print(m2)
