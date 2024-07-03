from linear_fit import linear_fit
from ortho_fit import orthogonal_fit
import numpy as np
import matplotlib.pyplot as plt
from utilities import pearson_correlation
from matplotlib.patches import Ellipse
import statistics as stat
from scipy.stats import t as t_dist


def fit_plot(x, y, alpha=0.05, print_out=True,
             ellipse=False, linear=False,
             ortho=False, ortho_ratio=1,
             show_CI=False, show_PI=False,
             show_plot=False, filename=None,
             xlabel=None, ylabel=None,
             grid=False, show_legend=False):

    res = dict()
    _, ax = plt.subplots()
    ax.scatter(x, y, color='blue', label='Data points')

    if ellipse:
        correlation = pearson_correlation(x, y, alpha=alpha,
                                          print_out=print_out)
        r = correlation["r"]
        res["Pearson"] = correlation
        major = np.abs(correlation["r_u"] - correlation["r_l"])
        minor = 2 * np.sqrt(1 - r**2)
        angle = np.degrees(np.arctan(r / np.sqrt(1 - r**2)) / 2)

        ax.add_patch(
            Ellipse(
                (stat.mean(x),
                 stat.mean(y)),
                major,
                minor,
                angle=angle,
                alpha=0.2,
                color='b'))

    if ortho:
        ortho_res = orthogonal_fit(x, y, error_ratio=ortho_ratio,
                                   print_out=print_out, alpha=alpha)
        res["Orthogonal Fit"] = ortho_res
        x1, x0 = max(x), min(x)
        x_line = [x0, x1]
        y_line = [ortho_res["intercept"] + x0 * ortho_res["slope"],
                  ortho_res["intercept"] + x1 * ortho_res["slope"]]
        ax.plot(x_line, y_line, color='k', label='Orthogonal Fit')

    if linear:
        l_res = linear_fit(x, y, print_out=print_out)
        res["Linear Fit"] = l_res
        x1, x0 = max(x), min(x)
        x_line = [x0, x1]
        y_line = [l_res["intercept"] + x0 * l_res["slope"],
                  l_res["intercept"] + x1 * l_res["slope"]]
        ax.plot(x_line, y_line, color='r', label='Linear Fit')
        alpha_label = " %d%%" % ((1 - alpha) * 100)
        if show_PI:
            n = len(x)
            x_line = np.linspace(x0, x1, 100)
            t_value = t_dist.ppf(1 - alpha / 2, n - 2)
            x_mean = stat.mean(x)
            Sxx = sum([(xi - x_mean)**2 for xi in x])
            se_pred = l_res["Root MSE"] * np.sqrt(1 + 1 / n +
                                                  (x_line - x_mean)**2 / Sxx)
            y_line = t_value * se_pred + \
                l_res["slope"] * x_line + l_res["intercept"]
            ax.plot(
                x_line,
                y_line,
                linewidth=1,
                color='purple',
                label='PI' +
                alpha_label,
                linestyle='dashed')
            y_line = -t_value * se_pred + \
                l_res["slope"] * x_line + l_res["intercept"]
            ax.plot(
                x_line,
                y_line,
                color='purple',
                linestyle='dashed',
                linewidth=1)
        if show_CI:
            n = len(x)
            x_line = np.linspace(x0, x1, 100)
            x_mean = stat.mean(x)
            t_value = t_dist.ppf(1 - alpha / 2, n - 2)
            Sxx = sum([(xi - x_mean)**2 for xi in x])
            se_pred = np.sqrt(
                l_res["MSE"] * (1 / n + (x_line - x_mean)**2 / Sxx))
            y_line = t_value * se_pred + \
                l_res["slope"] * x_line + l_res["intercept"]
            ax.plot(
                x_line,
                y_line,
                color='g',
                label='CI' +
                alpha_label,
                linestyle='dashed', linewidth=1)
            y_line = -t_value * se_pred + \
                l_res["slope"] * x_line + l_res["intercept"]
            ax.plot(x_line, y_line, color='g', linestyle='dashed', linewidth=1)

    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(grid)
    if show_legend:
        ax.legend(loc='best', frameon=True)
    if show_plot:
        plt.show()
    if filename is not None:
        fname = str(filename) + '.png'
        plt.savefig(
            fname,
            dpi=200,
            format='png')
    return res
