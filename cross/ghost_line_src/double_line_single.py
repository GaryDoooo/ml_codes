
import numpy as np
from statistics import mean
############# Own modules ############
from locate_cross import locate_cross
from double_line_subs import skew, make_list, fit_score_and_lvl, off_center, norm_test, check_2d2p, check_1d2p


def enhance(cropped_image):
    min_val = np.min(cropped_image)
    max_val = np.max(cropped_image)

    # Scale to [0, 255]
    enhanced_image = (255 * (cropped_image - min_val) / (max_val - min_val)).astype(np.uint8)
    return enhanced_image


def double_line(image, x=None, y=None):
    """
    image is a 2d numpy array of 0-255
    float32 tiff data can be normalized by the function above (enhance)

    """

    sub = np.array(image, dtype='float32')
    cross_sections = []
    if x is None or y is None:
        try:
            # Find the cross center inside the cropped image
            r = locate_cross(sub, cross_cnt=1)
        except BaseException:
            return None
        x, y = r[0]
    # Result list of the 4 cross-sections
    oc, ad, sk, d2, d1 = [], [], [], [], []
    for dy in [-40, -20, 20, 40]:
        try:
            # Get a 40 pixel wide horizontal cross section at the Y offset
            l = [sub[y + dy][_] for _ in range(x - 20, x + 21)]
            # In some cases the cross tilted, or inaccurate center detection,
            # recenter the window at max
            x0 = x - 20 + l.index(max(l))
            l = [sub[y + dy][_] for _ in range(x0 - 20, x0 + 20)]
            cross_sections.append(l)
            # ll here is the repeat expansion
            ll = make_list(l)

            ad.append(norm_test(ll))
            sk.append(abs(skew(ll)))
            d2.append(check_2d2p(l))
            d1.append(check_1d2p(l))
            oc.append(off_center(ll))
        except BaseException:
            pass

    try:
        res = [mean(ad), mean(sk), mean(d1), mean(d2), mean(oc)]
        fitted_score, lvl = fit_score_and_lvl(res)
    except BaseException:
        return None

    return {"lvl": lvl, "score": fitted_score,
            "AD": res[0], "Skewness": res[1],
            "D1": res[2], "D2": res[3], "offCenter": res[4],
            "cross sections": cross_sections}


if __name__ == "__main__":
    pass
