
import numpy as np
from statistics import mean, stdev, mode
from statsmodels.stats.diagnostic import normal_ad
############## Own Modules #################
from fitted_model import calculate_model

# The height ratio of second peak to the max(or min) of the derivative, the 
# threshold to filter background, the setting will impact some marginal cases
D1D2_THRESHOLD_RATIO = 0.5

def skew(data):
    """
    skewness of the given list of data. The scipy.stats.skew doesn't return same results to Minitab and JMP.
    This calculation does. 
    """
    u = mean(data)
    N = len(data)
    if N < 2:
        return
    std = stdev(data)
    try:
        skew = N / (N - 1) / (N - 2) * sum(((i - u) / std)**3
                                           for i in data)
    except BaseException:
        skew = np.nan
    return skew


def make_list(data, u=0):
    """
    Repeat expand the brightness level cross section into sample list, while
    treating the brightness as counts at each position.
    """
    return np.repeat(
        [float(i) - u for i in range(len(data))],
        data)


def derivative_forward(data):
    return [data[i + 1] - data[i] for i in range(len(data) - 1)]

def peak2(l, thd):
    """
    starting from a max point to find if a point over the threshold after negative value appeared
    or from a min poin to find if a point over the thd after positive value appeared.
    """
    starting_sign = np.sign(l[0])
    has_opposite = False
    for i in l:
        if starting_sign * np.sign(i) < 0:
            has_opposite = True
        if i > thd and has_opposite and l[0] > 0:
            return True
        if i < thd and has_opposite and l[0] < 0:
            return True
    return False


def two_maxima(data, positive=True):
    """
    To test if two maxima or minima in the 1D data list input
    """
    if positive:
        m = max(data)
    else:
        m = min(data)
    thd = m * D1D2_THRESHOLD_RATIO
    peak_idx = data.index(m)
    if peak2(data[peak_idx:], thd):
        return True
    if peak2(data[:peak_idx][::-1], thd):
        return True
    return False


def check_2d2p(d):
    """
    Detect if there are two minimum below the threshold, while between the two minimum 
    there is at least one point positive in the second derivative.
    """
    d2 = derivative_forward(derivative_forward(
        [float(i) for i in d]))
    return two_maxima(d2, positive=False)

def check_1d2p(d):
    """
    Detect if there is any point over the trigger threshold beside (either left or right) the max of the first derivative
    after a negative value appeared.
    """
    d1 = derivative_forward([float(i) for i in d])
    if two_maxima(d1, positive=True):
        return True
    return two_maxima(d1, positive=False)


def off_center(ll):
    """
    Measure the mean and maximum position distance
    input is repeat expanded data
    """
    return abs(mean(ll) - mode(ll))


def norm_test(data):
    """
    Anderson Darling normality test, the second return is p value, ignored 
    """
    s2, _ = normal_ad(np.array(data))
    return s2
    

def fit_score_and_lvl(data):
    """
    Use a fitted model to calculate a score, then round it to the nearest integer, and supplement it with some corner
    cases to obtain the final ghost line severity level classification.
    """
    [mad, msk, md1, md2, moc] = data
    s = calculate_model(mad, md1, md2, moc, msk)
    if s < 1.5:
        lvl = 1
    elif s >= 3.5:
        lvl = 4
    else:
        lvl = int(s + .5)
    if lvl == 1:
        if mad < 9 and md1 + md2 > 0.45:
            lvl = 2
        elif mad < 6.1 and md1 + md2 > .2:
            lvl = 2
    if lvl == 3 and md1 + md2 > 1.9:
        lvl = 4
    return s, lvl
