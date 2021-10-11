import csv
import colour


def sp2xy(sp):
    spd = colour.SpectralDistribution(sp, name='Sample')
    cmfs = colour.colorimetry.MSDS_CMFS_STANDARD_OBSERVER['CIE 1931 2 Degree Standard Observer']
    illuminant = colour.SDS_ILLUMINANTS['D65']
    XYZ = colour.sd_to_XYZ(spd, cmfs, illuminant)
    return colour.XYZ_to_xy(XYZ)


def read_CF():
    spb = read_400_700_sp('blue_filter.csv')
    spg = read_400_700_sp('green_filter.csv')
    spr = read_400_700_sp('red_filter.csv')
    sp = sp_add(sp_add(spb, spg), spr)
    return sp, spb, spg, spr


def read_RGB_LED():
    spv = read_400_700_sp('v_led.csv')
    spg = read_400_700_sp('green_led.csv')
    spr = read_400_700_sp('red_led.csv')
    sp = sp_add(sp_add(spv, spg), spr)
    return sp, spv, spg, spr


def read_400_700_sp(filename):
    sp = {}
    with open(filename, newline='') as csvfile:
        for r in csv.reader(csvfile, delimiter=',', quotechar='|'):
            sp[int(float(r[0]))] = float(r[1])
    return sp


def sp_Y_magnify(sp1, ratio):
    res = {}
    for key in sp1:
        res[key] = sp1[key] * ratio
    return res


def sp_X_magnify(sp1, ratio):
    res = {}
    for x in range(400, 701):
        try:
            res[x] = sp1[int(x / ratio)]
        except BaseException:
            res[x] = 0
    return res


def sp_product(sp1, sp2):
    res = {}
    for key in sp1:
        res[key] = sp1[key] * sp2[key]
    return res


def sp_add(sp1, sp2):
    res = {}
    for key in sp1:
        res[key] = sp1[key] + sp2[key]
    return res


def integration(sp):
    res = 0
    for key in sp:
        res += sp[key]
    return res


def get_xy(paras, vLED):
    (_, spLCD, gLED, rLED, _) = paras
    return sp2xy(sp_product(spLCD,
                            sp_add(sp_add(gLED, rLED), vLED)))
    #  sp_Y_magnify(
    #  vLED, powerX))))


def get_bhaz(paras, vLED):
    (bhaz, spLCD, gLED, rLED, _) = paras
    return integration(
        sp_product(bhaz,
                   sp_product(spLCD,
                              sp_add(sp_add(gLED, rLED), vLED))))
    #  sp_Y_magnify(
    #                 vLED, powerX)))))


def color_match(paras, l1, p1, l2):
    (bhaz, spLCD, gLED, rLED, fvLED) = paras
    sp1 = sp_Y_magnify(sp_X_magnify(fvLED, l1 / 403), p1)
    sp2_0 = sp_X_magnify(fvLED, l2 / 403)
    res = []
    for i in range(1, 100):
        sp2 = sp_Y_magnify(sp2_0, i / 100)
        sp = sp_add(sp2, sp1)
        res.append((i / 100, get_xy(paras, sp), sp))
    return min(res, key=lambda x:
               (x[1][0] - .31)**2 + (x[1][1] - .33)**2)


def main():
    spLED, vLED, gLED, rLED = read_RGB_LED()
    spLCD, bCF, gCF, rCF = read_CF()
    print("try other specturm")
    fvLED = read_400_700_sp('v_LED_full.csv')
    bhaz = read_400_700_sp('b_hazard.csv')
    paras = (bhaz, spLCD, gLED, rLED, fvLED)
    for l1 in range(400, 450, 5):
        for p1 in range(1, 21):
            power1 = p1 / 10
            for l2 in range(450, 500, 5):
                (p2, xy, sp) = color_match(paras, l1, power1, l2)
                print("L1", l1, "L2", l2, "p1 %.2f" % p1, "p2 %.2f" % p2,
                      "xy", xy, "bhaz", get_bhaz(paras, sp))


if __name__ == "__main__":
    main()
