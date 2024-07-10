from tkinter import *
from pandastable import config
from pandastable.core import Table
from pandastable.app import DataExplore
import os
import platform


class TestApp(DataExplore):
    """Basic test frame for the table"""

    def __init__(self, parent=None):
        self.parent = parent
        Frame.__init__(self)
        self.main = self.master
        self.main.geometry('600x400+200+100')
        self.main.title('Table app')

        # Get platform into a variable
        self.currplatform = platform.system()
        self.setConfigDir()
        # if not hasattr(self,'defaultsavedir'):
        self.defaultsavedir = os.path.join(os.path.expanduser('~'))
        self.loadAppOptions()
        # start logging
        self.start_logging()

        self.createMenuBar()
        #  self.setupGUI()
        self.clipboarddf = None
        self.projopen = False
        f = Frame(self.main)
        f.pack(fill=BOTH, expand=1)
        #  df = TableModel.getSampleData()
        self.table = pt = Table(f,
                                #  dataframe=df,
                                showtoolbar=False, showstatusbar=True)
        #  #  pt.show()
        #  #  # set some options
        options = {'colheadercolor': 'green', 'floatprecision': 5}
        config.apply_options(options, pt)
        pt.show()
        return


app = TestApp()
# launch the app
app.mainloop()
