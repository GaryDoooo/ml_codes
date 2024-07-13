from pandastable_local.plotting import addButton
from pandastable_local import images
#  from tkinter.ttk import Frame
from tkinter import BOTH, Toplevel, VERTICAL, LEFT, Frame, Text, TOP, END, BOTTOM, filedialog
import os
#  from idlelib.WidgetRedirector import WidgetRedirector
#  from collections import OrderedDict
############# Own Modules ###########
from plots import plot_viewer

#
#  class ReadOnlyText(Text):
#      def __init__(self, *args, **kwargs):
#          Text.__init__(self, *args, **kwargs)
#          self.redirector = WidgetRedirector(self)
#          self.insert = self.redirector.register(
#              "insert", lambda *args, **kw: "break")
#          self.delete = self.redirector.register(
#              "delete", lambda *args, **kw: "break")
#
#


class txt_viewer(plot_viewer):
    def __init__(self, table, parent=None):

        self.parent = parent
        self.table = table
        if table is not None:
            self.table.tOut = self  # opaque ref

        if self.parent is not None:
            Frame.__init__(self, parent)
            self.main = self.master
        else:
            self.main = Toplevel()
            self.master = self.main
            self.main.title('Output')
            self.main.protocol("WM_DELETE_WINDOW", self.close)
            g = '400x700'
            self.main.geometry(g)
        self.orient = VERTICAL
        self.style = None
        self.setupGUI()
        self.currentdir = os.path.expanduser('~')
        return

    def setupGUI(self):
        """Add GUI elements"""

        self.m = Frame(self.main)
        self.m.pack(fill=BOTH, expand=1)
        self.plotfr = Frame(self.m)
        self.T = Text(self.plotfr, bg='white')
        self.T.pack(fill=BOTH, expand=1)
        #  self.T.bind("<Key>", lambda e: "break")
        #  self.T.config(state='disabled')
        self.plotfr.pack(side=TOP, fill=BOTH, expand=1)

        # frame for controls
        self.ctrlfr = Frame(self.main)
        self.ctrlfr.pack(side=BOTTOM, fill=BOTH)

        # button frame
        bf = Frame(self.ctrlfr, padx=2)  # padding=2)
        bf.pack(side=TOP, fill=BOTH)
        side = LEFT
        addButton(bf, 'Clear', self.clear, images.plot_clear(),
                  'clear content', side=side)
        addButton(bf, 'Save', self.save, images.save(),
                  'save content', side=side)

        return

    def add_txt(self, txt):
        #  text.configure(state='normal')
        #  text.insert('end', 'Some Text')
        #  text.configure(state='disabled')
        #  self.T.config(state='normal')
        self.T.insert(END, txt)
        #  self.T.config(state='disabled')
        return

    def save(self, filename=None):
        """Save the current plot"""

        ftypes = [('txt', '*.txt')]
        if filename is None:
            filename = filedialog.asksaveasfilename(parent=self.master,
                                                    initialdir=self.currentdir,
                                                    filetypes=ftypes)
        if filename:
            self.currentdir = os.path.dirname(os.path.abspath(filename))
            try:
                with open(filename, 'w') as file:
                    text_content = self.T.get("1.0", "end-1c")
                    file.write(text_content)
            except BaseException:
                print("write file", filename, "error")
        return

    def clear(self):
        #  self.T.config(state=ENABLED)
        self.T.delete('1.0', END)
        #  self.T.config(state=DISABLED)
        return

    def close(self):
        print('txt win close')
        try:
            self.table.tOut = None
        except BaseException:
            pass
        self.main.destroy()
        return
