import math

v1 = (3,4)
v2 = (5,12)

#1
r_v1 = math.sqrt(v1[0]**2 + v1[1]**2)
r_v2 = math.sqrt(v2[0]**2 + v2[1]**2)

if r_v1 > r_v2:
    print("v1 is longer")
elif r_v1 < r_v2:
    print("v2 is longer")
else:
    print("vectors have the same length")