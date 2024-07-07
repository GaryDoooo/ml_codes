from scipy.stats import norm, binom
from scipy.stats import f as f_dist
#  from functools import lru_cache
from prettytable import PrettyTable as PT
#  import numpy as np
####### Own Modules ########
from binomial import binomial


def p_blaker(n, p, k):
    rv = binom(n, p)
    psl = []
    s = 0
    for i in range(n + 1):
        s += rv.pmf(i)
        psl.append(s)

    def pt_le_k(n, p, k):
        return psl[k] if k >= 0 else 0

    def pt_ge_k(n, p, k):
        return 1 - pt_le_k(n, p, k - 1)

    if pt_ge_k(n, p, k) < pt_le_k(n, p, k):
        k_modified = max([i for i in range(n + 1)
                          if pt_le_k(n, p, i) <= pt_ge_k(n, p, k)])
        return pt_ge_k(n, p, k) + pt_le_k(n, p, k_modified)
    elif pt_ge_k(n, p, k) == pt_le_k(n, p, k):
        return 1
    else:
        k_modified = min([i for i in range(n + 1)
                          if pt_ge_k(n, p, i) <= pt_le_k(n, p, k)])
        return pt_le_k(n, p, k) + pt_ge_k(n, p, k_modified)


def p_sterne(n, p, k):
    rv = binom(n, p)
    PTK = rv.pmf(k)
    return sum([rv.pmf(i) for i in range(n + 1) if rv.pmf(i) <= PTK])


def p_likelihood_ratio(n, p0, x):
    p = x / n
    rv = binom(n, p0)

    def LR(i):
        ii = min(i, n - i)
        return (p / p0)**ii * ((1 - p) / (1 - p0))**(n - ii)

    return sum(rv.pmf(y) for y in range(n + 1)
               if LR(y) >= LR(x))


def prop_test_1sample(events=1, N=1, p0=1,
                      print_out=False, alpha=.05):
    p = events / N
    Z = (p - p0) / (p0 * (1 - p0) / N)**.5
    p_norm = (1 - norm.cdf(abs(Z))) * 2
    p_norm_less = norm.cdf(Z)
    b_res = binomial(N, p0, x=events, print_out=False)
    #  print(b_res)
    p_bi = b_res["left_acc_p"]

    std = (p * (1 - p) / N)**.5
    CI_l, CI_u = (p + norm.ppf(alpha / 2) * std,
                  p + norm.ppf(1 - alpha / 2) * std)
    CI_high = p + norm.ppf(1 - alpha) * std
    CI_low = p + norm.ppf(alpha) * std

# https://support.minitab.com/en-us/minitab/help-and-how-to/statistics/basic-statistics/how-to/1-proportion/methods-and-formulas/methods-and-formulas/
# Clopper-Pearson exact confidence interval method
    dfn = 2 * events
    dfd = 2 * (N - events + 1)
    F = f_dist.ppf(alpha / 2, dfn, dfd)
    p_exct_l = dfn * F / (dfd + dfn * F)
    F = f_dist.ppf(alpha, dfn, dfd)
    p_exct_low = dfn * F / (dfd + dfn * F)

    dfn = 2 * (events + 1)
    dfd = 2 * (N - events)
    F = f_dist.ppf(1 - alpha / 2, dfn, dfd)
    p_exct_u = dfn * F / (dfd + dfn * F)
    F = f_dist.ppf(1 - alpha, dfn, dfd)
    p_exct_high = dfn * F / (dfd + dfn * F)

    p_s = p_sterne(N, p0, events)
    p_b = p_blaker(N, p0, events)

    if print_out:
        print("One sample propotion test alpha = %.3f" % alpha)
        #  print("Z porportion test")
        print("\np-value for H0: p==p0, Ha: p!=p0")
        print("Normal Approx.   %.3f" % p_norm)
        print("Strerne's Method %.3f" % p_s)
        print("Blaker's Method  %.3f" % p_b)
        print("\nH0: p==p0, Ha: p<p0.")
        print("Normal App. p-value = %.3f\nBinomial Exact p-value = %.3f" %
              (p_norm_less, p_bi))
        #  print("p-value %.3f" % p_norm_less,
        #        "for H0 p==p0, Ha p<p0.")
        pct = "%%%.1f" % (100 - alpha * 100)
        #  "CI (%.3f, %.3f), (0, %.3f), (%.3f, 1)" % (
        #      CI_l, CI_u, CI_high, CI_low))
        #  print("\nBinomial test p-value %.3f" %
        #        p_bi, "for gettig less or equal events if real p equals p0.")
        t = PT()
        t.field_names = ["N", "Event", "Sample P"]
        t.add_row([str(N), str(events), "%.3f" % (events / N)])
        print("")
        print(t)
        t = PT()
        print("p-value CI", pct)
        t.field_names = ["Algo", " CI", "Upper Bound",
                         "Lower Bound"]
        t.add_row(["Normal App.", "(%.3f, %.3f)" % (CI_l, CI_u),
                   "%.3f" % CI_high, "%.3f" % CI_low])
        t.add_row(["Clopper-Pearson\nexact", "(%.3f, %.3f)" %
                   (p_exct_l, p_exct_u), "%.3f" %
                   p_exct_high, "%.3f" %
                   p_exct_low])
        print(t)
        print("")

    return {"p norm": p_norm, "p Binomial": p_bi,
            "Z p less": p_norm_less,
            "CI norm": {"CI l": CI_l, "CI u": CI_u,
                        "CI high": CI_high, "CI low": CI_low},
            "p Sterne": p_s, "p Blaker": p_b,
            "CI exact": {"CI l": p_exct_l, "CI u": p_exct_u,
                         "CI high": p_exct_high, "CI low": p_exct_low}
            }


if __name__ == "__main__":
    print(prop_test_1sample(9, 250, .073, print_out=True))
    print(p_blaker(250, .073, 9), p_sterne(250, .073, 9))
    print(p_likelihood_ratio(250, .073, 9))
    print(p_likelihood_ratio(50, .35, 10))
    print(p_sterne(50, .35, 10))
