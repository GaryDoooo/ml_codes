from fredapi import Fred
from alpha_vantage.timeseries import TimeSeries
import argparse
import time
import yaoshi
import numpy as np
import logging

TIME_OUT = 1  # every step sleep 20 sec, total (TIME_OUT * WAIT_TIME) sec
WAIT_TIME = 20


def print_log(message):
    logging.info(message)
    print(message)


def init_log():
    logging.basicConfig(filename='log/' + "try_ticker" + '.log',
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
            print("receive error, try again.")
            if timeout < TIME_OUT:
                time.sleep(WAIT_TIME)
                timeout = timeout + 1
                pass
            else:
                print_log("time out %s" % symbol)
                return None
    return result.to_frame(name=symbol)  # convert it to dataframe


def read_stock_AV_intra(keys, symbol='QQQ', interval='5min', outputsize='compact'):
    ts = TimeSeries(key=keys[np.random.randint(len(keys))],
                    output_format='pandas', indexing_type='date')
    result = None
    timeout = 0
    while result is None:
        try:
            # connect AV
            result, _ = ts.get_intraday(
                symbol=symbol, interval=interval, outputsize=outputsize)
        except:
            print("receive error, try again.")
            if timeout < TIME_OUT:
                time.sleep(WAIT_TIME)
                timeout = timeout + 1
                pass
            else:
                print_log("time out %s" % symbol)
                return None
    return result


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
            print("receive error, try again.")
            if timeout < TIME_OUT:
                time.sleep(WAIT_TIME)
                timeout = timeout + 1
                pass
            else:
                print_log("time out %s" % symbol)
                return None
    return result


def dispatch(av,
             fred
             ):
    key = yaoshi.yaoshi()
    print("Got the ticker inputs: AV:%s   FRED:%s" % (av, fred))
    init_log()
############ read AV data ############

    if av != "no input":
        ticker = av
        print("checking... %s" % ticker)
        df = read_stock_AV(keys=key.avkeys, symbol=ticker,
                           outputsize='full')
        if df is not None:
            print_log("read daily %s from av [ %s to %s ]" % (ticker,
                                                              df.index[0],  df.index[-1]
                                                              ))
        df = read_stock_AV_intra(
            keys=key.avkeys, symbol=ticker, outputsize='full')
        if df is not None:
            print_log("read 5min %s from av [ %s to %s ]" % (ticker,
                                                             df.index[0],  df.index[-1]
                                                             ))

############ read FRED data ##########
    if fred != "no input":
        ticker = fred
        print("checking... %s" % ticker)
        df = read_fred(key=key.fredkeys[0], symbol=ticker)
        if df is not None:
            print_log("read %s from FRED [ %s to %s ]" % (ticker,
                                                          df.index[0], df.index[-1]
                                                          ))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--av',
                        default="no input",
                        type=str,
                        help='The first p.bz2 database.')
    parser.add_argument('--fred',
                        default="no input",
                        type=str,
                        help='The 2nd p.bz2 database.')
    parse_args, unknown = parser.parse_known_args()
    dispatch(**parse_args.__dict__)
