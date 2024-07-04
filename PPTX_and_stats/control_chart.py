import numpy as np
import matplotlib.pyplot as plt
import statistics as stat
####### Own modules ##########
from ctrl_chart_const import df as Ctrl_Cht_Const


def x_mR(x):  # , print_out=True, xLabels=None,max_xlabels=25):

    # Define list variable for moving ranges
    MR = [np.nan]
    for i in range(1, len(x)):
        MR.append(abs(x[i] - x[i - 1]))

    x_bar = stat.mean(x)
    R_bar = stat.mean(MR[1:])
#     E2=3/d2, when n=2 two numbers for range, E2=2.659
    E2 = 2.659
    x_UCL = x_bar + E2 * R_bar
    x_LCL = x_bar - E2 * R_bar

    # while n=2, D4=3.267
    D4 = 3.267
    R_UCL = D4 * R_bar
    R_LCL = 0

    return {"Y1": x, "Y2": MR, "bar1": x_bar, "ucl1": x_UCL,
            "ucl2": R_UCL, "lcl1": x_LCL, "lcl2": R_LCL,
            "bar2": R_bar, "n": 2,
            "ylabel1": "Individual Values",
            "ylabel2": "Moving Range (n=2)"}

    #  return x,MR,x_bar,ucl1,ucl2,lcl2,lcl2

    #  control_plot(Y1=x, Y2=MR, bar1=x_bar, ucl1=x_UCL,
    #               ucl2=R_UCL, lcl1=x_LCL, lcl2=R_LCL,
    #               bar2=R_bar, xLabels=xLabels,
    #               print_out=print_out,
    #               ylabel1="Individual Values",
    #               ylabel2="Moving Range (n=2)",
    #               max_label_num=max_xlabels)


# the number of samples each day need be consistent over time
# It's a sampling process not all the products each day.
# otherwise can't estimate an A2 value for UCL and LCL

def xBar_R(data):  # , print_out=True, max_xlabels=25,xLabels=None):

    xbar = [stat.mean(l) for l in data]
    R = [max(l) - min(l) for l in data]
    n = len(data[0])
    A2 = Ctrl_Cht_Const["A2"][n]
    xbar_bar = stat.mean(xbar)
    R_bar = stat.mean(R)
    xbar_ucl = xbar_bar + A2 * R_bar
    xbar_lcl = xbar_bar - A2 * R_bar
    D4 = Ctrl_Cht_Const["D4"][n]
    D3 = Ctrl_Cht_Const["D3"][n]
    R_UCL = D4 * R_bar
    R_LCL = D3 * R_bar
    #  if print_out:
    #      print("n = %d" % n)
    #

    return {"Y1": xbar, "Y2": R, "bar1": xbar_bar, "ucl1": xbar_ucl,
            "ucl2": R_UCL, "lcl1": xbar_lcl, "lcl2": R_LCL, "n": n,
            "bar2": R_bar, "ylabel1": "X Bar", "ylabel2": "Range"}
    #  control_plot(Y1=xbar, Y2=R, bar1=xbar_bar, ucl1=xbar_ucl,
    #               ucl2=R_UCL, lcl1=xbar_lcl, lcl2=R_LCL,
    #               bar2=R_bar, xLabels=xLabels,
    #               print_out=print_out,
    #               ylabel1="X Bar",
    #               ylabel2="Range",
    #               max_label_num=max_xlabels)


def xBar_S(data):  # , print_out=True, max_xlabels=25,xLabels=None):

    xbar = [stat.mean(l) for l in data]
    S = [stat.stdev(l) for l in data]
    n = len(data[0])
    A3 = Ctrl_Cht_Const["A3"][n]
    xbar_bar = stat.mean(xbar)
    S_bar = stat.mean(S)
    xbar_ucl = xbar_bar + A3 * S_bar
    xbar_lcl = xbar_bar - A3 * S_bar
    B4 = Ctrl_Cht_Const["B4"][n]
    B3 = Ctrl_Cht_Const["B3"][n]
    S_UCL = B4 * S_bar
    S_LCL = B3 * S_bar

    #  if print_out:
    #      print("n = %d" % n)
    #
    return {"Y1": xbar, "Y2": S, "bar1": xbar_bar, "ucl1": xbar_ucl,
            "ucl2": S_UCL, "lcl1": xbar_lcl, "lcl2": S_LCL, "n": n,
            "bar2": S_bar, "ylabel1": "X Bar", "ylabel2": "Stdev"}

    #  control_plot(Y1=xbar, Y2=S, bar1=xbar_bar, ucl1=xbar_ucl,
    #               ucl2=S_UCL, lcl1=xbar_lcl, lcl2=S_LCL,
    #               bar2=S_bar, xLabels=xLabels,
    #               print_out=print_out,
    #               ylabel1="X Bar",
    #               ylabel2="Stdev",
    #               max_label_num=max_xlabels)


