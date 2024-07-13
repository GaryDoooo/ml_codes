from tkinter import ttk
import tkinter as tk
from tkinter import TOP, LEFT, BOTH
from scipy.stats import probplot
########### Own Modules ###########
from dialog import Dialogs
from describe import describe
from utilities import norm_test


class DescribeDialog(Dialogs):
    def createWidgets(self, m):
        f = tk.LabelFrame(m, text='Stats Summary')
        f.pack(side=TOP, fill=BOTH, padx=2)
        self.xvar = tk.StringVar(value="")
        w = ttk.Combobox(
            f, values=self.valcols, textvariable=self.xvar,
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

        x = list(self.df[self.xvar.get()])
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
            f, values=self.valcols, textvariable=self.xvar,
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
        x = list(self.df[self.xvar.get()])
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
            f, values=self.valcols, textvariable=self.xvar,
            width=14)
        w.pack(side=LEFT, padx=2)
        self.add_alpha()
        return

    def apply(self):

        x = list(self.df[self.xvar.get()])
        alpha= self.alpha.get()
        
        describe(x, print_out=True, print_port=self.app.print,
                 percentiles=pct)
        return
