import numpy as np

# 1
arr=np.array([range(4), range(10,14)])
print(arr)
print(arr.shape)
print(arr.size)
print(arr.min(), arr.max())

# 2
print(arr.reshape(2,2,2)) #print array reshaped
print(arr.transpose()) #print array transposed
print(arr.flatten()) #print array flattened
print(arr.astype(np.float)) #print array converted to float
