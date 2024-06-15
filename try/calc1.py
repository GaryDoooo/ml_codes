from math import *
R = 1
alpha = pi / 4

surface = 0
dx = 0.001

for x in range(0, int((R - R * cos(alpha)) * 1000) + 1):
    x = x / 1000
    theta = acos((x + R * cos(alpha)) / R)
    surface += 2 * pi * x * dx / sin(theta)

print(surface)



