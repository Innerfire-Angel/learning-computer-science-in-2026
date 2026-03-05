import matplotlib.pyplot as plt
import numpy as np

#Даны 3 вектора
v1 = (3,1)
v2 = (0,4)
v3 = (-2,2)

vector1 = np.array(v1)
vector2 = np.array(v2)
vector3 = np.array(v3)

#1 находим результирующий вектор
result_vector = vector1 + vector2 + vector3
print(result_vector)

#2 рисуем вектор
fig, ax = plt.subplots()

ax.quiver(0, 0, result_vector[0], result_vector[1], angles='xy', scale_units='xy', scale=1, color='blue')

ax.set_xticks(range(-1, 9))
ax.set_yticks(range(-1, 9))

plt.grid(True)
plt.show()