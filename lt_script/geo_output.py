from utilities import g2a, TIRa
#  from math import pi
from numpy import nan


def theta2b(theta, n=1.52):
    b_max = 90 - 2 * theta
    alpha_TIR = 90 - TIRa(n=n)
    b_min = b_max - alpha_TIR
    #  print(b_max,b_min)
    return (g2a(b_min, n=n),
            g2a(b_max, n=n))


def var_theta(n=1.52):
    for theta in range(5, 46, 5):
        print(theta, "(%.1f, %.1f)" % theta2b(theta, n=n))
    for theta in range(20, 41):
        print(theta, "(%.1f, %.1f)" % theta2b(theta, n=n))


def alpha2b(alpha, theta=28, n=1.52):
    """
    from alpha to 0th order output angles in air.
    """
    b0 = 2 * theta + alpha - 90
    if abs(b0) >= TIRa(n=n):
        return alpha2b(90 - abs(b0), theta=theta, n=n)
    return g2a(b0, n=n)


def alpha2b1(alpha, theta=28, n=1.52):
    """
    from alpha to 1st order output angles in air
    """
    if alpha == theta:
        return nan
    #  if alpha>theta:
    #      b=90-alpha
    #      return alpha2b(2*theta+b-90,theta=theta,n=n)
    return alpha2b(2 * theta - alpha, theta=theta, n=n)


def var_alpha(theta=28, n=1.52):
    for alpha in range(10, int(90 - TIRa(n=n))):
        print(alpha, "%.2f %.2f" %
              (alpha2b(alpha, theta=theta, n=n),
               alpha2b1(alpha, theta=theta, n=n))
              )


if __name__ == "__main__":
    var_theta(n=2)
    var_alpha(n=2)
