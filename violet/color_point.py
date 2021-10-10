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
        res[x] = sp1[int(x / ratio)]
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


def main():
    spLED, vLED, gLED, rLED = read_RGB_LED()
    spLCD, bCF, gCF, rCF = read_CF()
    sp_after_LCD = sp_product(spLED, spLCD)
    print(sp2xy(sp_after_LCD))
    # boost V power to white
    for powerX in range(2, 10):
        print(
            "V power X%d" % powerX,
            sp2xy(sp_product(spLCD,
                             sp_add(sp_add(gLED, rLED), sp_Y_magnify(
                                 vLED, powerX)))))
    bhaz = read_400_700_sp('b_hazard.csv')
    print("V after LCD B haz",
          integration(
              sp_product(bhaz,
                         sp_product(spLCD,
                                    sp_add(sp_add(gLED, rLED), sp_Y_magnify(
                                        vLED, 2))))))
    bLED = sp_X_magnify(read_400_700_sp('v_LED_full.csv'), 1.117)
    for powerX in range(1, 10):
        print(
            "V power X%.1f" % (powerX / 10),
            sp2xy(sp_product(spLCD,
                             sp_add(sp_add(gLED, rLED), sp_Y_magnify(
                                 bLED, powerX / 10)))))
    print("B after LCD B haz",
          integration(
              sp_product(bhaz,
                         sp_product(spLCD,
                                    sp_add(sp_add(gLED, rLED), sp_Y_magnify(
                                        bLED, 0.1))))))
    print("try other specturm")
    fvLED = read_400_700_sp('v_LED_full.csv')
    for r in range(1, 117):
        ratio = 1 + r / 100
        bLED = sp_X_magnify(fvLED, ratio)
        res = []
        for powerX in range(1, 100):
            res.append(
                (powerX / 100,
                 sp2xy(
                     sp_product(
                         spLCD,
                         sp_add(
                             sp_add(
                                 gLED,
                                 rLED),
                             sp_Y_magnify(
                                 bLED,
                                 powerX / 100))))))
        pick_ratio = min(res, key=lambda x: (
            (x[1][0] - .3)**2 + (x[1][1] - .33)**2))[0]
        print(
            "Lambda",
            403 * ratio,
            "power X",
            pick_ratio,
            "B haz",
            integration(
                sp_product(
                    bhaz,
                    sp_product(
                        spLCD,
                        sp_add(
                            sp_add(
                                gLED,
                                rLED),
                            sp_Y_magnify(
                                bLED,
                                pick_ratio))))))


if __name__ == "__main__":
    main()
