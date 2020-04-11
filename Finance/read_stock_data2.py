import datetime as dt
#  import matplotlib.pyplot as plt
# from matplotlib import style
#  import pandas as pd
import pandas_datareader.data as web
import pickle
import bz2
import os.path
#  style.use("ggplot")


def read_stock(stock_name, start, end):
    if not os.path.isfile(stock_name + ".p.bz2"):
        print "=========", stock_name, "=========="
        df = web.DataReader(stock_name, "yahoo", start, end)
        print df.head()

        with bz2.BZ2File(stock_name + ".p.bz2", "w") as pfile:
            pickle.dump(df, pfile,
                        protocol=pickle.HIGHEST_PROTOCOL)


def main():
    start = dt.datetime(1970, 1, 1)
    end = dt.datetime(2017, 9, 29)

    nasdaq100list = pickle.load(
        open("/home/du/coding/Finance/nasdaq100list.p", "rb"))
    sp500list = pickle.load(open("/home/du/coding/Finance/sp500list.p", "rb"))
    total_list = nasdaq100list + sp500list

    for ticker in total_list:
        read_stock(ticker, start, end)


if __name__ == "__main__":
    main()
