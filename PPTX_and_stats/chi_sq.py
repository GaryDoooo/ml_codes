import statistics as stat
import numpy as np
from scipy.stats import chi2, norm, kurtosis
from scipy.stats import f as f_dist
from math import log as ln
from prettytable import PrettyTable as PT


def chi2_test_stdev(data_list, s0, print_out=True):
    df = len(data_list) - 1
    S = stat.variance(data_list) * df
    stdev = stat.stdev(data_list)
    chi_sq = S / s0 / s0
    p = 1 - chi2.cdf(chi_sq, df)

    chi2_low0025 = chi2.ppf(0.025, df)
    chi2_high0975 = chi2.ppf(0.975, df)
    chi2_low005 = chi2.ppf(0.05, df)
    stdev_range_low = (chi2_low0025 * s0 * s0 / df)**.5
    stdev_range_high = (chi2_high0975 * s0 * s0 / df)**.5

    std_range_from_S = ((S / chi2_high0975)**.5, (S / chi2_low0025)**.5)

    std_from_S_high95 = (S / chi2_low005)**.5

    if print_out:
        print("Population stdev: %.2f\nSampled stdev: %.2f" % (s0, stdev))
        print("df = %d" % df)
        print("chi square = %.2f" % chi_sq)
        print("Prob of variation is bigger than the sample. p = %.2f" % p)
        print("Lower %%2.5 Chi square = %.2f  Top %%2.5 Chi square = %.2f" % (
            chi2_low0025, chi2_high0975))
        print(
            "%%95 confidence range of stdev: (%.2f, %.2f), when sampling %d times from a population with stdev of %.2f." %
            (stdev_range_low, stdev_range_high, df + 1, s0))
        print(
            "%%95 confidence range of the population stdev: (%.2f, %.2f), where the samples came from." %
            std_range_from_S)
        print(
            "%%95 confidence the population stdev lower than %.2f, where the samples came from." %
            std_from_S_high95)

    return {
        "p": p,
        "chi_sq": chi_sq,
        "stdev": stdev,
        "df": df,
        "95_chi2_range": (
            chi2_low0025,
            chi2_high0975),
        "95_range_from_P": (
            stdev_range_low,
            stdev_range_high),
        "n": df + 1,
        "95_range_from_S": std_range_from_S,
        "std_from_S_high95": std_from_S_high95}


def several_tests_stdev_2sided(l1, l2, print_out=True):
    var1 = stat.variance(l1)
    var2 = stat.variance(l2)
    u1 = stat.mean(l1)
    u2 = stat.mean(l2)
    s1 = stat.stdev(l1)
    s2 = stat.stdev(l2)
    n1 = len(l1)
    n2 = len(l2)
    # This replicates Minitab result
    k1 = kurtosis(l1, fisher=True, bias=False)
    k2 = kurtosis(l2, fisher=True, bias=False)
    res = {
        "u1": u1,
        "u2": u2,
        "s1": s1,
        "s2": s2,
        "n1": n1,
        "n2": n2,
        "k1": k1,
        "k2": k2}
#     print(k1,k2)

    f = var1 / var2
    dfn, dfd = n1 - 1, n2 - 1
    p = (1 - f_dist.cdf(f, dfn, dfd)) * 2
    if p > 1:
        f = var2 / var1
        dfn, dfd = n2 - 1, n1 - 1
        p = (1 - f_dist.cdf(f, dfn, dfd)) * 2
    res["F"] = {"f": f, "p": p, "dfn": dfn, "dfd": dfd}

    #  kp = ((n1 - 1) * k1 + (n2 - 1) * k2) / (n1 + n2 - 2)
    #  SE = (kp / 2 / (n1 - 1) + kp / 2 / (n2 - 1))**.5
    z = (ln(var1) - ln(var2)) / (2 / n1 + 2 / n2)**.5
    p2 = 2 * (1 - norm.cdf(abs(z)))
    df = n1 - 1
    res["Bonett"] = {"z": z, "p": p2, "df": df}

    if print_out:
        print("u1 = %.2f\ts1 = %.2f\tn1 = %d" % (u1, s1, n1))
        print("u2 = %.2f\ts2 = %.2f\tn2 = %d" % (u2, s2, n2))
        print("\nTwo-sided F test: (Matches both, but senstive to normality.)")
        print("f ratio = %.2f\tdfn = %d\tdfd = %d" % (f, dfn, dfd))
        print("Two-sided test p=%.2f" % res["F"]["p"])
        print("\nBonett's test (doesn't match Minitab)")
        print("z = %.2f\tp=%.2f" % (z, res["Bonett"]["p"]))

    return res


#####################
#
single_pop_var_test = chi2_test_stdev

# 从一个population取样，测试这个population
# 的波动等于某一波动的可能性
###########################
#
#

# Pearson Chi square
# Expected frequency = (Row total * Column total) / Grand total
# Calculate the chi-square statistic using the formula:
# χ² = Σ [(O - E)² / E]
# Where O is the observed frequency and E is the expected frequency for each cell.
# Determine the degrees of freedom (df). For a contingency table, df =
# (rows - 1) * (columns - 1).


