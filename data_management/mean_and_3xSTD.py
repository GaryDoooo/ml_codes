import argparse
import pandas as pd
from statistics import mean, stdev
from gdu_modules import read_data, merge_df


def dispatch(avfilename,
             ticker,
             fredfilename,
             tickerlist
             ):

    df_av = read_data(avfilename)
    df_fred = read_data(fredfilename)
    df = merge_df(df_av, df_fred)

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

    print("### Print out all the columns in the ticker list with mean and 3xstd. ###")
    for col in df_cols:
        df_ = df[col].copy()
        df_ = df_.dropna().sort_index()
        print("%s,%f,%f" % (col, mean(
            df_), 3 * stdev(df_))
        )


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--avfilename',
                        type=str,
                        default='av_data',
                        help='The p.bz2 database of AV.')
    parser.add_argument('--ticker',
                        type=str,
                        default="no input",
                        help='to print a specific ticker data.')
    parser.add_argument('--fredfilename',
                        default="fred_data",
                        type=str,
                        help='The p.bz2 database of fred.')
    parser.add_argument('--tickerlist',
                        type=str,
                        default='no input',
                        help='to print a specified list of tickers, which is in a csv file under col=Ticker.')
    parse_args, unknown = parser.parse_known_args()
    dispatch(**parse_args.__dict__)
