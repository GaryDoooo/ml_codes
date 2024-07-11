from pandastable_local.plotting import PlotViewer, addFigure, addButton
from pandastable_local import handlers, images
#  from tkinter.ttk import Frame
from tkinter import BOTH, Toplevel, VERTICAL, TOP, BOTTOM, LEFT, BooleanVar, Checkbutton, IntVar, Label, X, Entry, Frame
import os
from collections import OrderedDict


class plot_viewer(PlotViewer):
    def __init__(self, table, parent=None, showoptions=True):

        self.parent = parent
        self.table = table
        if table is not None:
            self.table.pf = self  # opaque ref
        #self.mode = '2d'
        self.showoptions = showoptions
        self.multiviews = False
        if self.parent is not None:
            Frame.__init__(self, parent)
            self.main = self.master
        else:
            self.main = Toplevel()
            self.master = self.main
            self.main.title('Plot Viewer')
            self.main.protocol("WM_DELETE_WINDOW", self.close)
            g = '800x700+290+0'
            self.main.geometry(g)
        #self.toolslayout = layout
        # if layout == 'horizontal':
        self.orient = VERTICAL
        # else:
        #    self.orient = HORIZONTAL
        #  self.mplopts = MPLBaseOptions(parent=self)
        #  self.mplopts3d = MPL3DOptions(parent=self)
        #  self.labelopts = AnnotationOptions(parent=self)
        #  self.layoutopts = PlotLayoutOptions(parent=self)
        #
        #  self.gridaxes = {}
        # reset style if it been set globally
        self.style = None
        self.setupGUI()
        #  self.updateStyle()
        self.currentdir = os.path.expanduser('~')
        return

    def setupGUI(self):
        """Add GUI elements"""

        #import tkinter as tk
        #self.m = PanedWindow(self.main, orient=self.orient)
        self.m = Frame(self.main)
        self.m.pack(fill=BOTH, expand=1)
        # frame for figure
        self.plotfr = Frame(self.m)
        # add it to the panedwindow
        self.fig, self.canvas = addFigure(self.plotfr)
        #  self.ax = self.fig.add_subplot(111)

        #self.m.add(self.plotfr, weight=12)
        self.plotfr.pack(side=TOP, fill=BOTH, expand=1)

        # frame for controls
        self.ctrlfr = Frame(self.main)
        #self.m.add(self.ctrlfr, weight=4)
        self.ctrlfr.pack(side=BOTTOM, fill=BOTH)

        # button frame
        bf = Frame(self.ctrlfr, padx=2)  # padding=2)
        bf.pack(side=TOP, fill=BOTH)

        side = LEFT
        # add button toolbar
        #  addButton(bf, 'Plot', self.replot, images.plot(),
        #            'plot current data', side=side, compound="left", width=16)
        #  addButton(bf, 'Apply Options', self.updatePlot, images.refresh(),
        #            'refresh plot with current options', side=side,
        #             width=20)
        #  addButton(bf, 'Zoom Out', lambda: self.zoom(False), images.zoom_out(),
        #            'zoom out', side=side)
        #  addButton(bf, 'Zoom In', self.zoom, images.zoom_in(),
        #            'zoom in', side=side)
        #  addButton(bf, 'Clear', self.clear, images.plot_clear(),
        #            'clear plot', side=side)
        addButton(bf, 'Save', self.savePlot, images.save(),
                  'save plot', side=side)

        # dicts to store global options, can be saved with projects
        self.globalvars = {}
        self.globalopts = OrderedDict({'dpi': 80})
        # , 'grid layout': False, '3D plot': False})
        from functools import partial
        for n in self.globalopts:
            val = self.globalopts[n]
            if isinstance(val, bool):
                v = self.globalvars[n] = BooleanVar()
                v.set(val)
                b = Checkbutton(
                    bf, text=n, variable=v, command=partial(
                        self.setGlobalOption, n))
            else:
                v = self.globalvars[n] = IntVar()
                v.set(val)
                Label(bf, text=n).pack(side=LEFT, fill=X, padx=2)
                b = Entry(bf, textvariable=v, width=5)
                v.trace("w", partial(self.setGlobalOption, n))
            b.pack(side=LEFT, padx=2)
        #  addButton(bf, 'Hide', self.toggle_options, images.prefs(),
        #            'show/hide plot options', side=RIGHT)
        #  self.addWidgets()

        # def onpick(event):
        #    print(event)
        #self.fig.canvas.mpl_connect('pick_event', onpick)
        #self.fig.canvas.mpl_connect('button_release_event', onpick)
        dr = handlers.DragHandler(self)
        dr.connect()
        return

    def close(self):
        """Close the window"""
        print('plot close')
        try:
            self.table.pf = None
            self.animateopts.stop()
        except BaseException:
            pass
        self.main.destroy()
        return
