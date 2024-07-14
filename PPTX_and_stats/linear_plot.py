import numpy as np
import matplotlib.pyplot as plt
import statistics as stat
from scipy.stats import t as t_dist
from prettytable import PrettyTable as PT
###### Own modules #######
from linear_fit import linear_fit
from ortho_fit import orthogonal_fit
from utilities import pearson_correlation


def fit_plot(x, y, alpha=0.05, print_out=False,
             ellipse=False, linear=False,
             ortho=False, ortho_ratio=1,
             show_CI=False, show_PI=False,
             show_plot=False, filename=None,
             xlabel=None, ylabel=None,
             grid=False, show_legend=False,
             x_min=None, x_max=None,
             y_min=None, y_max=None,
             scatter=True, ax=None,
             ax_margin=0.1, print_port=print):

    print = print_port
    #  print("test")
    res = dict()
    if x_min is None:
        x_min = min(x) - (max(x) - min(x)) * ax_margin
    if x_max is None:
        x_max = max(x) + (max(x) - min(x)) * ax_margin
    if y_min is None:
        y_min = min(y) - (max(y) - min(y)) * ax_margin
    if y_max is None:
        y_max = max(y) + (max(y) - min(y)) * ax_margin

    if ax is None:
        _, ax = plt.subplots()

    if scatter:
        ax.scatter(x, y, color='blue', alpha=1 / (len(x))**.2,
                   label='Data points')

    if ellipse:
        correlation = pearson_correlation(x, y, alpha=alpha, print_port=print,
                                          print_out=print_out)
        res["Pearson"] = correlation
        # Use parametric equations to generate points on the ellipse:
        # x(t) = x̄ + a * cos(t) * cos(θ) - b * sin(t) * sin(θ)
        # y(t) = ȳ + a * cos(t) * sin(θ) + b * sin(t) * cos(θ)
        theta = np.linspace(0, np.pi * 2, 100)
        a = res["Pearson"]["ellipse"]["a"]
        b = res["Pearson"]["ellipse"]["b"]
        t = res["Pearson"]["ellipse"]["theta"]
        x_line = np.mean(x) + a * np.cos(theta) * np.cos(t) - \
            b * np.sin(theta) * np.sin(t)
        y_line = np.mean(y) + a * np.cos(theta) * np.sin(t) + \
            b * np.sin(theta) * np.cos(t)
        ax.fill(x_line, y_line, alpha=0.1, facecolor='blue', edgecolor='none')
        #  ax.plot(x_line, y_line)

    if ortho:
        ortho_res = orthogonal_fit(
            x,
            y,
            error_ratio=ortho_ratio,
            print_port=print,
            print_out=print_out,
            alpha=alpha)
        res["Orthogonal Fit"] = ortho_res
        x1, x0 = x_max, x_min
        x_line = [x0, x1]
        y_line = [ortho_res["intercept"] + x0 * ortho_res["slope"],
                  ortho_res["intercept"] + x1 * ortho_res["slope"]]
        ax.plot(x_line, y_line, color='k', label='Orthogonal Fit')

    if linear:
        l_res = linear_fit(x, y, print_out=print_out, print_port=print)
        res["Linear Fit"] = l_res
        x1, x0 = x_max, x_min
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

    ax.set(xlabel=xlabel)
    ax.set(ylabel=ylabel)
    ax.grid(grid)
    ax.set_xlim(left=x_min, right=x_max)
    ax.set_ylim(bottom=y_min, top=y_max)
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


def multi_fit(data, labels, print_out=False, print_port=print,
              axs=None, fig=None,
              show_plot=False, filename=None, ax_margin=0.1):

    t = PT(["\\"] + labels)
    cor_res = []
    n = len(data)
    for y in range(n):
        res_tmp = []
        row = [labels[y]]
        for x in range(n):
            r = pearson_correlation(data[x], data[y], print_out=False)
            row.append("%.3f" % r["r"])
            res_tmp.append(r)
        cor_res.append(res_tmp)
        t.add_row(row)
    res = {"pearson": cor_res}

    if print_out:
        print = print_port
        print("\n---- Pearson correlation coefficient ----")
        print(t)

    if axs is None or fig is None:
        fig, axs = plt.subplots(n - 1, n - 1)  # , sharex=True, sharey=True)
    # Remove vertical space between Axes
    fig.subplots_adjust(hspace=0)
    fig.subplots_adjust(wspace=0)

    for x in range(len(data) - 1):
        for y in range(1, len(data)):
            fx, fy = x, y - 1
            if x >= y:
                axs[fy][fx].axis('off')
            else:
                fit_plot(data[x], data[y], ax_margin=ax_margin,
                         ellipse=True, ax=axs[fy][fx],
                         xlabel=labels[x] if y == n - 1 else None,
                         ylabel=labels[y] if x == 0 else None)
                if x > 0:
                    axs[fy][fx].get_yaxis().set_visible(False)
    if show_plot:
        plt.show()
    if filename is not None:
        fname = str(filename) + '.png'
        plt.savefig(
            fname,
            dpi=200,
            format='png')
    return res


if __name__ == "__main__":
    data = [[11, 12, 13, 11.2, 12], [3, 4, 2, 3.3, 4.4],
            [3, 2, 1, 13, 12], [-3, -2, -1, -13, -12]]
    labels = ["AAlksdfsjd", "sskdf", "sdejf", "d"]
    multi_fit(data, labels, filename="test_multi")
