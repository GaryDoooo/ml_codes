from pandastable_local.dialogs import BaseDialog  # , addListBox
from tkinter import Frame, TOP, LEFT, X, BOTH
import tkinter as tk
import numpy as np


class Dialogs(BaseDialog):
    def __init__(self, parent=None, df=None, title='', app=None):

        BaseDialog.__init__(self, parent, df, title)
        self.app = app
        m = Frame(self.main)
        m.pack(side=TOP)

        self.cols = list(self.df.columns)
        self.valcols = list(
            self.df.select_dtypes(
                include=[
                    np.float64,
                    np.int32,
                    np.int64]))
        #  self.vars = OrderedDict()
        self.createWidgets(m)
        self.buttonsFrame()
        return

    def buttonsFrame(self):
        bf = Frame(self.main)
        bf.pack(side=TOP, fill=BOTH)
        b = tk.Button(bf, text="OK", command=self.ok)
        b.pack(side=LEFT, fill=X, expand=1, pady=2)
        b = tk.Button(bf, text="Cancel", command=self.quit)
        b.pack(side=LEFT, fill=X, expand=1, pady=2)
        b = tk.Button(bf, text="Help", command=self.help)
        b.pack(side=LEFT, fill=X, expand=1, pady=2)
        return

    def ok(self):
        self.quit()
        self.apply()
        return

    def add_xy_plot_settings(self, m):
        self.xlabel = tk.StringVar(value="")
        self.ylabel = tk.StringVar(value="")
        self.grid = tk.BooleanVar(value=False)
        self.show_legend = tk.BooleanVar(value=False)
        self.x_min = tk.StringVar(value="Auto")
        self.x_max = tk.StringVar(value="Auto")
        self.y_min = tk.StringVar(value="Auto")
        self.y_max = tk.StringVar(value="Auto")
        self.ax_margin = tk.DoubleVar(value=0.1)
        master = tk.LabelFrame(m, text='X Axis')
        master.pack(side=TOP, fill=BOTH, padx=2)
        w = tk.Label(master, text="Label")
        w.pack(side=LEFT, fill=X, padx=2)
        w = tk.Entry(master, textvariable=self.xlabel,
                     bg='white', width=15)
        w.pack(side=LEFT, padx=2, pady=2)
        w = tk.Label(master, text="Min")
        w.pack(side=LEFT, fill=X, padx=2)
        w = tk.Entry(master, textvariable=self.x_min,
                     bg='white', width=5)
        w.pack(side=LEFT, padx=2, pady=2)
        w = tk.Label(master, text="Max")
        w.pack(side=LEFT, fill=X, padx=2)
        w = tk.Entry(master, textvariable=self.x_max,
                     bg='white', width=5)
        w.pack(side=LEFT, padx=2, pady=2)

        master = tk.LabelFrame(m, text='Y Axis')
        master.pack(side=TOP, fill=BOTH, padx=2)
        w = tk.Label(master, text="Label")
        w.pack(side=LEFT, fill=X, padx=2)
        w = tk.Entry(master, textvariable=self.ylabel,
                     bg='white', width=15)
        w.pack(side=LEFT, padx=2, pady=2)
        w = tk.Label(master, text="Min")
        w.pack(side=LEFT, fill=X, padx=2)
        w = tk.Entry(master, textvariable=self.y_min,
                     bg='white', width=5)
        w.pack(side=LEFT, padx=2, pady=2)
        w = tk.Label(master, text="Max")
        w.pack(side=LEFT, fill=X, padx=2)
        w = tk.Entry(master, textvariable=self.y_max,
                     bg='white', width=5)
        w.pack(side=LEFT, padx=2, pady=2)

        master = tk.LabelFrame(m, text='Plot Setting')
        master.pack(side=TOP, fill=BOTH, padx=2)
        w = tk.Checkbutton(master, text='Show Grid',
                           variable=self.grid)
        w.pack(side=LEFT, padx=2, pady=2)
        w = tk.Checkbutton(master, text='Show Legend',
                           variable=self.show_legend)
        w.pack(side=LEFT, padx=2, pady=2)
        w = tk.Label(master, text="Margin")
        w.pack(side=LEFT, fill=X, padx=2)
        w = tk.Entry(master, textvariable=self.ax_margin,
                     bg='white', width=5)
        w.pack(side=LEFT, padx=2, pady=2)
        return

    def add_alpha(self, m):
        self.alpha = tk.DoubleVar(value=0.05)
        master = tk.LabelFrame(m, text='Alpha for CI and etc.')
        master.pack(side=TOP, fill=BOTH, padx=2)
        w = tk.Label(master, text="Alpha")
        w.pack(side=LEFT, fill=X, padx=2)
        w = tk.Entry(master, textvariable=self.alpha,
                     bg='white', width=5)
        w.pack(side=LEFT, padx=2, pady=2)
        return

    def get_plot_settings(self):
        try:
            self.x_max = float(self.x_max.get())
        except BaseException:
            self.x_max = None
        try:
            self.x_min = float(self.x_min.get())
        except BaseException:
            self.x_min = None
        try:
            self.y_max = float(self.y_max.get())
        except BaseException:
            self.y_max = None
        try:
            self.y_min = float(self.y_min.get())
        except BaseException:
            self.y_min = None
        self.ax_margin = self.ax_margin.get()
        self.xlabel = self.xlabel.get()
        self.ylabel = self.ylabel.get()
        self.show_legend = self.show_legend.get()
        self.grid = self.grid.get()
        return

    def update_vars(self):
        """ Do nothing, can be updated """
        return
