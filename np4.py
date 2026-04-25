import numpy as p
palani=p.array([568,955,458,786,249,549,532,573,513,950])
condition=palani>500
print(condition)

total=palani[palani>500]
print(total)

print(f"passed:{p.sum(palani)}")
indexing=p.where(palani>50)
print(indexing[0])

print(p.max(palani))