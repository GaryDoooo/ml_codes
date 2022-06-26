#  import csv
import colour
from color_point import *


def sp2Y(sp):
    spd = colour.SpectralDistribution(sp, name='Sample')
    cmfs = colour.colorimetry.MSDS_CMFS_STANDARD_OBSERVER['CIE 1931 2 Degree Standard Observer']
    illuminant = colour.SDS_ILLUMINANTS['D65']
    XYZ = colour.sd_to_XYZ(spd, cmfs, illuminant)
    #  return colour.XYZ_to_xy(XYZ)
    return XYZ[1]


def max_in_sp(sp):
    res = -1e9
    for key in sp:
        res = max(res, sp[key])
    return res


if __name__ == "__main__":
    sun = read_400_700_sp("solar.csv")
    print("Sun nit", sp2Y(sun))
    spb = read_400_700_sp('blue_filter.csv')
    vled = read_400_700_sp('410led.csv')
    v_after_cf = sp_product(spb, vled)
    #  print(v_after_cf)
    print("max_in_sp", max_in_sp(v_after_cf))
    print("v nit", sp2Y(v_after_cf))
    print("normalized v nit", sp2Y(v_after_cf) / max_in_sp(v_after_cf))
