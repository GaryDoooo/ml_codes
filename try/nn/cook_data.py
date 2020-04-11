import pandas as pd
import pickle
import bz2
import time
import logging
from pyti.exponential_moving_average import exponential_moving_average as ema
from pyti.relative_strength_index import relative_strength_index as rsi


def add_indicators(data, ema_period=[5, 25, 100], rsi_period=[14], prefix=""):
    result = None
    for period in ema_period:
        r_r = ema(data, period)
        df = pd.DataFrame(r_r, index=data.index, columns=[
                          prefix + "_%dema" % period])
        if result is None:
            result = df
        else:
            result = pd.merge(df, result,
                              how='outer', left_index=True, right_index=True)
    for period in rsi_period:
        r_r = rsi(data, period)
        df = pd.DataFrame(r_r, index=data.index, columns=[
                          prefix + "_%drsi" % period])
        result = pd.merge(df, result,
                          how='outer', left_index=True, right_index=True)
    return result


def print_log(message):
    logging.info(message)
    print(message)


def init_log():
    timestr = time.strftime("%Y%m%d-%H%M%S")
    logging.basicConfig(filename='log/' + timestr + '.log',
                        format='%(asctime)s %(message)s',
                        level=logging.INFO)


def read_data(filename, filepath="data/", fileprefix=""):
    filename = filepath + fileprefix + filename + ".p.bz2"
    with bz2.BZ2File(filename) as pfile_handle:
        old_data = pickle.load(pfile_handle)
    return old_data


def write_df_to_pbz(df, filename, filepath='./'):
    file_name_and_path = filepath + filename + ".p.bz2"
    with bz2.BZ2File(file_name_and_path, "w") as pfile:
        pickle.dump(df, pfile,
                    protocol=pickle.HIGHEST_PROTOCOL)


def find_ticker_list(data):
    ticker_list = []
    col = list(data.columns.values)
    for ticker in col:
        if "_ac" in ticker:
            ticker_list.append(ticker.replace("_ac", ""))
        elif "_" in ticker:
            pass
        else:
            ticker_list.append(ticker)
    return ticker_list


def relative_dist(df, ticker):
    col_list = list(df.columns.values)
    drop_list = [_ for _ in col_list if "rsi" in _]
    drop_list.append(ticker)
    operation_list = [_ for _ in col_list if not _ in drop_list]
    result = df[drop_list]
    for col in operation_list:
        #result.append({col: df[col] / df[ticker] - 1}, ignore_index=True)
        result[col] = df[col] / df[ticker] - 1
    return result


def pick_close_and_add_indicators_and_convert_relative_dist(data, ema_period, rsi_period):
    ticker_list = find_ticker_list(data)
    cols = list(data.columns.values)
    result = None
    for ticker in ticker_list:
        try:
            sub_list = [_ for _ in cols if ticker in _]
            sub_df = data[sub_list].dropna()
            if ticker + "_ac" in list(sub_df.columns.values):
                res_sub_df = sub_df.copy()
                res_sub_df = res_sub_df.drop(
                    [_ for _ in list(sub_df.columns.values) if not "_ac" in _], axis=1)
                res_sub_df.columns = [ticker]
                res_sub_df = pd.merge(res_sub_df,  sub_df.drop(
                    columns=[ticker + "_ac"]), how="outer", left_index=True, right_index=True)
            else:
                res_sub_df = sub_df.copy()

            res_sub_df = pd.merge(res_sub_df,
                                  add_indicators(
                                      res_sub_df[ticker], ema_period, rsi_period, prefix=ticker),
                                  how="outer", left_index=True, right_index=True)
            print(res_sub_df.head(20))
            res_sub_df = relative_dist(res_sub_df, ticker)
            print(res_sub_df.head(20))
            if result is None:
                result = res_sub_df
            else:
                result = pd.merge(result, res_sub_df, how="outer",
                                  left_index=True, right_index=True)
        except:
            print_log("Error with " + ticker)

    return result


def load_data(ema_period=[5, 25, 100], rsi_period=[14],
              save_result=False,
              av_save="av_cooked",
              fred_save="fred_cooked"):
    # load the two database files in the same dir
    # add indicators, change the open, high, low, ema to relative distance to close, return 2 df,
    # def add_indicators(data,ema_period=[5,25,100],rsi_period=[14],prefix=""):
    init_log()
    av_data = read_data("av_data", "./")
    fred_data = read_data("fred_data", "./")
    av_data = pick_close_and_add_indicators_and_convert_relative_dist(
        av_data, ema_period, rsi_period)
    fred_data = pick_close_and_add_indicators_and_convert_relative_dist(
        fred_data, ema_period, rsi_period)
    if save_result:
        write_df_to_pbz(av_data, av_save)
        write_df_to_pbz(fred_data, fred_save)
    return av_data, fred_data


def main():
    av_data, fred_data = load_data(save_result=True)
    print(av_data.head(20))
    print(fred_data.head(20))


if __name__ == "__main__":
    main()
