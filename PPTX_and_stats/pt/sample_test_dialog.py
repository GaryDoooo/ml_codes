import tkinter as tk
from tkinter import TOP, BOTH, LEFT, X, ttk
########### Own Modules ###########
from dialog import Dialogs
from utilities import number_list, get_number
from t_test import t_test_1sample, z_test_1sample


class Mean1SampleDialog(Dialogs):
    def createWidgets(self, m):
        """Create a set of grp-agg-func options together"""
        #  w = tk.Label(
        #      m, anchor="e", justify=LEFT, wraplength=300,
        #      text="Calculated probability of the population where the samples came " +
        #      "from has its mean equal to the hypothesized mean. When hypothesized " +
        #      "standard deviation given, Z-test will be performed, otherwise, " +
        #      "t-test will be performed.")
        #  w.pack(side=TOP, fill=BOTH, padx=2)
        f = tk.LabelFrame(m, text='Sample Values')
        f.pack(side=TOP, fill=BOTH, padx=2)
        self.xvar = tk.StringVar(value="")
        w = ttk.Combobox(
            f, values=self.cols, textvariable=self.xvar,
            width=14)
        w.pack(side=LEFT, padx=2)

        master = tk.LabelFrame(m, text='Summarized Data (Overriding)')
        master.pack(side=TOP, fill=BOTH, padx=2)
        self.sample_mean = tk.StringVar(value="")
        self.sample_std = tk.StringVar(value="")
        self.sample_n = tk.StringVar(value="")
        w = tk.Label(master, text="N")
        w.pack(side=LEFT, fill=X, padx=2)
        w = tk.Entry(master, textvariable=self.sample_n,
                     bg='white', width=5)
        w.pack(side=LEFT, padx=2, pady=2)
        w = tk.Label(master, text="Stdev")
        w.pack(side=LEFT, fill=X, padx=2)
        w = tk.Entry(master, textvariable=self.sample_std,
                     bg='white', width=5)
        w.pack(side=LEFT, padx=2, pady=2)
        w = tk.Label(master, text="Mean")
        w.pack(side=LEFT, fill=X, padx=2)
        w = tk.Entry(master, textvariable=self.sample_mean,
                     bg='white', width=5)
        w.pack(side=LEFT, padx=2, pady=2)

        master = tk.LabelFrame(m, text='Hypothesis Test')
        master.pack(side=TOP, fill=BOTH, padx=2)
        self.u0 = tk.StringVar(value="")
        w = tk.Label(master, text="Mean")
        w.pack(side=LEFT, fill=X, padx=2)
        w = tk.Entry(master, textvariable=self.u0,
                     bg='white', width=5)
        w.pack(side=LEFT, padx=2, pady=2)

        return

    def apply(self):
        if len(self.xvar.get()) > 0:
            x = number_list(self.df[self.xvar.get()],
                            col_name=self.xvar.get(),
                            print_out=True, print_port=self.app.print)
        else:
            x = None

        mean = get_number(self.sample_mean)
        std = get_number(self.sample_std)
        n = get_number(self.sample_n)
        u0 = get_number(self.u0)
        #  s0=get_number(self.s0)

        if mean is None or std is None or n is None:
            if x is None:
                return
            mean = std = n = None
        else:
            x = []
        if u0 is None:
            return
        t_test_1sample(x, u0, print_out=True,
                       sample_mean=mean, sample_n=n,
                       sample_std=std,
                       print_port=self.app.print)
        return


class Mean1SampleZDialog(Dialogs):
    def createWidgets(self, m):
        f = tk.LabelFrame(m, text='Sample Values')
        f.pack(side=TOP, fill=BOTH, padx=2)
        self.xvar = tk.StringVar(value="")
        w = ttk.Combobox(
            f, values=self.cols, textvariable=self.xvar,
            width=14)
        w.pack(side=LEFT, padx=2)

        master = tk.LabelFrame(m, text='Summarized Data (Overriding)')
        master.pack(side=TOP, fill=BOTH, padx=2)
        self.sample_mean = tk.StringVar(value="")
        self.sample_n = tk.StringVar(value="")
        w = tk.Label(master, text="N")
        w.pack(side=LEFT, fill=X, padx=2)
        w = tk.Entry(master, textvariable=self.sample_n,
                     bg='white', width=5)
        w.pack(side=LEFT, padx=2, pady=2)
        w = tk.Label(master, text="Mean")
        w.pack(side=LEFT, fill=X, padx=2)
        w = tk.Entry(master, textvariable=self.sample_mean,
                     bg='white', width=5)
        w.pack(side=LEFT, padx=2, pady=2)

        master = tk.LabelFrame(m, text='Hypothesis Test')
        master.pack(side=TOP, fill=BOTH, padx=2)
        self.u0 = tk.StringVar(value="")
        self.s0 = tk.StringVar(value="")
        w = tk.Label(master, text="Mean")
        w.pack(side=LEFT, fill=X, padx=2)
        w = tk.Entry(master, textvariable=self.u0,
                     bg='white', width=5)
        w.pack(side=LEFT, padx=2, pady=2)
        master = tk.LabelFrame(m, text='Known Value')
        master.pack(side=TOP, fill=BOTH, padx=2)
        w = tk.Label(master, text="Stdev")
        w.pack(side=LEFT, fill=X, padx=2)
        w = tk.Entry(master, textvariable=self.s0,
                     bg='white', width=5)
        w.pack(side=LEFT, padx=2, pady=2)

        return

    def apply(self):
        if len(self.xvar.get()) > 0:
            x = number_list(self.df[self.xvar.get()],
                            col_name=self.xvar.get(),
                            print_out=True, print_port=self.app.print)
        else:
            x = None

        mean = get_number(self.sample_mean)
        n = get_number(self.sample_n)
        u0 = get_number(self.u0)
        s0 = get_number(self.s0)

        if mean is None or n is None:
            if x is None:
                return
            mean = n = None
        else:
            x = []
        if u0 is None or s0 is None:
            return
        z_test_1sample(x, u0, s0, print_out=True,
                       sample_mean=mean, sample_n=n,
                       print_port=self.app.print)
        return
