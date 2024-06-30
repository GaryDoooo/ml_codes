from cpk import cpk_calc, cpk
from chi_sq import chi2_test_stdev
from random import random as rand
from numpy.random import normal as norm_rand


def gen_pop(spec, L, U, S):
    std = (spec["USL"] - spec["LSL"]) / (L + rand() * (U - L))
    mean = spec["T"] + std * (rand() - 0.5) * S
    return mean, std


def gen_samples(mean, std, N):
    return list(norm_rand(mean, std, 10))


def test(spec, L, U, S, N):
    mean, std = gen_pop(spec, L, U, S)
    data = gen_samples(mean, std, N)
    r1 = chi2_test_stdev(data, std, print_out=False)
    r3 = cpk_calc(
        mean,
        std,
        spec["T"],
        spec["USL"],
        spec["LSL"], N - 1, N,
        print_out=False)
    r2 = cpk(
        data,
        spec["T"],
        spec["USL"],
        spec["LSL"],
        alpha=0.1,
        print_out=False)
    p_cpk = r3["cpk"]
    #  s_cpk = r2["Overall"]["cpk"]
    s_cpkL = r2["Overall"]["cpk_l"]
    s_std_u = r1["std_from_S_high95"]
    r4 = cpk_calc(
        mean,
        s_std_u,
        spec["T"],
        spec["USL"],
        spec["LSL"], N - 1, N,
        print_out=False)
    ss_cpk = r4["cpk"]
    #  print(p_cpk, s_cpk, ss_cpk, s_cpkL)
    return p_cpk < ss_cpk, p_cpk < s_cpkL


if __name__ == "__main__":
    spec = {"T": 20, "USL": 22, "LSL": 18}
    Total = 10000
    print("test repeats", Total)
    for L in [1, 2, 4]:
        for U in [6, 8, 10]:
            for S in [1, 2, 4]:
                for N in [10, 20, 40]:
                    out2 = out1 = 0
                    for _ in range(Total):
                        r = test(spec, L, U, S, N)
                        out1 += r[0]
                        out2 += r[1]
                    print("L", L, "U", U, "N", N, "S", S, "chi2",
                          out1 / Total, "jmp", out2 / Total)
    # Output of 10K tests, 5.09% and 3.89% L=4, U=8, N=10, S=1
    #  print(mean, std, data)
