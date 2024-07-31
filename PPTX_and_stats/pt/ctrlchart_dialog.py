
from tkinter import ttk
import tkinter as tk
from tkinter import TOP, LEFT, X, BOTH, RIGHT
###################################
#  from pandastable_local.dialogs import addListBox
########### Own Modules ###########
from dialog import Dialogs
from utilities import is_number, number_list, filter_voids, grouping_by_labels, get_number
from control_chart import x_plot


class IMRDialog(Dialogs):
    def createWidgets(self, m):
        self.input_data(m)
        self.more_settings(m)
        self.mr_range = tk.IntVar(value=2)
        return

    def input_data(self, m):
        f = tk.LabelFrame(m, text='Input Column')
        f.pack(side=TOP, fill=BOTH, padx=2)
        self.xvar = tk.StringVar(value="")
        w = tk.Label(f, text="Values")
        w.pack(side=LEFT, fill=X, padx=2)
        w = ttk.Combobox(
            f, values=self.cols, textvariable=self.xvar,
            width=14)
        w.pack(side=LEFT, padx=2)
        self.mr_range = tk.IntVar(value=2)
        w = tk.Label(f, text="Moving Range")
        w.pack(side=LEFT, fill=X, padx=2)
        w = tk.Entry(f, textvariable=self.mr_range,
                     bg='white', width=5)
        w.pack(side=LEFT, padx=2, pady=2)

        return

    def more_settings(self, m):
        self.x_options(m)
        self.y_options(m, label1="",  # "Individual Values",
                       label2="")  # Moving Range (n=2)")
        self.y_refs(m, label1=" ",
                    label2=" ")
        self.one_chart = False
        self.chart_two_only = False
        self.plot_type = "x_mR"
        return

    def y_refs(self, m, label1=None, label2=None):
        master = tk.LabelFrame(m, text='Y ref lines (optional)')
        master.pack(side=TOP, fill=BOTH, padx=2)
        self.y1ref = tk.StringVar(value=label1)
        self.y2ref = tk.StringVar(value=label2)

        w = tk.Label(master, text="Y positions (sep by ,)")
        w.pack(side=LEFT, fill=X, padx=2)
        if label1 is None:
            w = tk.Entry(master, textvariable=self.y2ref,
                         bg='white', width=15)
        else:
            w = tk.Entry(master, textvariable=self.y1ref,
                         bg='white', width=15)
        w.pack(side=LEFT, padx=2, pady=2)
        if label2 is None or label1 is None:
            return
        w = tk.Label(master, text="Y pos for chart 2")
        w.pack(side=LEFT, fill=X, padx=2)
        w = tk.Entry(master, textvariable=self.y2ref,
                     bg='white', width=15)
        w.pack(side=LEFT, padx=2, pady=2)
        return

    def y_options(self, m, label1=None, label2=None):
        master = tk.LabelFrame(m, text='Y axis setting (optional)')
        master.pack(side=TOP, fill=BOTH, padx=2)
        self.y1label = tk.StringVar(value=label1)
        self.y2label = tk.StringVar(value=label2)

        w = tk.Label(master, text="Y Label")
        w.pack(side=LEFT, fill=X, padx=2)
        if label1 is None:
            w = tk.Entry(master, textvariable=self.y2label,
                         bg='white', width=15)
        else:
            w = tk.Entry(master, textvariable=self.y1label,
                         bg='white', width=15)
        w.pack(side=LEFT, padx=2, pady=2)
        if label2 is None or label1 is None:
            return
        w = tk.Label(master, text="Y Label for chart 2")
        w.pack(side=LEFT, fill=X, padx=2)
        w = tk.Entry(master, textvariable=self.y2label,
                     bg='white', width=15)
        w.pack(side=LEFT, padx=2, pady=2)
        return

    def x_options(self, m):
        master = tk.LabelFrame(m, text='X axis setting (optional)')
        master.pack(side=TOP, fill=BOTH, padx=2)
        self.max_x_labels = tk.DoubleVar(value=25)
        self.xlabel = tk.StringVar(value="")
        self.xlabelID = tk.StringVar(value="")

        w = tk.Label(master, text="X Label")
        w.pack(side=LEFT, fill=X, padx=2)
        w = tk.Entry(master, textvariable=self.xlabel,
                     bg='white', width=15)
        w.pack(side=LEFT, padx=2, pady=2)

        w = tk.Label(master, text="Axes Label Col.")
        w.pack(side=LEFT, fill=X, padx=2)
        w = ttk.Combobox(
            master, values=self.cols, textvariable=self.xlabelID,
            width=14)
        w.pack(side=LEFT, padx=2)
        w = tk.Label(master, text="Max Axes Labels")
        w.pack(side=LEFT, fill=X, padx=2)
        w = tk.Entry(master, textvariable=self.max_x_labels,
                     bg='white', width=15)
        w.pack(side=LEFT, padx=2, pady=2)
        return

    def get_data(self):
        xlabels = None
        if self.xlabelID.get() == "":
            data = number_list(self.df[self.xvar.get()])
            xlabels = list(range(1, len(data) + 1))
        else:
            ids = self.df[self.xlabelID.get()]
            x = self.df[self.xvar.get()]
            [x, ids] = filter_voids([x, ids])
            data, xlabels = [], []
            for i, j in zip(x, ids):
                if is_number(i):
                    data.append(float(i))
                    xlabels.append(j)
        fig, ax, axs = self.get_axs()
        return data, xlabels, fig, ax, axs

    def get_axs(self):
        pf = self.app.showPlotViewer()
        fig = pf.fig
        ax1 = fig.add_subplot(2, 1, 1)  # 2 rows, 1 column, first plot
        ax2 = fig.add_subplot(2, 1, 2)  # 2 rows, 1 column, second plot
        return fig, None, [ax1, ax2]

    def apply(self):
        data, xlabels, fig, ax, axs = self.get_data()
        x_plot(
            data, xLabels=xlabels,
            xlabel=self.xvar.get() if self.xlabel.get() == "" else self.xlabel.get(),
            ylabel1=None if self.y1label.get() == "" else self.y1label.get(),
            ylabel2=None if self.y2label.get() == "" else self.y2label.get(),
            max_label_num=self.max_x_labels.get(),
            one_chart=self.one_chart,
            chart_two_only=self.chart_two_only,
            refY1=self.y1ref.get(), refY2=self.y2ref.get(),
            print_out=True, plot_type=self.plot_type,
            mr_range=self.mr_range.get(),
            fig=fig, ax=ax, axs=axs,
            print_port=self.app.print)

        return


