from scipy.special import gamma
import math
from scipy import integrate
from scipy.stats import norm
from functools import lru_cache

# https://en.wikipedia.org/wiki/Unbiased_estimation_of_standard_deviation
# to get unbiased std use normal std (mean.stdev) divided by c4 below
# n is the number of sample points.


def c4_values(n):
    return (2 / (n - 1))**.5 * gamma(n / 2) / gamma((n - 1) / 2)


def scale_factor_f(n):
    # https://www.jmp.com/support/help/en/17.0/#page/jmp/statistical-details-for-capability-indices-for-normal-distributions.shtml
    return 1 / 2 / (n - 1) / (1 / c4_values(n)**2 - 1)


def d2_values(n):
    # The d2 value here is same to the GRR d2 with k==15
    # Source: https://support.minitab.com/en-us/minitab/help-and-how-to/quality-and-process-improvement/control-charts/how-to/time-weighted-charts/ewma-chart/methods-and-formulas/unbiasing-constants-d2-d3-and-d4/
    #
    d2 = [0, 0,
          1.128379167,  # n = 2
          1.692568751,  # n = 3
          2.058751154,  # n = 4
          2.325929342,  # n = 5
          2.534413951,  # n = 6
          2.704000246,  # n = 7
          2.847000307,  # n = 8
          2.970000000,  # n = 9
          3.077999711,  # n = 10
          3.173000000,  # n = 11
          3.258000000,  # n = 12
          3.336000000,  # n = 13
          3.407000000,  # n = 14
          3.472000000,  # n = 15
          3.532000000,  # n = 16
          3.588000000,  # n = 17
          3.640000000,  # n = 18
          3.689000000,  # n = 19
          3.735000000   # n = 20
          , 3.778, 3.819, 3.858, 3.895, 3.931, 3.964, 3.997, 4.027, 4.057, 4.086, 4.113, 4.139, 4.165, 4.189, 4.213, 4.236, 4.259, 4.280, 4.301, 4.322, 4.341, 4.361, 4.379, 4.398, 4.415, 4.433, 4.450, 4.466, 4.482, 4.498]
    return d2[n] if n < 51 else d2[50]


def grouping_by_labels(data_list, grouping_list):
    data = [(i, j) for i, j in zip(grouping_list, data_list)]
    data.sort(key=lambda x: x[0])
    subgroup, res = [], []
    prev_i = None
    for i, j in data:
        if prev_i != i:
            res.append(subgroup)
            subgroup = []
        subgroup.append(j)
        prev_i = i
    res.append(subgroup)
    return res[1:]


@lru_cache
def calculate_d2(n):
    def integrand(x):
        return 1 - (1 - norm.cdf(x))**n - norm.cdf(x)**n

    d2, _ = integrate.quad(integrand, -10, 10)  # -float('inf'), float('inf'))
    return d2  # round(d2,5)


@lru_cache
def calculate_d3(n):
    def inner_integrand(x, y):
        return 1 - norm.cdf(y)**n - (1 - norm.cdf(x))**n + \
            (norm.cdf(y) - norm.cdf(x))**n

    def outer_integrand(y):
        result, _ = integrate.quad(
            lambda x: inner_integrand(
                x, y), -10, y)  # -float('inf'), y)
        return result

    integral, _ = integrate.quad(outer_integrand, -10, 10)
    # -float('inf'), float('inf'))
    d3 = math.sqrt(2 * integral - calculate_d2(n)**2)
    return d3  # round(d3,5)
