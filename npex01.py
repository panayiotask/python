# 1
import numpy as np
x=list(range(1,11))
print(x)
a1=np.array(x, np.int32)
print(a1, a1.dtype)
a2=np.array(x, np.float32)
print(a2, a2.dtype)

# 2
zer=np.zeros((2,3,4))
#print(zer)
ones=np.ones((2,3,4))
arr=np.arange(0,1000)
#print(arr)

# 3
a=np.array([2,3.2,5.5,-6.4,-2.2,2.4])
#print(a)
print(a[1])
print(a[1:4])

a=np.array([[2,3.2,5.5,-6.4,-2.2,2.4],
[1,22,4,0.1,5.3,-9],
[3,1,2.1,21,1.1,-2]])

print(a[:,3])
print(a[1:4, 0:4])
print(a[1:,2])
