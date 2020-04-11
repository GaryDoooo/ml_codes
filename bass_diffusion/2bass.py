from scipy.optimize import leastsq
import numpy as np
import matplotlib.pyplot as plt
from math import log
#
# data source: https://www.worldometers.info/coronavirus/
# daily total cases from Jan 21 2020y = rray([    446, 579, 844, 1312, 2015, 2801, 45    6061,  7816,  9821,  11948,    14551])
x = np.linspace(1.0, len(y), num=len(y))
vars = [660630, 0.3, 0.1]

# residual (error) function


def residual(vars, t, sales):
    M = vars[0]
    P = vars[1]
    Q = vars[2]
    Bass = M * (((P+Q)**2/P)*np.exp(-(P+Q)*t))/(1+(Q/P)*np.exp(-(P+Q)*t))**2
    return (Bass - (sales))


# non linear least square fitting
varfinal, cov, infodict, mesg, ier = leastsq(
    residual, vars, args=(x, y), full_output=True)

ssErr = (infodict['fvec']**2).sum()
ssTot = ((y-y.mean())**2).sum()
rsquared = 1-(ssErr/ssTot)

# estimated coefficients
m = varfinal[0]
p = varfinal[1]
q = varfinal[2]
t_star = -log(p/q)/(p+q)

# print(varfinal)
# print(cov, infodict, mesg, ier)
print("m = %04f   p = %04f   q = %04f" % (m, p, q))
print("R sq =", rsquared)
print("T star =", t_star)

chart_title = "m=%.2f p=%.4f q=%.4f Rsq=%.4f T*=%.2f" % (
    m, p, q, rsquared, t_star)
print(chart_title)


# time interpolation
t = x
sales = y
tp = np.linspace(0.0, t_star*2, num=100)
cofactor = np.exp(-(p+q) * tp)
sales_pdf = m * (((p+q)**2/p)*cofactor)/(1+(q/p)*cofactor)**2
# plt.plot(tp, sales_pdf, t, sales)

# Cumulative sales (cdf)
c_sales = np.cumsum(sales)
sales_cdf = m*(1-cofactor)/(1+(q/p)*cofactor)
# plt.plot(tp, sales_cdf, t, c_sales)

fig, ax1 = plt.subplots()

color = 'tab:red'
ax1.set_xlabel('time')
ax1.set_ylabel('PDF', color=color)
ax1.plot(tp, sales_pdf, t, sales)
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

color = 'tab:blue'
ax2.set_ylabel('CDF', color=color)  # we already handled the x-label with ax1
ax2.plot(tp, sales_cdf, t, c_sales)
ax2.tick_params(axis='y', labelcolor=color)

# add a vertical line at t star
plt.axvline(t_star, linestyle=":")
plt.title(chart_title)

fig.tight_layout()  # otherwise the right y-label is slightly clipped
plt.savefig('pdf_cdf.png')
