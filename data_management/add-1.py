#import pandas as pd
from gdu_modules import read_data, write_data_to_pbz


def main():
    filename = "av_cooked"
    df = read_data(filename)
    df = df.sort_index()
    df.loc[-10:-8, 'TIP_vol'] = -1
    write_data_to_pbz(df, filename)


if __name__ == "__main__":
    main()
