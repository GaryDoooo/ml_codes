import os.path
import bz2
import pickle
# import math
import numpy as np


class verify_data:
    def __init__(self, stock_name):
        self.openfile(stock_name)
        self.checknan()
        self.checkzero()

    def checkzero(self):
        self.total_zeros_in_volume = np.sum(
            1 * self.df['Volume'].as_matrix() == 0)
        self.total_zeros_in_ohlc = np.sum(
            1 * self.df[['Open', 'High', 'Low', 'Close', 'Adj Close']].as_matrix() == 0)

    def checknan(self):
        #  not_a_number = float('nan')
        self.not_a_number_total = np.sum(1 * np.isnan(self.df.as_matrix()))
        #  1 * (self.df.as_matrix() == not_a_number))

    def openfile(self, stock_name):
        if not os.path.isfile(stock_name + ".p.bz2"):
            # print stock_name, "is not exist."
            self.file_not_exist = True
        else:
            self.file_not_exist = False
            with bz2.BZ2File(stock_name + ".p.bz2") as pfile_handle:
                self.df = pickle.load(pfile_handle)


def main():
    nasdaq100list = pickle.load(open("nasdaq100list.p", "rb"))
    sp500list = pickle.load(open("sp500list.p", "rb"))
    total_list = nasdaq100list + sp500list
    good_data = 0
    good_tickers_list = []
    for ticker in total_list:
        result = verify_data("data/" + ticker)
        print ticker + ":",
        if result.file_not_exist:
            print "file not exist."
        else:
            if (result.not_a_number_total > 0):
                print "Total NaN", result.not_a_number_total,
            if (result.total_zeros_in_ohlc > 0):
                print "zero in OHLC", result.total_zeros_in_ohlc,
            if (result.total_zeros_in_volume > 0):
                print "zero in Vol", result.total_zeros_in_volume
            elif (result.not_a_number_total == 0)and(result.total_zeros_in_ohlc == 0):
                good_data += 1
                print "data are GOOD."
                good_tickers_list += [ticker]
            else:
                print "."

    print "Total good sets:", good_data
    print good_tickers_list
    pickle.dump(good_tickers_list, open(
        "Tickers_with_good_data.p", "wb"), protocol=0)


if __name__ == "__main__":
    main()