def chi_square(data, print_out=True):
    a = np.array(data)  # a stores the observed values
    col_sum = np.sum(a, axis=0)
    row_sum = np.sum(a, axis=1)
    ttl_sum = np.sum(col_sum)

    chi_sq = 0
    for y in range(a.shape[0]):
        for x in range(a.shape[1]):
            expected = row_sum[y] * col_sum[x] / ttl_sum
            chi_sq += (a[y][x] - expected)**2 / expected

    df = (a.shape[0] - 1) * (a.shape[1] - 1)

    p = 1 - chi2.cdf(chi_sq, df)

    LR = 0
    for y in range(a.shape[0]):
        for x in range(a.shape[1]):
            expected = row_sum[y] * col_sum[x] / ttl_sum
            LR += 2 * a[y][x] * ln(a[y][x] / expected)

    p_LR = 1 - chi2.cdf(LR, df)

    if print_out:
        print("df = %d" % df)
        t = PT()
        t.field_names = ["Test", "Chi sq", "P >ChiSq"]
        t.add_row(["Likelihood Ratio", "%.3f" % LR, "%.3f" % p_LR])
        t.add_row(["Pearson", "%.3f" % chi_sq, "%.3f" % p])
        print(t)

    return {"p Pearson": p, "chi sq Pearson": chi_sq, "df": df,
            "p LR": p_LR, "chi sq LR": LR}

# Key differences and considerations:
#         Robustness:
#             The Brown-Forsythe and O'Brien tests are generally considered the most robust,
#         followed by Levene's test, with the F-test being the least robust to violations of normality.
#
#         Power:
#             Under normal distributions, the F-test is most powerful, followed by Levene's test,
# then Brown-Forsythe. However, for non-normal distributions, the robust
# tests often outperform the F-test.

#         Underlying distribution:
#             If the data is known to follow a specific distribution, this can guide
#         the choice of test. For example, the Brown-Forsythe test performs well for skewed distributions,
# while Levene's test with squared deviations is better for symmetric,
# moderate-tailed distributions.

#         Sample size:
#             For small samples, the O'Brien and Ramsey conditional tests have shown good Type I
#         error control across different distribution shapes


def multi_pop_var_test(data, print_out=True):
    # data in a list of lists

    def one_way_anova(data):
        ns = [len(l) for l in data]
        k, N = len(data), sum(ns)
        means = [stat.mean(l) for l in data]
        mean = np.concatenate(data).mean()
        SSB = sum([n * (x - mean)**2 for n, x in zip(ns, means)])
        SSW = sum([sum([(v - stat.mean(l))**2 for v in l]) for l in data])
        F = (SSB / (k - 1)) / (SSW / (N - k))
        p = 1 - f_dist.cdf(F, k - 1, N - k)
        return {"F": F, "p": p}

    def OBrien(data):
        #      uij = [nj(nj - 1.5)(xij - Mj)^2 - 0.5SSj] / [(nj - 1)(nj - 2)]
        #         Where:
        #         uij is the transformed score
        #         nj is the number of observations in group j
        #         xij is the original score
        #         Mj is the mean of group j
        #         SSj is the sum of squared deviations from the mean for group j
        #     Do one way ANOVA to uij
        Zij = [[((len(l) - 1.5) * len(l) * (v - stat.mean(l))**2 -
                 stat.variance(l) * (len(l) - 1) / 2) / (len(l) - 1) / (len(l) - 2)
                for v in l] for l in data]
        return one_way_anova(Zij)

    def Levene(data):
        #    Calculate the absolute deviation from the group mean for each data point:
        #   Zij=|X_ij - X̄_i|, where X_ij is the jth observation in the ith group,
        # and X̄_i is the mean of the ith group.
        Zij = [[abs(v - stat.mean(l)) for v in l] for l in data]
        return one_way_anova(Zij)

    def Brown_Forsythe(data):
        #   Zij=|X_ij - median of the group |
        Zij = [[abs(v - stat.median(l)) for v in l] for l in data]
        return one_way_anova(Zij)

    res = {"OBrien": OBrien(data)}
    res["Levene"] = Levene(data)
    res["Brown_Forsythe"] = Brown_Forsythe(data)

    if print_out:
        print("O'Brien[.5]       p = %.3f" % res["OBrien"]["p"])
        print("Levene            p = %.3f" % res["Levene"]["p"])
        print("Brown-Forsythe    p = %.3f" % res["Brown_Forsythe"]["p"])

    return res

##############
# 从两个population取样，测试这两个population的
# 波动一致的可能性
#######################


def two_pop_var_test(l1, l2, print_out=True):
    res = multi_pop_var_test([l1, l2], print_out=print_out)
    res2 = several_tests_stdev_2sided(l1, l2, print_out=False)
    if print_out:
        print("2 Sided F test    p = %.3f" % res2["F"]["p"])
    res["F"] = res2["F"]

    return res


if __name__ == "__main__":
    print(chi_square([[30, 76, 49], [1, 37, 62], [11, 11, 26]]))
    chi_square([[95, 43], [101, 64]])
