import argparse
import pandas as pd
from gdu_modules import read_data, write_data_to_pbz


def dispatch(filename,
             ticker,
             tickerlist
             ):
    df = read_data(filename)
    df = df.sort_index()
    df_cols = list(df.columns.values)
    if ticker != "no input":
        df_cols = [_ for _ in df_cols if ticker == _.split("_")[0]]
        # pick out all cols names with ticker str in it.
    elif tickerlist != "no input":
        res = []
        tickers = pd.read_csv(tickerlist, sep=',')
        for ticker in tickers['Ticker']:
            res.extend([_ for _ in df_cols if ticker == _.split("_")[0]])
        df_cols = res

    # df_cols are the cols appeared in the input, which should be removed
    write_data_to_pbz(df.drop(df_cols, axis=1), filename)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--filename',
                        type=str,
                        help='The p.bz2 database.')
    parser.add_argument('--ticker',
                        type=str,
                        default="no input",
                        help='to print a specific ticker data.')
    parser.add_argument('--tickerlist',
                        type=str,
                        default='no input',
                        help='to print a specified list of tickers, which is in a csv file under col=Ticker.')
    parse_args, unknown = parser.parse_known_args()
    dispatch(**parse_args.__dict__)
