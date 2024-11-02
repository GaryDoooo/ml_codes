
import numpy as np
from statistics import mean
from PIL import Image
############# Own modules ############
from locate_cross import locate_cross
from double_line_subs import skew, make_list, fit_score_and_lvl, off_center, norm_test, check_2d2p, check_1d2p


def double_line(filename):
    """
    This code evaluates image ghosting severity levels.

    Ghost line levels are determined using four evaluations: Anderson-Darling test, skewness, and double extrema tests in first and second derivatives. The level settings are empirical, manually verified with a limited number of images.

    Args:
        filename (str): This code specifically processes 3x3 plus-shaped cross images, comprising a low-resolution full image and high-resolution zoomed-in crops of each cross. 

    Returns:
        a dict including 
        lvl: 
            a list of 9 zones' ghost line level results
        data: 
            a list of 6 lists of the 9 zones' fitted_score, mean AD-value, mean skewness, mean first and second derivative detection results, and mean center offsets.
        cross sections: 
            a list of 9x4=36 cross sections 

    """
    
    image = Image.open(filename)
    # Convert the image to grayscale
    grayscale_image = image.convert('L')
    # Convert the grayscale image to a 2D NumPy array
    a = np.array(grayscale_image)
    
    # hard-coded positions of the 9 zoomed in images. The position follows
    # 0 1 2
    # 3 4 5
    # 6 7 8
    x1, x2, x3, x4, x5, x6 = 1050, 1263, 1319, 1530, 1584, 1794
    y1, y2, y3, y4, y5, y6 = 173, 384, 501, 714, 824, 1038
    subs = [(x1, y1, x2, y2), (x3, y1, x4, y2), (x5, y1, x6, y2),
            (x1, y3, x2, y4), (x3, y3, x4, y4), (x5, y3, x6, y4),
            (x1, y5, x2, y6), (x3, y5, x4, y6), (x5, y5, x6, y6)]

    # Result list of the 9 zones
    res_list = [[] for i in range(7)]
    cross_sections = []
    for x1, y1, x2, y2 in subs:
        sub = a[y1:y2, x1:x2]
        try:
        # Find the cross center inside the cropped image
            r = locate_cross(sub, cross_cnt=1)
        except BaseException:
            for lst in res_list:
                lst.append(-1)
            continue
        x, y = r[0]
        # Result list of the 4 cross-sections 
        oc, ad, sk, d2, d1 = [], [], [], [], []
        # Hard-coded cross section Y offsets from the cross center
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
            for lst, i in zip(res_list,
                              [lvl, fitted_score] + res):
                lst.append(i)
        except BaseException:
            for lst in res_list:
                lst.append(-2)

    return {"lvl": res_list[0], "data": res_list[1:],
            "cross sections": cross_sections}


if __name__ == "__main__":
    fn = input("")
    r = double_line(fn)
    print(fn, ",", str(r['lvl']), str(r['data']))
    

