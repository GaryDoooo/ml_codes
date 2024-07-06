from scipy.stats import norm
####### Own Modules ########
from binomial import binomial


def prop_test_1sample(events=1, N=1, p0=1,
                      print_out=False, alpha=.05):
    p = events / N
    Z = (p - p0) / (p0 * (1 - p0) / N)**.5
    p_norm = (1 - norm.cdf(abs(Z))) * 2
    p_norm_less = norm.cdf(Z)
    b_res = binomial(N, p0, x=events, print_out=False)
    p_bi = b_res["left_acc_p"]

    std = (p * (1 - p) / N)**.5
    CI_l, CI_u = (p + norm.ppf(alpha / 2) * std,
                  p + norm.ppf(1 - alpha / 2) * std)
    CI_high = p + norm.ppf(1 - alpha) * std
    CI_low = p + norm.ppf(alpha) * std

    if print_out:
        print("One sample propotion test alpha = %.3f" % alpha)
        print("Z porportion test")
        print("p-value %.3f for real p equals p0." % p_norm)
        print("p-value %.3f" % p_norm_less,
              "for H0 p==p0, Ha p<p0.")
        print("%%%.1f" % (100 - alpha * 100),
              "CI (%.3f, %.3f), (0, %.3f), (%.3f, 1)" % (
                  CI_l, CI_u, CI_high, CI_low))
        print("\nBinomial test p-value %.3f" %
              p_bi, "for gettig less or equal events if real p equals p0.")
    return {"Z p": p_norm, "Binomial p": p_bi,
            "Z p less": p_norm_less, "CI l": CI_l, "CI u": CI_u,
            "CI high": CI_high, "CI low": CI_low}


if __name__ == "__main__":
    print(prop_test_1sample(9, 250, .073, print_out=True))
