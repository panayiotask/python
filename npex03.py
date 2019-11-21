import numpy as np

# 1
a=np.array([range(4), range(10,14)])

b=np.array([2,-1,1,0])

print(a)
print(b)
print(a*b)

b1=b*100

b2=b*100.0

print(b1)
print(b2)

print(b1==b2)

print(b1.dtype)
print(b2.dtype)

# 2
arr=np.array([range(0,10)])
#print(arr)

print(arr<3)
print(np.less(arr,3))

condition=np.logical_or(arr<3, arr>8)

arr_new=np.where(condition, arr*5, arr*-5)
print(arr_new)

# 3
# function that calculates the wind resultant
def wind(u,v):
    output=(u**2+v**2)**0.5
    condition=output<0.1
    output2=np.where(condition, 0.1, output)
    return output2

u=np.array([[4,5,6],[2,3,4]])
v=np.array([[2,2,2],[1,1,1]])
print(wind(u,v))

u2=np.array([[4,5,0.01],[2,3,4]])
v2=np.array([[2,2,0.03],[1,1,1]])
print(wind(u2,v2))








