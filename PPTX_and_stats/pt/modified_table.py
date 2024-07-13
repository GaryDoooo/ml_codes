import pandas as pd
from tkinter import VERTICAL, HORIZONTAL
############ pandastable #############
from pandastable_local.core import Table, ToolBar, statusBar
from pandastable_local.data import TableModel
from pandastable_local.headers import RowHeader, IndexHeader
from pandastable_local.dialogs import AutoScrollbar
############## Own Module ###############
from modified_header import MColumnHeader as ColumnHeader


class MTable(Table):
    def paste(self, event=None):
        """Paste a new table from the clipboard"""

        self.storeCurrent()
        try:
            df = pd.read_clipboard(sep=',', on_bad_lines='skip', header=None)
        except BaseException:
            #  messagebox.showwarning("Could not read data", e,
            #                          parent=self.parentframe)
            print("Can't paste.")
            return
        if len(df) == 0:
            return
        print(self.multiplerowlist, self.multiplecollist)
        print(df)
        #  df = pd.read_clipboard(sep=',', on_bad_lines='skip')
        model = TableModel(df)
        #  self.updateModel(model)
        #  self.redraw()
        return model

    def handle_double_click(self, event):
        """Do double click stuff. Selected row/cols will already have
           been set with single click binding"""

        row = self.get_row_clicked(event)
        col = self.get_col_clicked(event)
        print(row, col, self.currentrow, self.currentcol)
        self.drawCellEntry(self.currentrow, self.currentcol)
        return

    def show(self, callback=None):
        """Adds column header and scrollbars and combines them with
           the current table adding all to the master frame provided in constructor.
           Table is then redrawn."""

        # Add the table and header to the frame
        self.rowheader = RowHeader(
            self.parentframe,
            self)
        #  fgcolor=self.rowheaderfgcolor,
        #  bgcolor=self.rowheaderbgcolor)
        self.colheader = ColumnHeader(
            self.parentframe,
            self)
        #  fgcolor=self.colheaderfgcolor,
        #  bgcolor=self.colheaderbgcolor)
        self.rowindexheader = IndexHeader(
            self.parentframe, self, bg=self.rowheaderbgcolor)
        self.Yscrollbar = AutoScrollbar(
            self.parentframe,
            orient=VERTICAL,
            command=self.set_yviews)
        self.Yscrollbar.grid(
            row=1,
            column=2,
            rowspan=1,
            sticky='news',
            pady=0,
            ipady=0)
        self.Xscrollbar = AutoScrollbar(
            self.parentframe,
            orient=HORIZONTAL,
            command=self.set_xviews)
        self.Xscrollbar.grid(row=2, column=1, columnspan=1, sticky='news')
        self['xscrollcommand'] = self.Xscrollbar.set
        self['yscrollcommand'] = self.Yscrollbar.set
        self.colheader['xscrollcommand'] = self.Xscrollbar.set
        self.rowheader['yscrollcommand'] = self.Yscrollbar.set
        self.parentframe.rowconfigure(1, weight=1)
        self.parentframe.columnconfigure(1, weight=1)

        self.rowindexheader.grid(row=0, column=0, rowspan=1, sticky='news')
        self.colheader.grid(row=0, column=1, rowspan=1, sticky='news')
        self.rowheader.grid(row=1, column=0, rowspan=1, sticky='news')
        self.grid(row=1, column=1, rowspan=1, sticky='news', pady=0, ipady=0)

        self.adjustColumnWidths()
        # bind redraw to resize, may trigger redraws when widgets added
        # self.redrawVisible)
        self.parentframe.bind("<Configure>", self.resized)
        self.colheader.xview("moveto", 0)
        self.xview("moveto", 0)
        if self.showtoolbar:
            self.toolbar = ToolBar(self.parentframe, self)
            self.toolbar.grid(row=0, column=3, rowspan=2, sticky='news')
        if self.showstatusbar:
            self.statusbar = statusBar(self.parentframe, self)
            self.statusbar.grid(row=3, column=0, columnspan=2, sticky='ew')
        # self.redraw(callback=callback)
        self.currwidth = self.parentframe.winfo_width()
        self.currheight = self.parentframe.winfo_height()
        if hasattr(self, 'pf'):
            self.pf.updateData()
        return
