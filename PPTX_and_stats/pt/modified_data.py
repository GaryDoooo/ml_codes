##################
from pandastable_local.data_orig import TableModel as TM


class TableModel(TM):
    def deleteColumns(self, cols=None):
        """Remove all cols or list provided"""

        df = self.df
        colnames = df.columns[cols]
        df.drop(colnames, axis=1, inplace=True)
        return

    #  def addColumn(self, colname=None, dtype=None, data=None):
    #      """Add a column"""
    #
    #      if data is None:
    #          data = [""] * self.df.shape[0]
    #          #  data = pd.Series(dtype=dtype)
    #
    #      self.df[colname] = data
    #      return
