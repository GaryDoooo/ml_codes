import pickle
import bz2
import time
import logging
import pandas as pd
import os


def cols_of_ticker(ticker, col_list=None, df=None):
    # return a list of col names of the ticker in either a col name list or dataframe
    if col_list is None:
        if not df is None:
            col_list = list(df.columns)
        else:
            return []
    return [_ for _ in col_list if ticker == _.split("_")[0]]


def merge_df(df1, df2):
    if df1 is None:
        return df2
    elif df2 is None:
        return df1
    else:
        return pd.merge(df1, df2,
                        how='outer', left_index=True, right_index=True)


def read_data(filename, filepath="./"):
    # read whatever pickle output to a return
    if ".p.bz2" not in filename:
        filename = filename + ".p.bz2"
    file_name_and_path = filepath + filename
    with bz2.BZ2File(file_name_and_path) as pfile_handle:
        old_data = pickle.load(pfile_handle)
    return old_data


def write_data_to_pbz(df, filename, filepath="./"):
    # write either dataframe or class to pickle
    if ".p.bz2" not in filename:
        filename = filename + ".p.bz2"
    file_name_and_path = filepath + filename
    with bz2.BZ2File(file_name_and_path, "w") as pfile:
        pickle.dump(df, pfile,
                    protocol=pickle.HIGHEST_PROTOCOL)


def print_log(message):
    logging.info(message)
    print(message)


def init_log():
    if not os.path.exists("log"):
        os.makedirs("log")
    timestr = time.strftime("%Y%m%d-%H%M%S")
    logging.basicConfig(filename='log/' + timestr + '.log',
                        format='%(asctime)s %(message)s',
                        level=logging.INFO)
