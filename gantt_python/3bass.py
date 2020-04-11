from scipy.optimize import leastsq
import numpy as np
import matplotlib.pyplot as plt
from math import log
from pandas import read_excel


def Nt_dynamic_model(m, p, q, g, t, N0):
    p2 = g + p - q
    p1 = (p2**2 + 4 * p * q)**0.5
    p3 = ((p1 - p2) / 2 - q * N0 / m) / ((p1 + p2) / 2 + q * N0 / m)
    a = (p1 - p2) / 2 - p3 * (p1 + p2) / 2 * np.exp(-p1 * t)
    b = q + q * p3 * np.exp(-p1 * t)
    Nt = m * np.exp(g * t) * a / b
    return Nt


def Nt_bass_model(m, p, q, t, N0):
    c = np.exp(-(p + q) * t)
    a = m - p * (m - N0) / (p + q / m * N0) * c
    b = 1 + q / m * (m - N0) / (p + q / m * N0) * c
    Nt = a / b
    return Nt


class bass_diffusion:
    def __init__(self, time, total_sales, dynamic_model=False):
        self.x = time
        self.y = total_sales
        self.dynamic_model = dynamic_model
        if dynamic_model:
            vars = [10000, 0.01, 0.3, -1]
            varfinal, cov, infodict, mesg, ier = leastsq(
                self.residual_dynamic, vars, args=(
                    self.x, self.y), full_output=True)
            self.g = varfinal[3]
        else:
            vars = [10000, 0.03, 0.3]
            varfinal, cov, infodict, mesg, ier = leastsq(
                self.residual, vars, args=(
                    self.x, self.y), full_output=True)
            self.g = 0

            # residual (error) function
        ssErr = (infodict["fvec"]**2).sum()
        ssTot = ((self.y - self.y.mean())**2).sum()
        self.rsquared = 1 - (ssErr / ssTot)
        # estimated coefficien
        self.m0 = varfinal[0]
        self.p = varfinal[1]
        self.q = varfinal[2]
        self.t_star = -log(self.p / self.q) / (self.p + self.q)

    def residual(self, vars, t, total_sales):
        m = vars[0]
        p = vars[1]
        q = vars[2]
        N0 = total_sales[0]
        Nt = Nt_bass_model(m, p, q, t, N0)
        if p > 0 and q > 0 and m > 0:  # boundary
            return (np.diff(Nt) - np.diff(total_sales))
        else:
            return [1e10] * (len(Nt) - 1)

    def residual_dynamic(self, vars, t, total_sales):
        m = vars[0]
        p = vars[1]
        q = vars[2]
        g = vars[3]
        N0 = total_sales[0]
        Nt = Nt_dynamic_model(m, p, q, g, t, N0)
        if p > 0 and q > 0 and m > 0 and g <= 0:  # boundary
            return (np.diff(Nt) - np.diff(total_sales))
        else:
            return [1e10] * (len(Nt) - 1)


def main():
    df = read_excel("input.xlsx")  # , sheet_name="Data")
    y = df["Total"]
    x = df["time"]

    bass = bass_diffusion(x, y, dynamic_model=False)
    t = np.linspace(0, bass.t_star * 2, num=1000)
    Nt = Nt_bass_model(bass.m0, bass.p, bass.q, t, bass.y[0])
    # Nt = Nt_dynamic_model(bass.m0, bass.p, bass. q, bass.
    # g, t, bass.y[0])

    dNt = np.diff(Nt) / np.diff(t)
    dy = np.diff(y) / np.diff(x)
    t_star = (t[np.argmax(dNt)] + t[np.argmax(dNt) - 1]) / 2
    t0 = bass.t_star - t_star
    dt = t[:-1] + np.diff(t) / 2
    dx = x[:-1] + np.diff(x) / 2

    chart_title = "m0=%.2f p=%.2e %.2e Rsq=%.4f \nT*=%.1f g=%.4f t0=%.2f" % (
        bass.m0, bass.p, bass.q, bass.rsquared, bass.t_star, bass.g, t0)
    print(chart_title)

    fig, ax1 = plt.subplots()
    color = 'tab:red'
    ax1.set_xlabel('time')
    ax1.set_ylabel('PDF', color=color)
    ax1.plot(dt, dNt, color=color, linestyle="--")
    ax1.plot(dx, dy, color='black')
    #  print(dy)
    #  print(dNt)
    ax1.tick_params(axis='y', labelcolor=color)
    ax1.axvline(t_star, linestyle=":")
    #  plt.yscale('log')
    _, ymax = plt.ylim()
    plt.ylim([ymax / 1e5, ymax])
    ax2 = ax1.twinx()
    # instantiate a second axes that shares the same x-axis
    color = 'tab:blue'
    ax2.set_ylabel('CDF', color=color)
    # already handled the x - label with ax1
    ax2.plot(t, Nt, color=color, linestyle="--")
    ax2.plot(x, y, color='black')
    #  print(y)
    #  print(Nt)
    ax2.tick_params(axis='y', labelcolor=color)
    # add a vertical line at t star
    #  plt.axvline(t_star + (t[1] - t[0]) / 2, linestyle=":")
    plt.title(chart_title)
    plt.xlim([0, bass.t_star * 2 - t0])
    fig.tight_layout()
    # otherwise the right y-label is slightly clipped
    plt.savefig('pdf_cdf.svg')


if __name__ == "__main__":
    main()

# from bass. = MO * np.exp(G * (t + tO))# Bass = m
# * (((P + (2)**2 / P) * np.exp(-(P + Q) * (t +
# tO))) / \# (1 + (Q / P) * np.exp(-(P + Q) * (t +
# tO)))**24 cofactor = np.exp(-(P + Q) * t0)#
# salei_cdf_at_t0 = m[0] * (1 - cofactor) / (1 +
# (Q / P) * cofactor)* it Bass.insert(0,
# sales_cdf_at_t0)# Acc_Bass =
# np.cumsum(np.insert(Bass, 0, sales_cdf_at_t0))*
# sales.insert(0, init_c_sales)# # time
# interpolation# t = xi sales = yi tp =
# np.linspace(0.0, t_star * 2, num=100)# cofactor
# = np.exp(-(p + q) * tp)* sales_pdf = m * (((p +
# q)**2 / p) * cofactor) / (1 / p) * cofactor)**2#
# # plt.plot(tp, sales_pdf, t, sales)* I
# Cumulative sales (cdf)# c_sales =
# np.cumsum(sales)# sales_cdf = m * (1 - cofactor)
# / (1 + (q / p) * cofactor)# # plt.plot(t
# sales_cdf, t, c_sales)
#  df 0 N0 / c = self, 00,
#  is dual
#  t) - .m0, ass.q, q=-1] +
#  we PO m + (q P,
