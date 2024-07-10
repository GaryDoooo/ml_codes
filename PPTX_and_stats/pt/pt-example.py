from tkinter import Frame, Menu, BOTH
#  messagebox, simpledialog, PanedWindow, HORIZONTAL
from pandastable_local import config
from pandastable_local.core import Table
from pandastable_local.app import DataExplore
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

        #  self.setupGUI()
        f = Frame(self.main)
        f.pack(fill=BOTH, expand=1)
        #  #  df = TableModel.getSampleData()
        self.table = pt = Table(f, showtoolbar=False, showstatusbar=True)
        options = {'colheadercolor': 'green', 'floatprecision': 5}
        config.apply_options(options, pt)
        pt.show()
        self.createMenuBar()
        #  self.setupGUI()
        #  self.setStyles()
        self.clipboarddf = None
        self.projopen = False

        #  self.newProject()
        #  self.main.protocol('WM_DELETE_WINDOW', self.quit)
        self.main.lift()
        return

    def createMenuBar(self):
        """Create the menu bar for the application. """

        self.menu = Menu(self.main)
        file_menu = Menu(self.menu, tearoff=0)
        # add recent first
        #  self.createRecentMenu(file_menu)
        filemenuitems = {'01New Project': {'cmd': lambda: self._call('new')},
                         '02Open Project': {'cmd': lambda: self._call('load')},
                         #  '03Close': {'cmd': self.closeProject},
                         '04Save': {'cmd': lambda: self._call('save')},
                         '05Save As': {'cmd': lambda: self._call('saveAs')},
                         '06sep': '',
                         '07Import CSV': {'cmd': lambda: self._call('importCSV')},
                         #  '08Import HDF5': {'cmd': self.importHDF},
                         #  '09Import from URL': {'cmd': self.importURL},
                         '10Import Excel': {'cmd': lambda: self._call('loadExcel')},
                         '10Export CSV': {'cmd': lambda: self._call('doExport')},
                         '11sep': '',
                         '12Quit': {'cmd': self.quit}}

        self.file_menu = self.createPulldown(
            self.menu, filemenuitems, var=file_menu)
        self.menu.add_cascade(label='File', menu=self.file_menu['var'])

        editmenuitems = {'01Undo Last Change': {'cmd': self.undo},
                         '02Copy Table': {'cmd': self.copyTable},
                         '03Find/Replace': {'cmd': self.findText},
                         '04Preferences': {'cmd': self.currentTablePrefs}
                         }
        self.edit_menu = self.createPulldown(self.menu, editmenuitems)
        self.menu.add_cascade(label='Edit', menu=self.edit_menu['var'])

        self.view_menu = {
            '01Zoom In': {
                'cmd': lambda: self._call('zoomIn')}, '02Zoom Out': {
                'cmd': lambda: self._call('zoomOut')}, '03Wrap Columns': {
                'cmd': lambda: self._call('setWrap')}, '04sep': '', '05Dark Theme': {
                    'cmd': lambda: self._call(
                        'setTheme', name='dark')}, '06Bold Theme': {
                            'cmd': lambda: self._call(
                                'setTheme', name='bold')}, '07Default Theme': {
                                    'cmd': lambda: self._call(
                                        'setTheme', name='default')}, }
        self.view_menu = self.createPulldown(self.menu, self.view_menu)
        self.menu.add_cascade(label='View', menu=self.view_menu['var'])

        self.table_menu = {'01Describe Table': {'cmd': self.describe},
                           '02Convert Column Names': {'cmd': lambda: self._call('convertColumnNames')},
                           '03Convert Numeric': {'cmd': lambda: self._call('convertNumeric')},
                           '04Clean Data': {'cmd': lambda: self._call('cleanData')},
                           '05Find Duplicates': {'cmd': lambda: self._call('findDuplicates')},
                           '06Correlation Matrix': {'cmd': lambda: self._call('corrMatrix')},
                           #  '07Concatenate Tables': {'cmd': self.concat},
                           '08Table to Text': {'cmd': lambda: self._call('showasText')},
                           '09Table Info': {'cmd': lambda: self._call('showInfo')},
                           '10sep': '',
                           '11Transform Values': {'cmd': lambda: self._call('transform')},
                           '12Group-Aggregate': {'cmd': lambda: self._call('aggregate')},
                           '13Cross Tabulation': {'cmd': lambda: self._call('crosstab')},
                           '14Merge/Concat Tables': {'cmd': lambda: self._call('doCombine')},
                           '15Pivot Table': {'cmd': lambda: self._call('pivot')},
                           '16Melt Table': {'cmd': lambda: self._call('melt')},
                           '17Time Series Resampling': {'cmd': lambda: self._call('resample')}
                           }
        self.table_menu = self.createPulldown(self.menu, self.table_menu)
        self.menu.add_cascade(label='Tools', menu=self.table_menu['var'])

        self.plots_menu = {'01Store plot': {'cmd': self.addPlot},
                           '02Clear plots': {'cmd': self.updatePlotsMenu},
                           '03PDF report': {'cmd': self.pdfReport},
                           '04sep': ''}
        self.plots_menu = self.createPulldown(self.menu, self.plots_menu)
        self.menu.add_cascade(label='Plots', menu=self.plots_menu['var'])

        self.help_menu = {'01Online Help': {'cmd': self.online_documentation},
                          '02View Error Log': {'cmd': self.showErrorLog},
                          '03About': {'cmd': self.about}}
        self.help_menu = self.createPulldown(self.menu, self.help_menu)
        self.menu.add_cascade(label='Help', menu=self.help_menu['var'])

        self.main.config(menu=self.menu)
        return

    def getCurrentTable(self):
        return self.table


app = TestApp()
# launch the app
app.mainloop()
