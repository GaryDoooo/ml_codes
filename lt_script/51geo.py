from math import pi, tan, sin, cos

T = 1.7
a = 50.6 / 180 * pi
L = T / tan(a)
N = 38


def extrude(p_list, Z=48):
    print("ExtrudedPrism ", end=" ")
    for p in p_list:
        print("XYZ %.4f,%.4f,0" % p, end=" ")
    print("XYZ %.4f,%.4f," % p_list[-1] + str(Z), end=" ")
    print("XYZ %.4f,%.4f," % p_list[-2] + str(Z))


def trim_by_angle(x, y, z, a):
    a = a / 180 * pi
    x1 = cos(a) + x
    y1 = sin(a) + y
    print(
        "trimsolid xyz", "%.4f,%.4f,%.4f" %
        (x, y, z), "xyz %.4f,%.4f,%.4f" %
        (x1, y1, z))


ext = extrude

#  ext([(0, 0), (0, 1), (1, 1)])
ext([(0, 0), (0, T), (L, T)])
x = 0
for i in range(N):
    x1 = x
    x2 = x1 + L
    x3 = x2 + L
    ext([(x1, 0), (x2, 0), (x3, T), (x2, T)])
    x = x2

trim_by_angle(x, 0, 0, -86)

#  x1 = x
#  x2 = x + L
#  ext([(x1, 0), (x2, T), (x2 + 10, T), (x2 + 10 + L, 0)])
