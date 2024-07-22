from math import pi, tan

T = 1.7
a = 28 / 180 * pi
L = T / tan(a)


def extrude(p_list, Z=48):
    print("ExtrudedPrism ", end=" ")
    for p in p_list:
        print("XYZ %.4f,%.4f,0" % p, end=" ")
    print("XYZ %.4f,%.4f," % p_list[-1] + str(Z), end=" ")
    print("XYZ %.4f,%.4f," % p_list[-2] + str(Z))


ext = extrude

#  ext([(0, 0), (0, 1), (1, 1)])
ext([(0, 0), (0, T), (L, T)])
x = 0
for i in range(8):
    x1 = x
    x2 = x1 + L
    x3 = x2 + L
    ext([(x1, 0), (x2, 0), (x3, T), (x2, T)])
    x = x2

x1 = x
x2 = x + L
ext([(x1, 0), (x2, T), (x2 + 10, T), (x2 + 10 + L, 0)])
