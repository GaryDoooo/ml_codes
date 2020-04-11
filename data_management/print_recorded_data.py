import argparse
import pickle
import bz2
import pandas as pd
from statistics import mean, median, stdev


def read_data(filename):
    with bz2.BZ2File(filename) as pfile_handle:
        old_data = pickle.load(pfile_handle)
    return old_data


def dispatch(filename,
             ticker,
             timetable,
             stats,
             tickerlist,
             savecsv,
             head,
             tail
             ):
    df = read_data(filename)
    df = df.sort_index()
    df_cols = list(df.columns.values)
    if ticker != "no input":
        df_cols = [_ for _ in df_cols if ticker == _.split("_")[0]]
        # pick out all cols names with ticker str in it.
    if tickerlist != "no input":
        res = []
        tickers = pd.read_csv(tickerlist, sep=',')
        for ticker in tickers['Ticker']:
            res.extend([_ for _ in df_cols if ticker == _.split("_")[0]])
        df_cols = res
    df = df[df_cols]
    if head > 0:
        df = df.head(head)
    elif tail > 0:
        df = df.tail(tail)

    if timetable == "yes":
        cols = df_cols
        for col in cols:
            if ("_" in col) and (not "_ac" in col):
                pass
            else:
                df_ = df[col].copy()
                df_ = df_.dropna().sort_index()
                print(col.replace("_ac", ""),
                      df_.index[0], df_.index[-1], df_.shape[0])
    elif stats == "yes":
        for col in df_cols:
            df_ = df[col].copy()
            df_ = df_.dropna().sort_index()
            print("Ticker", col, "max %f min %f mean %f median %f std %f #of-1 %d" %
                  (max(df_), min(df_), mean(
                      df_), median(df_), stdev(df_), len(df_[df_ == -1]))
                  )
    elif savecsv != 'no input':
        if not ".csv" in savecsv:
            print("Please give a filename, like --savecsv=xxx.csv including csv.")
        else:
            df.to_csv(savecsv, sep=',')
    else:
        print(df.shape)
        print(df.head())
        print(df.tail())


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--filename',
                        type=str,
                        help='The p.bz2 database.')
    parser.add_argument('--ticker',
                        type=str,
                        default="no input",
                        help='to print a specific ticker data.')
    parser.add_argument('--timetable',
                        default="no",
                        type=str,
                        help='Print the time range of the ticker(s).')
    parser.add_argument('--stats',
                        default="no",
                        type=str,
                        help='Print data stat numbers of the ticker(s).')
    parser.add_argument('--tickerlist',
                        type=str,
                        default='no input',
                        help='to print a specified list of tickers, which is in a csv file under col=Ticker.')
    parser.add_argument('--savecsv',
                        type=str,
                        default='no input',
                        help='Put a csv filename here and save the selected part (if selected) into csv.')
    parser.add_argument('--head',
                        type=int,
                        default=0,
                        help='Crop the head X rows.')
    parser.add_argument('--tail',
                        type=int,
                        default=0,
                        help='Crop the tail X rows.')
    parse_args, unknown = parser.parse_known_args()
    dispatch(**parse_args.__dict__)
