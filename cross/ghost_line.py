from PIL import Image
import numpy as np
from statistics import mean, stdev, mode
from statsmodels.stats.diagnostic import normal_ad
############# Own modules ############
from locate_cross import locate_cross

D1D2_THRESHOLD_RATIO = 0.5

#  D1D2_LVLS = [1, .7, .2]
#
#  OC_LVLS = [2.5, 1.75, 1]
#
#  AD_VALUE_TRIGGER = 9
#  SKEW_TRIGGER = .4


def skew(data):
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
    d2 = derivative_forward(derivative_forward(
        [float(i) for i in d]))
    return two_maxima(d2, positive=False)
    #  thd = min(d2) * D1D2_THRESHOLD_RATIO
    #  l = [0 if i >= thd else 1 for i in d2
    #       if i > 0 or i < thd]
    #  return len(compress_list(l)) > 3


def check_1d2p(d):
    d1 = derivative_forward([float(i) for i in d])
    if two_maxima(d1, positive=True):
        return True
    return two_maxima(d1, positive=False)
    #  thd = max(d1) * D1D2_THRESHOLD_RATIO
    #  peak = d1.index(max(d1))
    #  if peak2(d1[peak:], thd):
    #      return True
    #  if peak2(d1[:peak][::-1], thd):
    #      return True
    #  return False


def norm_test(data):
    s2, _ = normal_ad(np.array(data))
    return s2


def off_center(ll):
    return abs(mean(ll) - mode(ll))


def score(data):

    [mad, msk, md1, md2, moc] = data

    #  def levels(value, lvls):
    #      for i, lvl in enumerate(lvls):
    #          if value > lvl:
    #              return 3 - i
    #      return 0
    #
    #  d1d2 = levels(md1 + md2 / 2, D1D2_LVLS)
    #  mad_msk = mad < AD_VALUE_TRIGGER or msk > SKEW_TRIGGER
    #  oc = levels(moc, OC_LVLS)

    #  print(d1d2, oc, mad_msk)
    #  return 1
    #  res=1
    #  if (d1d1|oc)==1:
    #      res=2
    #  elif
    intercept = 2.14
    res = intercept
    res += mad * (-0.0986)
    res += (mad - 9.83) * (md1 - 0.164) * (-0.169)
    res += (mad - 9.83) * (md2 - 0.372) * (-0.183)
    res += moc * 0.419
    res += (md1 - 0.164) * (md2 - 0.372) * (moc - 1.08) * 2.44
    res += (mad - 9.83) * (md1 - 0.164) * (md2 - 0.372) * (moc - 1.08) * 0.519
    return res


def to_lvl(s):
    if s < 1.5:
        return 1
    if s >= 3.5:
        return 4
    return int(s + .5)


def double_line(filename):
    image = Image.open(filename)

    # Convert the image to grayscale
    grayscale_image = image.convert('L')

    # Convert the grayscale image to a 2D NumPy array
    a = np.array(grayscale_image)

    x1, x2, x3, x4, x5, x6 = 1050, 1263, 1319, 1530, 1584, 1794
    y1, y2, y3, y4, y5, y6 = 173, 384, 501, 714, 824, 1038
    subs = [(x1, y1, x2, y2), (x3, y1, x4, y2), (x5, y1, x6, y2),
            (x1, y3, x2, y4), (x3, y3, x4, y4), (x5, y3, x6, y4),
            (x1, y5, x2, y6), (x3, y5, x4, y6), (x5, y5, x6, y6)]

    #  lvls, mads, msks, md2s, md1s = [], [], [], [], []
    #  mocs = []
    res_list = [[] for i in range(7)]
    cross_sections = []
    for x1, y1, x2, y2 in subs:
        sub = a[y1:y2, x1:x2]
        try:
            r = locate_cross(sub, cross_cnt=1)
        except BaseException:
            for lst in res_list:
                lst.append(-1)
            continue
        x, y = r[0]
        oc, ad, sk, d2, d1 = [], [], [], [], []
        for dy in [-40, -20, 20, 40]:
            try:
                l = [sub[y + dy][_] for _ in range(x - 20, x + 21)]
                x0 = x - 20 + l.index(max(l))
                l = [sub[y + dy][_] for _ in range(x0 - 20, x0 + 20)]
                cross_sections.append(l)
                ll = make_list(l)
                ad.append(norm_test(ll))
                sk.append(abs(skew(ll)))
                d2.append(check_2d2p(l))
                d1.append(check_1d2p(l))
                oc.append(off_center(ll))
            except BaseException:
                pass
        #  lvl = 1
        try:
            #  mad, msk, md2, md1
            res = [mean(ad), mean(sk), mean(d1), mean(d2), mean(oc)]
            #  moc = mean(oc)
            fitted_score = score(res)
            for lst, i in zip(res_list,
                              [to_lvl(fitted_score), fitted_score] + res):
                lst.append(i)
        except BaseException:
            for lst in res_list:
                lst.append(-2)

    return {"lvl": res_list[0], "data": res_list[1:],
            "cross sections": cross_sections}
    #  [mads, msks, md1s, md2s, mocs]}


if __name__ == "__main__":
    fn = input("")
    r = double_line(fn)
    print(fn, ",", str(r['lvl']), str(r['data']))