def p_np_plot(p=None, n=1,
              bar1=None, ucl1=None, lcl1=None, xLabels=None,
              print_out=True, max_label_num=25,
              ylabel="P"):

    if isinstance(n, int):
        nlist = [n] * len(p)
    else:
        nlist = n

    p_bar = sum([i * j for i, j in zip(p, nlist)]) / sum(nlist)
    ucl_list = [p_bar + 3 * (p_bar * (1 - p_bar) / i)**.5 for i in nlist]
    lcl_list = [max(0, p_bar - 3 * (p_bar * (1 - p_bar) / i)**.5)
                for i in nlist]

    xs = [-.5]
    for _ in range(len(p)):
        xs.append(xs[-1] + 1)
        xs.append(xs[-1])
    xs = xs[:-1]

    lcl_ys, ucl_ys = [], []
    for ucl in ucl_list:
        ucl_ys.append(ucl)
        ucl_ys.append(ucl)
    for lcl in lcl_list:
        lcl_ys.append(lcl)
        lcl_ys.append(lcl)

    fig, ax = plt.subplots(1, figsize=(15, 15))

    ax.plot(p, linestyle='-', marker='o', color='black')

    if bar1 is not None:
        p_bar = bar1
    ax.axhline(p_bar, color='blue')

    if ucl1 is not None:
        ax.axhline(ucl1, color='red', linestyle='dashed')
    else:
        ax.plot(xs, ucl_ys, color='red')
    if lcl1 is not None:
        ax.axhline(lcl1, color='red', linestyle='dashed')
    else:
        ax.plot(xs, lcl_ys, color='red')

    ax.set(ylabel=ylabel)

    if xLabels is not None:
        step = 1
        if len(xLabels) > max_label_num:
            step = int(len(xLabels) / max_label_num + 1)
        ax.set_xticks(range(len(xLabels)), xLabels,
                      rotation='vertical')
        ax.set_xticks(ax.get_xticks()[::step])

    plt.show()

    if print_out:
        print(ylabel)
        print("mean = %.4f" % (p_bar))


def x_plot(data, bar1=None,
           ucl1=None, lcl1=None, bar2=None,
           ucl2=None, lcl2=None, xLabels=None,
           print_out=False, max_label_num=25,
           ylabel1=None, ylabel2=None,
           xlabel=None, ax=None,
           one_chart=False, show_plot=False,
           filename=None, plot_type="x_mR"):

    plot_type = plot_type.upper()
    if "BAR" in plot_type and "R" in plot_type.replace("BAR", ""):
        s = xBar_R(data)
    elif "BAR" in plot_type and "S" in plot_type:
        s = xBar_S(data)
    else:
        s = x_mR(data)

    bar1 = bar1 if bar1 is not None else s["bar1"]
    bar2 = bar2 if bar2 is not None else s["bar2"]
    ucl1 = ucl1 if ucl1 is not None else s["ucl1"]
    ucl2 = ucl2 if ucl2 is not None else s["ucl2"]
    lcl1 = lcl1 if lcl1 is not None else s["lcl1"]
    lcl2 = lcl2 if lcl2 is not None else s["lcl2"]
    ylabel1 = ylabel1 if ylabel1 is not None else s["ylabel1"]
    ylabel2 = ylabel2 if ylabel2 is not None else s["ylabel2"]
    n = s["n"]

    if ax is not None:
        one_chart = True
        axs = [ax, ax]
    elif one_chart:
        fig, ax = plt.subplots(1)  # , figsize=(15, 15))
        axs = [ax, ax]
    else:
        fig, axs = plt.subplots(2)  # , figsize=(15, 15), sharex=True)
        # Remove vertical space between Axes
        fig.subplots_adjust(hspace=0)

    axs[0].plot(s["Y1"], linestyle='-', marker='o', color='black',
                linewidth=1, markersize=3)
    axs[0].axhline(bar1, color='blue')
    axs[0].axhline(ucl1, color='red', linestyle='dashed')
    axs[0].axhline(lcl1, color='red', linestyle='dashed')
    axs[0].set(ylabel=ylabel1)

    if not one_chart:
        axs[1].plot(s["Y2"], linestyle='-', marker='o', color='black',
                    linewidth=1, markersize=3)
        axs[1].axhline(bar2, color='blue')
        axs[1].axhline(ucl2, color='red', linestyle='dashed')
        axs[1].axhline(lcl2, color='red', linestyle='dashed')
        axs[1].set_ylim(bottom=0)
        axs[1].set(ylabel=ylabel2)

    if xLabels is not None:
        step = 1
        if len(xLabels) > max_label_num:
            step = int(len(xLabels) / max_label_num + 1)
        axs[1].set_xticks(range(len(xLabels)), xLabels,
                          rotation='vertical')
        axs[1].set_xticks(axs[1].get_xticks()[::step])

    if xlabel is not None:
        axs[1].set(xlabel=xlabel)

    if show_plot:
        plt.show()

    if filename is not None:
        fname = str(filename) + '.png'
        plt.savefig(
            fname,
            dpi=200,
            format='png')

    if print_out:
        print(ylabel1)
        print("LCL=%.2f\tmean = %.2f\tUCL=%.2f" % (
            lcl1, bar1, ucl1))
        print(ylabel2)
        print("LCL=%.2f\tmean = %.2f\tUCL=%.2f" % (
            lcl2, bar2, ucl2))
        print("n =", n)

    res = {"lcl1": lcl1, "bar1": bar1, "ucl1": ucl1,
           "lcl2": lcl2, "bar2": bar2, "ucl2": ucl2,
           "n": n}

    return res
