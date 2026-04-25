import numpy as np
arr =np.array([
    [85,95,91],
    [81,54,94,],
    [85,64,67]
])
print(arr.shape)
print(arr[0])
print(arr[1][2])
print(arr[:,0])
avg=np.mean(arr,axis=1)
print(avg)
avg2=np.mean(arr,axis=0)
print(avg2)