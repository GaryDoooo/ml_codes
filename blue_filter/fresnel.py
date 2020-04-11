import math
import matplotlib.pyplot as plt


def fresnel_R(theta, n1=1, n2=1.5):
    # theta is Theta incidence
    theta = theta / 180 * math.pi
    cos_theta_t = math.sqrt(
        1 - (n1 / n2 * math.sin(theta))**2
    )
    Rs = ((n1 * math.cos(theta) - n2 * cos_theta_t) /
          (n1 * math.cos(theta) + n2 * cos_theta_t)
          )**2
    Rp = ((n1 * cos_theta_t - n2 * math.cos(theta)) /
          (n1 * cos_theta_t + n2 * math.cos(theta))
          )**2
    return Rs, Rp


def two_surface_fresnel(theta, n1=1, n2=1.5):
    Rs, Rp = fresnel_R(theta, n1, n2)
    R = (Rs + Rp) / 2
    T = 1 - R
    return 1 - T**2


def one_surface_fresnel(theta, n1=1, n2=1.5):
    Rs, Rp = fresnel_R(theta, n1, n2)
    return (Rs + Rp) / 2


def main():
    result_theta = []
    result_R = []
    for theta in range(0, 90, 5):
        result_theta.append(theta)
        result_R.append(
            two_surface_fresnel(theta)
        )

    fig, ax1 = plt.subplots()
    ax1.set_xlabel('theta')
    ax1.set_ylabel('Reflection of two interfaces')
    ax1.plot(result_theta, result_R, "r--")
    plt.savefig('result/fresnel.svg')


if __name__ == "__main__":
    main()
