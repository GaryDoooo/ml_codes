from math import sin, asin, pi
from numpy import nan


def g2a(a, n=1.52):
    """"
    Glass incident angle to air output
    angle, input in degrees
    """
    try:
        if abs(sin(a / 180 * pi) * n) <= 1:
            return asin(sin(a / 180 * pi) * n) / pi * 180
        else:
            return nan
    except BaseException:
        print(sin(a / 180 * pi) * n)


def a2g(a, n=1.52):
    """
    Air incident angle to glass output
    angle, input in degrees
    """
    return asin(sin(a / 180 * pi) / n) / pi * 180


def TIRa(n=1.52):
    """
    TIR angle inside a high
    index media
    """
    return asin(1 / n) / pi * 180


if __name__ == "__main__":
    print(a2g(8.12))
