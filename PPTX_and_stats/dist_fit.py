from scipy.stats import norm
from scipy.stats import t as t_dist
from math import log as ln
from numpy import nan
import statistics as stat


def ABL(rv, data, k):
    """
    calculate -2*log-likelihood, AICc and BIC
    rv is the frozen dist function
    k is the number of parameters of the dist funciton.
    """
    log_likelihood = sum(
        ln(rv.pdf(i)) for i in data)
    n = len(data)
    if n - k > 1:
        AICc = -2 * log_likelihood + 2 * k * n / (n - k - 1)
    else:
        AICc = nan
    if n > 0:
        BIC = -2 * log_likelihood + ln(n) * k
    else:
        BIC = nan
    return -2 * log_likelihood, AICc, BIC


def fit_norm(data):
    u, s = stat.mean(data), stat.stdev(data)
    #  u, s = norm.fit(data)
    print(u, s)
    rv = norm(u, s)
    n = len(data)
    ll, aicc, bic = ABL(rv, data, 2)
    sem = s / n**.5
    ses = s / (2 * (n - 1))**.5
    print(sem, ses)
    print(ll, aicc, bic)
    u4 = sum((i - u)**4 for i in data) / n
    sess = (1 / n * (u4 - (n - 3) / (n - 1) * s**4))**.5
    print(sess / 2 / s)
    #  print(stat.stdev(data))


def fit_t(data):
    
    print(t_dist.fit(data))


if __name__ == "__main__":
    data = [
        59,
        61,
        55,
        66,
        52,
        60,
        61,
        51,
        60,
        61,
        56,
        65,
        63,
        58,
        59,
        61,
        62,
        65,
        63,
        62,
        63,
        64,
        65,
        64,
        68,
        64,
        69,
        62,
        64,
        67,
        65,
        66,
        62,
        66,
        65,
        60,
        68,
        62,
        68,
        70]
    fit_norm(data)
