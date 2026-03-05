import math
import matplotlib.pyplot as plt

v = (4, 3)

#1
r_v = math.sqrt(v[0]**2 + v[1]**2)
print(r_v)

#2
print(math.atan2(v[1], v[0]) * (180/math.pi))

#3
x = [0, v[0]]
y = [0, v[1]]
plt.plot(x, y)
plt.show()