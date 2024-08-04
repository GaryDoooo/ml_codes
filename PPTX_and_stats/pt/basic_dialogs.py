from tkinter import ttk
import tkinter as tk
from tkinter import TOP, LEFT, BOTH, X
from scipy.stats import probplot
########### Own Modules ###########
from dialog import Dialogs, addListBox
from describe import describe
from utilities import norm_test, number_list, mean_std_CIs


class MCorDialog(Dialogs):
    def createWidgets(self, m):
        f = tk.LabelFrame(m, text='Variables')
        f.pack(side=TOP, fill=BOTH, padx=2)
        w, self.grpvar = addListBox(
            f, values=self.cols, width=20, label='columns')
        w.pack(side=LEFT, fill=X, padx=10)

    #  return {"N": N, "mean": mean, "stdev": std, "SEM": SEM, "var": var,
    #          "coefvar": coefvar, "sum": sum(data), "min": min(data),
    #          "max": max(data), "Q1": qnt[0], "Q3": qnt[1], "median": median,
    #          "range": R, "IQR": IQR, "mode": mode, "n mode": N_mode,
    #          "skew": skew, "kurt": kurt, "quantiles": qnt2}
        self.ax_margin = tk.DoubleVar(value=0.1)
        self.red_ellipse = tk.BooleanVar(value=False)
        master = tk.LabelFrame(m, text='Plot Setting')
        master.pack(side=TOP, fill=BOTH, padx=2)
        w = tk.Label(master, text="Margin (0.1=10%% of data range)")
        w.pack(side=LEFT, fill=X, padx=2)
        w = tk.Entry(master, textvariable=self.ax_margin,
                     bg='white', width=5)
        w.pack(side=LEFT, padx=2, pady=2)
        w = tk.Checkbutton(master, text='Ellipse Outline',
                           variable=self.red_ellipse)
        w.pack(side=LEFT, padx=2, pady=2)
        self.add_alpha(m)
        return

    def ok(self):
        self.grpcols = self.grpvar.getSelectedItem()
        self.quit()
        self.apply()
        return

    def apply(self):

        data = number_2Dlist(df=self.df, cols=self.grpcols,
                             print_out=True, print_port=self.app.print)
        pf = self.app.showPlotViewer(figsize=(7, 7))
        axs = []
        n = len(data)
        try:
            ax_margin = self.ax_margin.get()
            alpha = self.alpha.get()
        except BaseException:
            ax_margin = 0.1
            alpha = 0.05

        for y in range(n - 1):
            r = []
            for x in range(1, n):
                r.append(
                    pf.fig.add_subplot(n - 1, n - 1, y * (n - 1) + x)
                )
            axs.append(r)

        multi_fit(
            data,
            self.grpcols,
            print_out=True,
            print_port=self.app.print,
            axs=axs,
            fig=pf.fig,
            alpha=alpha,
            ax_margin=ax_margin,
            red_ellipse=self.red_ellipse.get())
        return


class DescribeDialog(Dialogs):
    def createWidgets(self, m):
        f = tk.LabelFrame(m, text='Stats Summary')
        f.pack(side=TOP, fill=BOTH, padx=2)
        self.xvar = tk.StringVar(value="")
        w = ttk.Combobox(
            f, values=self.cols, textvariable=self.xvar,
            width=14)
        w.pack(side=LEFT, padx=2)

        self.pct = tk.StringVar(
            value="100, 99.5, 97.5, 90, 75, 50,25, 10, 2.5, 0.5, 0")
        f = tk.LabelFrame(m, text='Percentiles for Quantiles')
        f.pack(side=TOP, fill=BOTH, padx=2)
        w = tk.Entry(f, textvariable=self.pct,
                     bg='white', width=35)
        w.pack(side=LEFT, padx=2)
        return

    def apply(self):

        x = number_list(self.df[self.xvar.get()],
                        col_name=self.xvar.get(),
                        print_out=True, print_port=self.app.print)
        print(x)
        pct = self.pct.get()
        try:
            pct = [float(i) for i in pct.split(",") if 0 <= float(i) <= 100]
        except BaseException:
            pct = [100, 99.5, 97.5, 90, 75, 50, 25, 10, 2.5, 0.5, 0]
        describe(x, print_out=True, print_port=self.app.print,
                 percentiles=pct)
        return


class NormTestDialog(Dialogs):
    def createWidgets(self, m):
        f = tk.LabelFrame(m, text='Normality Test')
        f.pack(side=TOP, fill=BOTH, padx=2)
        self.xvar = tk.StringVar(value="")
        w = ttk.Combobox(
            f, values=self.cols, textvariable=self.xvar,
            width=14)
        w.pack(side=LEFT, padx=2)
        f = tk.LabelFrame(m, text='Plot')
        f.pack(side=TOP, fill=BOTH, padx=2)
        self.qq = tk.BooleanVar(value=False)
        w = tk.Checkbutton(f, text='Show QQ Plot',
                           variable=self.qq)
        w.pack(side=LEFT, padx=2, pady=2)
        return

    def apply(self):
        x = number_list(self.df[self.xvar.get()],
                        col_name=self.xvar.get(),
                        print_out=True, print_port=self.app.print)
        qq = self.qq.get()

        norm_test(x, print_out=True, print_port=self.app.print)
        if qq:
            pf = self.app.showPlotViewer()
            pf.ax = pf.fig.add_subplot(111)
            #  fit_plot(x, y, ax=pf.ax, print_port=self.app.print,
            probplot(x, dist="norm", plot=pf.ax)
            pf.ax.set_xlabel('Theoretical quantiles')
            pf.ax.set_ylabel('Observed Values')
        return


class CIDialog(Dialogs):
    def createWidgets(self, m):
        f = tk.LabelFrame(m, text='Mean & Std CI')
        f.pack(side=TOP, fill=BOTH, padx=2)
        self.xvar = tk.StringVar(value="")
        w = ttk.Combobox(
            f, values=self.cols, textvariable=self.xvar,
            width=14)
        w.pack(side=LEFT, padx=2)
        self.add_alpha(m)
        return

    def apply(self):
        x = number_list(self.df[self.xvar.get()],
                        col_name=self.xvar.get(),
                        print_out=True, print_port=self.app.print)
        alpha = self.alpha.get()
        mean_std_CIs(x, alpha=alpha, print_out=True, print_port=self.app.print)
        return
