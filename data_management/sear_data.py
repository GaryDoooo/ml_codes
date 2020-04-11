from gdu_modules import read_data, write_data_to_pbz, init_log, print_log
import pandas as pd
import numpy as np


def set_to_one_neg_one_range(col, df, zero, one):
    print_log("set10 %s %f %f" % (col, zero, one))
    df[col] = df[col].apply(lambda _: (_ - zero) / one)
    return df


def set_day_by_day_change(col, df,
                          set_neg_one_to_zero=False):
    data = df[col]
    neg_one = data == -1
    data[neg_one] = np.nan
    today = data.dropna()  # no -1 and initial nan
    yesterday = today.shift(1)
    change = (today - yesterday) / yesterday
    change[0] = 0
    df[col] = change
    if set_neg_one_to_zero:
        df[col][neg_one] = 0
    return df


def sear_by_cols(df, set_range_tickers_list):
    cols = list(df.columns)
    print(cols)
    print(set_range_tickers_list['Tickers'])
    vix_ticker_list = list(set_range_tickers_list['Tickers'])
    df = df.sort_index()
    for col in cols:
        ticker = col.split("_")[0]
        if "rsi" in col:
            df = set_to_one_neg_one_range(col, df, zero=50, one=50)
            print_log("RSI processed %s" % col)
        elif col == ticker:  # if the col is close adj
            if col in vix_ticker_list:
                df = set_to_one_neg_one_range(col, df,
                                              zero=set_range_tickers_list[set_range_tickers_list['Tickers']
                                                                          == col]['mean'],
                                              one=set_range_tickers_list[set_range_tickers_list['Tickers']
                                                                         == col]['3std'])
                print_log("Ticker in list found and processed: %s" % col)
            else:
                df = set_day_by_day_change(col, df)
        elif "vol" in col:
            if ticker in vix_ticker_list:
                df[col] = 0
            else:
                df = set_day_by_day_change(col, df)
    return df


def sear_data(
        set_range_tickers_csv="set_one_and_zero.csv",
        av_data_file="av_cooked",
        fred_data_file="fred_cooked",
        av_output="av_seared",
        fred_output="fred_seared"):
    # Take the file contents out and feed into the next level
        # The set range tickers should be the one output from mean and 3xstd.py,
        # and has the first line as the col names = Tickers,mean,3std
    init_log()
    set_range_tickers_list = pd.read_csv(set_range_tickers_csv, sep=",")
    df = read_data(av_data_file)
    print_log("Done read av data in.")
    df = sear_by_cols(df, set_range_tickers_list)
    print_log("Done av data col by col.")
    write_data_to_pbz(df, av_output)
    print_log("Wrote av data output.")

    df = read_data(fred_data_file)
    print_log("Done read fred data in.")
    df = sear_by_cols(df, set_range_tickers_list)
    print_log("Done fred data col by col.")
    write_data_to_pbz(df, fred_output)
    print_log("Done wrote fred output.")


def main():
    sear_data()


if __name__ == "__main__":
    main()
