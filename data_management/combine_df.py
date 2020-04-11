import pandas as pd
import argparse
import pickle
import bz2
import time


def read_data(filename):
    if ".p.bz2" not in filename:
        filename = filename + ".p.bz2"
    with bz2.BZ2File(filename) as pfile_handle:
        old_data = pickle.load(pfile_handle)
    return old_data


def write_df_to_pbz(df, filename, filepath="./"):
    if ".p.bz2" not in filename:
        filename = filename + ".p.bz2"
    file_name_and_path = filepath + filename
    with bz2.BZ2File(file_name_and_path, "w") as pfile:
        pickle.dump(df, pfile,
                    protocol=pickle.HIGHEST_PROTOCOL)


def dispatch(file1,
             file2,
             output
             ):
    df1 = read_data(file1)
    df2 = read_data(file2)
    all_df = pd.merge(df1, df2,
                      how='outer', left_index=True, right_index=True)
    if output == "NA":
        output = time.strftime("%Y%m%d-%H%M%S")
    write_df_to_pbz(all_df, output)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--file1',
                        type=str,
                        help='The first p.bz2 database.')
    parser.add_argument('--file2',
                        type=str,
                        help='The 2nd p.bz2 database.')
    parser.add_argument('--output',
                        default="NA",
                        type=str,
                        help='The output p.bz2 database.')
    parse_args, unknown = parser.parse_known_args()
    dispatch(**parse_args.__dict__)
