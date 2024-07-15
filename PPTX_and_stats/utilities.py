from scipy.special import gamma
from scipy import integrate
from scipy.stats import norm, shapiro, chi2
from functools import lru_cache
import numpy as np
from statsmodels.stats.diagnostic import normal_ad
from scipy.stats import t as t_dist
import statistics as stat
######### Own Modules ############
# from binomial import binomial
from chi_sq import chi2_test_stdev
from t_test import t_test_1sample


def mean_std_CIs(data, alpha=0.05, print_out=False, print_port=print):
    chi2_r = chi2_test_stdev(
        data,
        1,
        alpha=alpha,
        print_out=False,
        print_port=print_port)
    std_2side_range = chi2_r["95_range_from_S"]
    chi2_r = chi2_test_stdev(
        data,
        1,
        alpha=2 * alpha,
        print_out=False,
        print_port=print_port)
    std_1side_range = chi2_r["95_range_from_S"]

    t_r = t_test_1sample(
        data,
        1,
        alpha=alpha,
        print_out=False,
        print_port=print_port)
    mean_2side_range = t_r["u0_95range"]
    t_r = t_test_1sample(
        data,
        1,
        alpha=2 * alpha,
        print_out=False,
        print_port=print_port)
    mean_1side_range = t_r["u0_95range"]

    if print_out:
        print = print_port
        print("\n---- Confidence Intervals ----")
        pct = "%.1f%% " % (100 - 100 * alpha)
        print("For the population where the samples came from:\n")
        print(
            pct +
            "Prob that mean is in the range of (%.3f, %.3f)" %
            mean_2side_range)
        print(pct + "Prob that mean is less than %.3f." % mean_1side_range[1])
        print(
            pct +
            "Prob that mean is greater than %.3f.\n" %
            mean_1side_range[0])
        print(
            pct +
            "Prob that stdev is in the range of (%.3f, %.3f)" %
            std_2side_range)
        print(pct + "Prob that stdev is less than %.3f." % std_1side_range[1])
        print(
            pct +
            "Prob that stdev is greater than %.3f." %
            std_1side_range[0])
    return {"std 2side": std_2side_range, "std 1side": std_1side_range,
            "mean 2side": mean_2side_range, "mean 1side": mean_1side_range}


def pearson_correlation(x, y, alpha=0.05, print_out=True, print_port=print):
    print = print_port
    sx, sy = sum(x), sum(y)
    sx2 = sum([i * i for i in x])
    sy2 = sum([i * i for i in y])
    sxy = sum([i * j for i, j in zip(x, y)])
    n = len(x)
    x_bar, y_bar = sx / n, sy / n
#     r = [n(ΣXY) - (ΣX)(ΣY)] / √[n(ΣX²) - (ΣX)²][n(ΣY²) - (ΣY)²]
    r = (n * sxy - sx * sy) / ((n * sx2 - sx * sx) * (n * sy2 - sy * sy))**.5
#     Cov(X,Y) = Σ[(X - X̄)(Y - Ȳ)] / (n - 1)
    cov = sum([(i - x_bar) * (j - y_bar) for i, j in zip(x, y)]) / (n - 1)
    # https://zhiyzuo.github.io/Pearson-Correlation-CI-in-Python/
    # below confidence level calc
    #  print(r)
    if abs(r) < 1:
        r_z = np.arctanh(r)
    else:
        r_z = 10000
    se = 1 / np.sqrt(n - 3)
    z = norm.ppf(1 - alpha / 2)
    lo_z, hi_z = r_z - z * se, r_z + z * se
    lo, hi = np.tanh((lo_z, hi_z))
#     Calculate the t-statistic using the formula:
#     t = r * √((n-2) / (1-r²))
#     where n is the sample size
#     Determine the degrees of freedom (df):
#     df = n - 2
    if abs(r) == 1:
        p = a = b = theta = 0
    else:
        t = r * ((n - 2) / (1 - r * r))**.5
        p = (1 - t_dist.cdf(t, n - 2)) * 2

    # Calculate ellipse
