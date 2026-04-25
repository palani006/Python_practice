import numpy as np
marks=np.array([52,45,88,45,62,50,])
marks_scaled=marks*1.1
print(marks_scaled)

internal=np.array([75,59,58,62,84,43])
external=np.array([58,69,45,87,95,73])
total=internal+external
print(total)

print(f"sum:{np.sum(marks)}")
print(f"mean:{np.mean(marks)}")
print(f"min:{np.min(marks)}")
print(f"max:{np.max(marks)}")
print(f"std{np.std(marks)}")
print(f"sqrt:{np.sqrt(marks)}")