class IDialog(IMRDialog):
    def input_data(self, m):
        f = tk.LabelFrame(m, text='Input Column')
        f.pack(side=TOP, fill=BOTH, padx=2)
        self.xvar = tk.StringVar(value="")
        w = tk.Label(f, text="Values")
        w.pack(side=LEFT, fill=X, padx=2)
        w = ttk.Combobox(
            f, values=self.cols, textvariable=self.xvar,
            width=14)
        w.pack(side=LEFT, padx=2)
        self.mr_range = tk.IntVar(value=2)
        return

    def more_settings(self, m):
        self.x_options(m)
        self.y_options(m, label1="")
        self.y_refs(m, label1=" ")
        self.one_chart = True
        self.chart_two_only = False
        self.plot_type = "x_mR"
        return

    def get_axs(self):
        pf = self.app.showPlotViewer()
        fig = pf.fig
        pf.ax = pf.fig.add_subplot(111)
        return fig, pf.ax, None


class MRDialog(IMRDialog):

    def more_settings(self, m):
        self.x_options(m)
        self.y_options(m,  # label1="",  # "Individual Values",
                       label2="")  # Moving Range (n=2)")
        self.y_refs(m,  # label1=" ",
                    label2=" ")
        self.one_chart = False
        self.chart_two_only = True
        self.plot_type = "x_mR"
        return

    def get_axs(self):
        pf = self.app.showPlotViewer()
        fig = pf.fig
        pf.ax = pf.fig.add_subplot(111)
        return fig, pf.ax, None


class XBRDialog(IMRDialog):

    def input_data(self, m):
        f = tk.LabelFrame(m, text='Input Column')
        f.pack(side=TOP, fill=BOTH, padx=2)
        self.xvar = tk.StringVar(value="")
        w = tk.Label(f, text="Values")
        w.pack(side=LEFT, fill=X, padx=2)
        w = ttk.Combobox(
            f, values=self.cols, textvariable=self.xvar,
            width=14)
        w.pack(side=LEFT, padx=2)
        ff = tk.LabelFrame(f, text='Grouping By')
        ff.pack(side=RIGHT, fill=X, padx=2)
        self.gsize = tk.StringVar(value="")
        self.gid = tk.StringVar(value="")
        w = tk.Label(ff, text="Size")
        w.pack(side=LEFT, fill=X, padx=2)
        w = tk.Entry(ff, textvariable=self.gsize,
                     bg='white', width=5)
        w.pack(side=LEFT, padx=2, pady=2)
        w = tk.Label(ff, text="ID Col.")
        w.pack(side=LEFT, fill=X, padx=2)
        w = ttk.Combobox(
            ff, values=self.cols, textvariable=self.gid,
            width=14)
        w.pack(side=LEFT, padx=2)

        return

    def get_data(self):
        self.plot_type = "XBAR_R"
        gsize = get_number(self.gsize)
        xid = self.xvar.get()
        if xid not in list(self.df):
            self.error("Can't get data.")
            return
        if gsize is None:
            gid = self.gid.get()
            if gid not in list(self.df):
                self.error("Can't get valid a grouping method.")
                return
            data, keys = grouping_by_labels(self.df[xid],
                                            self.df[gid], return_keys=True)
        else:
            gsize = int(gsize)
            l = list(self.df[xid])
            if gsize > 0:
                data = [l[i:i + gsize] for i in range(0, len(l), gsize)]

        if self.xlabelID.get() == "":
            if gsize is None:
                xlabels = keys
            xlabels = list(range(1, len(data) + 1))
        else:
            ids = self.df[self.xlabelID.get()]
            [ids] = filter_voids([ids])
            xlabels = list(range(1, len(data) + 1))
            for i, v in enumerate(ids):
                try:
                    xlabels[i] = v
                except BaseException:
                    pass

        fig, ax, axs = self.get_axs()
        return data, xlabels, fig, ax, axs
