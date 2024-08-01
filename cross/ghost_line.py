from PIL import Image
import numpy as np
from statistics import mean
from statsmodels.stats.diagnostic import normal_ad
from scipy.stats import skew
############# Own modules ############
from locate_cross import locate_cross


def make_list(data, u=0):
    return np.repeat(
        [float(i) - u for i in range(len(data))],
        data)


def derivative_forward(data):
    return [data[i + 1] - data[i] for i in range(len(data) - 1)]


def compress_list(lst):
    return [x for i, x in enumerate(lst) if i == 0 or x != lst[i - 1]]


def check_2d2p(d):
    d2 = derivative_forward(derivative_forward(
        [float(i) for i in d]))
    thd = min(d2) * .5
    l = [0 if i >= thd else 1 for i in d2
         if i > 0 or i < thd]
    return len(compress_list(l)) > 3


def check_1d2p(d):
    def peak2(l, thd):
        has_neg = False
        for i in l:
            if i < 0:
                has_neg = True
            if i > thd and has_neg:
                return True
        return False
    d1 = derivative_forward([float(i) for i in d])
    thd = max(d1) * .5
    peak = d1.index(max(d1))
    if peak2(d1[peak:], thd):
        return True
    if peak2(d1[:peak][::-1], thd):
        return True
    return False


def norm_test(data):
    s2, _ = normal_ad(np.array(data))
    return s2


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

    lvls, mads, msks, md2s, md1s = [], [], [], [], []
    for x1, y1, x2, y2 in subs:
        sub = a[y1:y2, x1:x2]
        try:
            r = locate_cross(sub, cross_cnt=1)
        except BaseException:
            lvls.append(0)
            continue
        x, y = r[0]
        ad, sk, d2, d1 = [], [], [], []
        for dy in [-40, -20, 20, 40]:
            try:
                l = [sub[y + dy][_] for _ in range(x - 20, x + 21)]
                x0 = x - 20 + l.index(max(l))
                l = [sub[y + dy][_] for _ in range(x0 - 20, x0 + 20)]
                ll = make_list(l)
                ad.append(norm_test(ll))
                sk.append(skew(ll))
                d2.append(check_2d2p(l))
                d1.append(check_1d2p(l))
            except BaseException:
                pass
        lvl = 1
        try:
            mad, msk, md2, md1 = mean(ad), mean(sk), mean(d2), mean(d1)
            if md2 + md1 > 1:
                lvl = 4
            else:
                if md2 > .2 or md1 > .2:
                    lvl = 2
                if mad < 9 or msk > .4:
                    lvl += 1
            lvls.append(lvl)
            mads.append(mad)
            msks.append(msk)
            md1s.append(md1)
            md2s.append(md2)
        except BaseException:
            lvls.append(0)

    return {"lvl": lvls, "data": [
        mads, msks, md1s, md2s]}


if __name__ == "__main__":
    fn = input("")
    r = double_line(fn)
    print(r['str'])
