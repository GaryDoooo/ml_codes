from tkinter import ttk
import tkinter as tk
from tkinter import TOP, LEFT, X, BOTH
########### Own Modules ###########
from linear_plot import fit_plot
from dialog import Dialogs


class LinearFitDialog(Dialogs):
    def createWidgets(self, m):
        """Create a set of grp-agg-func options together"""
        master = self.main
        f = tk.LabelFrame(m, text='X Y Values')
        f.pack(side=TOP, fill=BOTH, padx=2)
        self.xvar = tk.StringVar(value="")
        self.yvar = tk.StringVar(value="")
        w = tk.Label(f, text="X")
        w.pack(side=LEFT, fill=X, padx=2)
        w = ttk.Combobox(
            f, values=self.valcols, textvariable=self.xvar,
            width=14)
        w.pack(side=LEFT, padx=2)
        w = tk.Label(f, text="Y")
        w.pack(side=LEFT, fill=X, padx=2)
        w = ttk.Combobox(
            f, values=self.valcols, textvariable=self.yvar,
            width=14)
        w.pack(side=LEFT, padx=2)
        self.ellipse = tk.BooleanVar(value=False)
        self.linear = tk.BooleanVar(value=True)
        self.ortho = tk.BooleanVar(value=False)
        self.ortho_ratio = tk.DoubleVar(value=1)
        self.show_CI = tk.BooleanVar(value=False)
        self.show_PI = tk.BooleanVar(value=False)
        self.scatter = tk.BooleanVar(value=True)

        ####### extension #######
        self.update_vars()

        master = tk.LabelFrame(m, text='Correlation')
        master.pack(side=TOP, fill=BOTH, padx=2)
        w = tk.Checkbutton(master, text='Scatter Dots',
                           variable=self.scatter)
        w.pack(side=LEFT, padx=2, pady=2)
        w = tk.Checkbutton(master, text='Correlation Ellipse',
                           variable=self.ellipse)
        w.pack(side=LEFT, padx=2, pady=2)

        master = tk.LabelFrame(m, text='Linear Fit')
        master.pack(side=TOP, fill=BOTH, padx=2)
        w = tk.Checkbutton(master, text='Show Fit',
                           variable=self.linear)
        w.pack(side=LEFT, padx=2, pady=2)
        w = tk.Checkbutton(master, text='Confidence Interval',
                           variable=self.show_CI)
        w.pack(side=LEFT, padx=2, pady=2)
        w = tk.Checkbutton(master, text='Prediction Interval',
                           variable=self.show_PI)
        w.pack(side=LEFT, padx=2, pady=2)

        master = tk.LabelFrame(m, text='Orthogonal Fit')
        master.pack(side=TOP, fill=BOTH, padx=2)
        w = tk.Checkbutton(master, text='Show Fit',
                           variable=self.ortho)
        w.pack(side=LEFT, padx=2, pady=2)
        w = tk.Label(master, text="Ratio")
        w.pack(side=LEFT, fill=X, padx=2)
        w = tk.Entry(master, textvariable=self.ortho_ratio,
                     bg='white', width=5)
        w.pack(side=LEFT, padx=2, pady=2)

        self.add_xy_plot_settings(m)
        self.add_alpha(m)
        return

    def apply(self):
        """Apply crosstab"""

        x = list(self.df[self.xvar.get()])
        y = list(self.df[self.yvar.get()])
        pf = self.app.showPlotViewer()
        pf.ax = pf.fig.add_subplot(111)

        self.get_plot_settings()

        fit_plot(x, y, ax=pf.ax, print_port=self.app.print,
                 alpha=self.alpha.get(),
                 ortho_ratio=self.ortho_ratio.get(),
                 ellipse=self.ellipse.get(),
                 linear=self.linear.get(), show_CI=self.show_CI.get(),
                 ortho=self.ortho.get(), show_PI=self.show_PI.get(),
                 xlabel=self.xlabel if self.xlabel != "" else self.xvar.get(),
                 ylabel=self.ylabel if self.ylabel != "" else self.yvar.get(),
                 x_min=self.x_min, y_min=self.y_min,
                 x_max=self.x_max, y_max=self.y_max,
                 ax_margin=self.ax_margin,
                 show_legend=self.show_legend, grid=self.grid,
                 scatter=self.scatter.get(), print_out=True
                 )
        return


class CorrelationDialog(LinearFitDialog):
    def update_vars(self):
        self.linear = tk.BooleanVar(value=False)
        self.ellipse = tk.BooleanVar(value=True)
        return


class OrthoFitDialog(LinearFitDialog):
    def update_vars(self):
        self.linear = tk.BooleanVar(value=False)
        self.ortho = tk.BooleanVar(value=True)
        return