# Source: https://education.illinois.edu/docs/default-source/carolyn-anderson/edpsy584/lectures/MultivariateNormal-beamer-online.pdf
# page 8 to p 22
# The numpy eigenvalue flipped order comparing to the slide
# Don't know why, swapping D1 and D0 seems work well.
# Important: chi2 cumulated prob uses 1-alpha, not 1-alpha/2

        xv = stat.variance(x)
        yv = stat.variance(y)
        D, E = np.linalg.eig([[xv, cov], [cov, yv]])
        X2 = chi2.ppf(1 - alpha, 2)
        x1 = (X2 * D[1])**.5 * E[0][0]
        y1 = (X2 * D[1])**.5 * E[0][1]
        x2 = (X2 * D[0])**.5 * E[1][0]
        y2 = (X2 * D[0])**.5 * E[1][1]
        a = (x1 * x1 + y1 * y1)**.5
        b = (x2 * x2 + y2 * y2)**.5
        theta = np.arctan(x1 / y1)

    if print_out:
        print("\n---- Pearson correlation alpha = %.3f ----" % alpha)
        print("Correlation coefficient: %.3f" % r)
        print("Confidence Interval (%.3f, %.3f)" % (lo, hi))
        print("Covariance: %.3f" % cov)
        print("p-value = %.3f\tN = %d" % (p, n))

    return {"r": r, "r_l": lo, "r_u": hi, "cov": cov, "p": p, "N": n,
            "ellipse": {"a": a, "b": b, "theta": theta}}


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


def group_df_to_list(df, y_key="Value", grp_key="Date"):
    return [list(df[df[grp_key] == gid][y_key])
            for gid in df[grp_key].unique()]


def group_by2factors(f1, f2, d):
    f2_d = [(i, j) for i, j in zip(f2, d)]
    gf1 = grouping_by_labels(f2_d, f1)
    res = []
    for sublist in gf1:
        factor = [i[0] for i in sublist]
        data = [i[1] for i in sublist]
        res.append(grouping_by_labels(
            data, factor))
    return res


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
    d3 = (2 * integral - calculate_d2(n)**2)**.5
    return d3  # round(d3,5)


def quantiles(input_data,
              percentiles=[100, 99.5, 97.5, 90, 75, 50,
                           25, 10, 2.5, 0.5, 0]):

    data = sorted([i for i in input_data])
    N = len(data)
    # x input is percentile
    def p(x): return (N + 1) * x / 100

    def value(i):
        if i <= 1:
            return data[0]
        if i >= N:
            return data[-1]
        a1 = data[int(i) - 1]
        a2 = data[int(i)]
        dec = i - int(i)
        return a1 + (a2 - a1) * dec

    res = []
    for i in percentiles:
        res.append(value(p(i)))
    return res
    ########## Result same to JMP  ##################


def norm_test(data, print_out=False, print_port=print):
    s1, p1 = shapiro(data)
    s2, p2 = normal_ad(np.array(data))
    if print_out:
        print = print_port
        print("\n---- Normality Test ----")
        print(f"Shapiro-Wilk test\tstats {s1:.3f}\tp-value {p1:.3f}")
        print(f"Anderson Darling test\tstats {s2:.3f}\tp-value {p2:.3f}")
    return {"shapiro s": s1, "shapiro p": p1, "AD s": s2, "AD p": p2}


def number_list(data, col_name="unknown", print_out=False,
                print_port=print):
    l = list(data)
    res = []
    for i in l:
        try:
            j = float(i)
            if j < 0 or j >= 0:
                res.append(j)
        except BaseException:
            pass
    if print_out:
        print = print_port
        print("Col: " +
              col_name +
              ", inputs: %d, valid numbers: %d" %
              (len(l), len(res)))
    return res


def number_2lists(d1, d2, col_name1="unknown",
                  col_name2="unknown", print_out=False,
                  print_port=print):
    l1 = list(d1)
    l2 = list(d2)
    x, y = [], []
    for i, j in zip(l1, l2):
        try:
            ii = float(i)
            jj = float(j)
            if jj < 0 or jj >= 0:
                if ii < 0 or ii >= 0:
                    x.append(ii)
                    y.append(jj)
        except BaseException:
            pass
    if print_out:
        print = print_port
        print(
            "Col " +
            col_name1 +
            " inputs: %d" %
            len(l1) +
            ", Col " +
            col_name2 +
            " inputs: %d." %
            len(l2))
        print("Valid number pairs: %d." % len(x))
    return x, y


def get_number(x):
    """x is a tk variable with get()"""
    try:
        return float(x.get())
    except BaseException:
        return None


if __name__ == "__main__":
    pearson_correlation([1, 2, 3], [2, 3, 1])
