from tkinter import Frame, Menu, BOTH, Toplevel, END
#  messagebox, simpledialog, PanedWindow, HORIZONTAL
from pandastable_local import config, plotting
#  from pandastable_local.core import Table
from pandastable_local.app import DataExplore
import pickle
import os
import platform
import time
######## Own Module ###########
from modified_table import MTable as Table
from plots import plot_viewer
#  from linear_plot import fit_plot
from txt_output import txt_viewer
from fit_dialog import LinearFitDialog, CorrelationDialog, OrthoFitDialog, ResidDialog, MCorDialog
from basic_dialogs import DescribeDialog, NormTestDialog, CIDialog
from sample_test_dialog import Mean1SampleDialog, Mean1SampleZDialog


class TestApp(DataExplore):
    """Basic test frame for the table"""

    def __init__(self, parent=None):
        self.parent = parent
        Frame.__init__(self)
        self.main = self.master
        self.main.geometry('600x400+50+100')
        self.main.title('Table app')

        # Get platform into a variable
        self.currplatform = platform.system()
        self.setConfigDir()
        if not hasattr(self, 'defaultsavedir'):
            self.defaultsavedir = os.path.join(os.path.expanduser('~'))
        self.loadAppOptions()
        # start logging
        self.start_logging()

        f = Frame(self.main)
        f.pack(fill=BOTH, expand=1)
        self.table = Table(f, showtoolbar=False, showstatusbar=True,
                           enable_menus=True)
        options = {'colheadercolor': 'green', 'floatprecision': 3,
                   'rowheaderfgcolor': 'black', 'rowheaderbgcolor': 'gray'}
        config.apply_options(options, self.table)
        self.table.show()
        self.createMenuBar()
        #  self.setupGUI()
        self.setStyles()
        self.clipboarddf = None
        self.projopen = False
        self.plots = dict()
        self.table.tOut = None

        #  self.newProject()
        self.main.protocol('WM_DELETE_WINDOW', self.quit)
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
                         '03Paste w/o header Ctrl-V': {'cmd': lambda: self._call('paste')},
                         '04Paste w/ header': {'cmd': lambda: self._call('paste_header')},
                         '13Find/Replace': {'cmd': self.findText},
                         '20sep': 'ddddd',
                         '24Preferences': {'cmd': self.currentTablePrefs}}
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

        self.data_menu = {
            '01Create Categorical': {'cmd': lambda: self._call('createCategorical')},
            '02Apply Function': {'cmd': lambda: self._call('applyColumnFunction')},
            '03Resample/Transform': {'cmd': lambda: self._call('applyTransformFunction')},
            '04Value Counts': {'cmd': lambda: self._call('valueCounts')},
            '05String Operation': {'cmd': lambda: self._call('applyStringMethod')},
            '06Date/Time Conversion': {'cmd': lambda: self._call('convertDates')},
            '22Filter Rows': {'cmd': lambda: self._call('queryBar')}}
        self.data_menu = self.createPulldown(self.menu, self.data_menu)
        self.menu.add_cascade(label='Data', menu=self.data_menu['var'])

        self.table_menu = {
            #  '01Describe Table': {'cmd': self.describe},
            '02Convert Column Names': {'cmd': lambda: self._call('convertColumnNames')},
            '03Convert Numeric': {'cmd': lambda: self._call('convertNumeric')},
            '04Clean Data': {'cmd': lambda: self._call('cleanData')},
            '05Find Duplicates': {'cmd': lambda: self._call('findDuplicates')},
            #  '06Correlation Matrix': {'cmd': lambda: self._call('corrMatrix')},
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

        self.stats_menu = {
            '01Describe': {'cmd': self.describe},
            '02Normality': {'cmd': self.norm_test},
            '03Confidence Intervals': {'cmd': self.confidence_interval},
            '13Correlation': {'cmd': self.correlation},
            '16Orthogonal Fit': {'cmd': self.ortho_fit},
            '14Linear Fit': {'cmd': self.linear_fit},
            '15Residual Plots': {'cmd': self.resid},
            '17Correlation Matrix': {'cmd': self.multi_cor},
            '22One Sample Mean t-test': {'cmd': self.mean_1sample},
            '23One Sample Mean Z-test': {'cmd': self.mean_1sampleZ},
            '06sep': '', '20sep': ''}
        self.stats_menu = self.createPulldown(self.menu, self.stats_menu)
        self.menu.add_cascade(label='Stats', menu=self.stats_menu['var'])

        self.plots_menu = {
            '01Plot Selected': {
                'cmd': lambda: self._call('plotSelected')}, '02sep': '', '03Store plot': {
                'cmd': self.addPlot}, '04Clear plots': {
                'cmd': self.updatePlotsMenu}, '05PDF report': {
                    'cmd': self.pdfReport}, '06sep': ''}
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

    def addPlot(self):
        """Store the current plot so it can be re-loaded"""

        #  name = self.getCurrentSheet()
        #  table = self.sheets[name]
        table = self.getCurrentTable()
        fig = table.pf.fig
        t = time.strftime("%H:%M:%S")
        label = t
        # dump and reload the figure to get a new object
        p = pickle.dumps(fig)
        fig = pickle.loads(p)
        self.plots[label] = fig

        def func(label):
            fig = self.plots[label]
            win = Toplevel()
            win.title(label)
            plotting.addFigure(win, fig)

        menu = self.plots_menu['var']
        menu.add_command(label=label, command=lambda: func(label))
        return

    def updatePlotsMenu(self, clear=True):
        """Clear stored plots"""

        if clear:
            self.plots = {}
        menu = self.plots_menu['var']
        menu.delete(6, menu.index(END))
        return

    def showPlotViewer(self, parent=None):
        """Create plot frame"""

        if hasattr(self.table, 'pf') and self.table.pf is not None:
            self.addPlot()
            self.table.pf.close()

        self.table.pf = plot_viewer(table=self.table, parent=parent)
        if hasattr(self.table, 'child') and self.table.child is not None:
            self.table.child.pf = self.table.pf
        return self.table.pf

    def print(self, txt, end="\n"):
        if self.table.tOut is None:
            self.tOut = txt_viewer(table=self.table)
        self.tOut.add_txt(txt + end)
        return

    def linear_fit(self):

        _ = LinearFitDialog(
            self.table, app=self,
            df=self.table.model.df,
            title='Linear Fit')
        return

    def correlation(self):

        _ = CorrelationDialog(
            self.table, app=self,
            df=self.table.model.df,
            title='Correlation')
        return

    def ortho_fit(self):

        _ = OrthoFitDialog(
            self.table, app=self,
            df=self.table.model.df,
            title='Orthogonal Fit')
        return

    def describe(self):
        _ = DescribeDialog(
            self.table, app=self,
            df=self.table.model.df,
            title='Stats Summary')
        return

    def norm_test(self):
        _ = NormTestDialog(
            self.table, app=self,
            df=self.table.model.df,
            title='Normality Test')
        return

    def resid(self):
        _ = ResidDialog(
            self.table, app=self,
            df=self.table.model.df,
            title='Residual Plots')
        return

    def confidence_interval(self):
        _ = CIDialog(
            self.table, app=self,
            df=self.table.model.df,
            title='Confidence Intervals')
        return

    def multi_cor(self):
        _ = MCorDialog(
            self.table, app=self,
            df=self.table.model.df,
            title='Multi Column Correlation')
        return

    def mean_1sample(self):
        _ = Mean1SampleDialog(
            self.table, app=self,
            df=self.table.model.df,
            title='One sample t-test')
        return

    def mean_1sampleZ(self):
        _ = Mean1SampleZDialog(
            self.table, app=self,
            df=self.table.model.df,
            title='One sample Z-test')
        return


if __name__ == "__main__":
    app = TestApp()
    # launch the app
    app.mainloop()
