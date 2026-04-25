import numpy as np
array=np.array([
    [76,79,76,91,99],
    [79,79,80,89,94],
    [88,89,81,85,87],
    [85,87,83,95,87],
    ])
print(array)
avg1=np.mean(array,axis=1)
print(avg1)
avg2=np.mean(array,axis=0)
print(avg2)
high_avg=np.max(avg1)
print(high_avg)
print(array[array>75])