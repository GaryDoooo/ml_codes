from fredapi import Fred
from alpha_vantage.timeseries import TimeSeries
import pandas as pd
import argparse
import pickle
import bz2
import numpy as np
import time
import os
import logging
import yaoshi


TIME_OUT = 2  # every step sleep 20 sec, total (TIME_OUT * WAIT_TIME) sec
WAIT_TIME = 180


def print_log(message):
    logging.info(message)
    print(message)


def init_log():
    timestr = time.strftime("%Y%m%d-%H%M%S")
    logging.basicConfig(filename='log/' + timestr + '.log',
                        format='%(asctime)s %(message)s',
                        level=logging.INFO)


def read_fred(key, symbol='QQQ'):
    fred = Fred(api_key=key)
    result = None
    timeout = 0
    while result is None:
        try:
            # connect fred
            # output is a series with date index
            result = fred.get_series(symbol)
        except:
            if timeout < TIME_OUT:
                time.sleep(WAIT_TIME)
                timeout = timeout + 1
                pass
            else:
                print_log("time out %s" % symbol)
                return None
    return result.to_frame(name=symbol)  # convert it to dataframe


def read_stock_AV(keys, symbol='QQQ', interval='5min', outputsize='compact'):
    ts = TimeSeries(key=keys[np.random.randint(len(keys))],
                    output_format='pandas', indexing_type='date')
    result = None
    timeout = 0
    while result is None:
        try:
            # connect AV
            # result, _ = ts.get_intraday(
            #    symbol=symbol, interval=interval, outputsize=outputsize)
            result, _ = ts.get_daily_adjusted(
                symbol=symbol, outputsize=outputsize)
        except:
            if timeout < TIME_OUT:
                time.sleep(WAIT_TIME)
                timeout = timeout + 1
                pass
            else:
                print_log("time out %s" % symbol)
                return None
    return result


def read_data(symbol, filepath="data/", fileprefix=""):
    filename = filepath + fileprefix + symbol + ".p.bz2"
    with bz2.BZ2File(filename) as pfile_handle:
        old_data = pickle.load(pfile_handle)
    return old_data


def write_data(symbol, df, filepath="data/", fileprefix=""):
    filename = filepath + fileprefix + symbol + ".p.bz2"
    if os.path.isfile(filename):
        old_data = read_data(symbol, filepath, fileprefix)
        df = pd.concat([df, old_data])  # .drop_duplicates().sort_index()
        df = df[~df.index.duplicated(keep='first')]
    with bz2.BZ2File(filename, "w") as pfile:
        pickle.dump(df, pfile,
                    protocol=pickle.HIGHEST_PROTOCOL)


def write_df_to_pbz(df, filename, filepath='./'):
    file_name_and_path = filepath + filename + ".p.bz2"
    with bz2.BZ2File(file_name_and_path, "w") as pfile:
        pickle.dump(df, pfile,
                    protocol=pickle.HIGHEST_PROTOCOL)


def adjust_open_high_low(av, ticker):
    av['adj'] = av['5. adjusted close'] / av['4. close']
    av['ao'] = av['adj'] * av['1. open']
    av['ah'] = av['adj'] * av['2. high']
    av['al'] = av['adj'] * av['3. low']
    av['ac'] = av['5. adjusted close']
    df = pd.concat(
        [av['ao'], av['ah'], av['al'], av['ac'], av['6. volume']], axis=1, keys=[
            ticker + '_ao', ticker + '_ah',
            ticker + '_al', ticker + '_ac', ticker + '_vol'])
    return df


def acq_fred_and_av_from_internet(
        fred_ticker_csv,
        av_ticker_csv):
    # print(os.listdir("."))
    init_log()
    key = yaoshi.yaoshi()
############ read AV data ############
    av_df = None
    if av_ticker_csv != "no input":
        av_ticker_list = pd.read_csv(av_ticker_csv, sep=',')
        for ticker in av_ticker_list['Ticker']:
            df = read_stock_AV(
                keys=key.avkeys, symbol=ticker, outputsize='full')
            if df is not None:
                df = adjust_open_high_low(df, ticker)
                print_log("read %s from av [ %s to %s ]" % (ticker,
                                                            df.index[0],  df.index[-1]
                                                            ))
                if av_df is None:
                    av_df = df
                else:
                    av_df = pd.merge(df, av_df,
                                     how='outer', left_index=True, right_index=True)
    #  write_data(ticker, df, filepath=filepath, fileprefix=fileprefix)
############ read FRED data ##########
    fred_df = None
    if fred_ticker_csv != "no input":
        fred_ticker_list = pd.read_csv(fred_ticker_csv, sep=',')
        for ticker in fred_ticker_list['Ticker']:
            df = read_fred(key=key.fredkeys[0], symbol=ticker)
            if df is not None:
                print_log("read %s from FRED [ %s to %s ]" % (ticker,
                                                              df.index[0], df.index[-1]
                                                              ))
                if fred_df is None:
                    fred_df = df
                else:
                    fred_df = pd.merge(df, fred_df,
                                       how='outer', left_index=True, right_index=True)
    return av_df, fred_df


def dispatch(avfilename, fredfilename):
    av_df, fred_df = acq_fred_and_av_from_internet(fred_ticker_csv=fredfilename,
                                                   av_ticker_csv=avfilename)
    timestr = time.strftime("%Y%m%d-%H%M%S")
    if av_df is not None:
        write_df_to_pbz(av_df, timestr + "av_data")
    if fred_df is not None:
        write_df_to_pbz(fred_df, timestr + "fred_data")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--avfilename',
                        default="no input",
                        type=str,
                        help='The p.bz2 database.')
    parser.add_argument('--fredfilename',
                        default="no input",
                        type=str,
                        help='The p.bz2 database.')
    parse_args, unknown = parser.parse_known_args()
    dispatch(**parse_args.__dict__)
