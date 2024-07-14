import pandas as pd
from tkinter import END, StringVar, Entry
import numpy as np
############ pandastable #############
from pandastable_local.core import Table
from pandastable_local.data import TableModel
#  from pandastable_local.headers import IndexHeader,
from pandastable_local.dialogs import MultipleValDialog
############## Own Module ###############
#  from modified_header import MColumnHeader as ColumnHeader
#  from modified_header import RowHeader
from df_combine import df_combine


class MTable(Table):
    def sortColumnIndex(self):
        """Sort the column header by the current rows values"""

        cols = self.model.df.columns
        # get only sortable cols
        # temp = self.model.df._convert(convert_numeric=True) **** depreciated
        # ****
        temp = self.model.df.apply(pd.to_numeric, errors='ignore')
        temp = temp.select_dtypes(include=['int', 'float'])
        rowindex = temp.index[self.currentrow]
        #  row = temp.ix[rowindex] **** depreciated ****
        row = temp.iloc[rowindex]
        # add unsortable cols to end of new ordered ones
        newcols = list(temp.columns[row.argsort()])
        a = list(set(cols) - set(newcols))
        newcols.extend(a)
        self.model.df = self.model.df.reindex(columns=newcols)
        self.redraw()
        return

    def update_rowcolors(self):
        """Update row colors if present so that it syncs with current dataframe."""

        df = self.model.df
        rc = self.rowcolors
        if len(df) == len(self.rowcolors):
            rc.set_index(df.index, inplace=True)
        elif len(df) > len(rc):
            idx = df.index.difference(rc.index)
            #self.rowcolors = rc.append(pd.DataFrame(index=idx))
            self.rowcolors = pd.concat([rc, pd.DataFrame(index=idx)])
        else:
            idx = rc.index.difference(df.index)
            rc.drop(idx, inplace=True)
        # check columns
        cols = list(rc.columns.difference(df.columns))
        print(cols)
        if len(cols) > 0:
            try:
                rc.drop(cols, inplace=True)
            except BaseException:
                pass
        cols = list(df.columns.difference(rc.columns))
        if len(cols) > 0:
            for col in cols:
                rc[col] = np.nan
        return

    def setAlignment(self, colnames=None):
        """Set column alignments, overrides global value"""

        cols = self.multiplecollist
        df = self.model.df
        cf = self.columnformats
        cfa = cf['alignment']
        vals = ['Left', 'Right', 'Center']
        conv = {"Left": 'w', "Right": 'e', "Center": 'center'}
        d = MultipleValDialog(title='set alignment',
                              initialvalues=[vals],
                              labels=['Align:'],
                              types=['combobox'],
                              parent=self.parentframe)
        if d.result is None:
            return
        aln = conv[d.results[0]]
        #  print(aln)
        for col in cols:
            colname = df.columns[col]
            cfa[colname] = aln
        self.redraw()
        return

    def handle_right_click(self, event):
        return

    def drawCellEntry(self, row, col, text=None):
        """When the user single/double clicks on a text/number cell,
          bring up entry window and allow edits."""

        def select_all(event):
            event.widget.select_range(0, END)
            return 'break'

        if not self.editable:
            return
        h = self.rowheight
        #  model = self.model
        text = self.model.getValueAt(row, col)
        if pd.isnull(text):
            text = ''
        x1, y1, x2, y2 = self.getCellCoords(row, col)
        w = x2 - x1
        self.cellentryvar = txtvar = StringVar()
        txtvar.set(text)

        self.cellentry = Entry(self.parentframe, width=20,
                               textvariable=txtvar,
                               takefocus=1,
                               font=self.thefont)
        self.cellentry.icursor(END)
        self.cellentry.bind(
            '<Return>',
            lambda x: self.handleCellEntry(
                row,
                col))
        self.cellentry.bind("<FocusIn>", select_all)
        self.cellentry.bind("<Tab>",
                            lambda x: self.handleCellEntry(
                                row,
                                col, nxt_col=True))
        self.cellentry.focus_set()
        self.entrywin = self.create_window(x1, y1,
                                           width=w, height=h,
                                           window=self.cellentry, anchor='nw',
                                           tag='entry')
        return

    def handleCellEntry(self, row, col, nxt_col=False):
        """Callback for cell entry"""

        value = self.cellentryvar.get()
        if self.filtered == 1:
            df = self.dataframe
        else:
            df = None
        self.model.setValueAt(value, row, col, df=df)

        self.drawText(row, col, value, align=self.align)
        self.delete('entry')
        self.gotonextCell(nxt_col=nxt_col)
        return

    def gotonextCell(self, nxt_col=False):
        """Move highlighted cell to next cell in row after enter cell entry"""

        if hasattr(self, 'cellentry'):
            self.cellentry.destroy()
        if nxt_col:
            self.currentcol += 1
        else:
            self.currentrow = self.currentrow + 1
        #  self.drawSelectedRect(self.currentrow, self.currentcol)
        self.drawCellEntry(self.currentrow, self.currentcol)
        return

    def handle_double_click(self, event):
        """Do double click stuff. Selected row/cols will already have
           been set with single click binding"""

        row = self.get_row_clicked(event)
        col = self.get_col_clicked(event)
        print(row, col, self.currentrow, self.currentcol)
        self.drawCellEntry(self.currentrow, self.currentcol)
        return

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

        try:
            ins_y = min(self.multiplerowlist)
            ins_x = min(self.multiplecollist)
        except BaseException:
            ins_y = ins_x = 0
        model = TableModel(df_combine(
            self.model.df, df,
            ins_y=ins_y, ins_x=ins_x))
        self.updateModel(model)
        self.redraw()
        return

    def paste_header(self, event=None):
        """Paste a new table from the clipboard"""

        self.storeCurrent()
        try:
            df = pd.read_clipboard(sep=',', on_bad_lines='skip')
        except BaseException:
            print("Can't paste.")
            return
        if len(df) == 0:
            return

        try:
            ins_x = min(self.multiplecollist)
        except BaseException:
            ins_x = 0
        new_df = df_combine(
            self.model.df, df,
            ins_y=0,  # min(self.multiplerowlist),
            ins_x=ins_x)
        col_names = new_df.columns.tolist()
        df2_cols = df.columns.tolist()
        for x in range(len(df2_cols)):
            xx = ins_x + x
            col_names[xx] = df2_cols[x]
        new_df.columns = col_names
        model = TableModel(new_df)
        self.updateModel(model)
        self.redraw()
        return
