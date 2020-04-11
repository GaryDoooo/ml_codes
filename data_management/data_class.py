from gdu_modules import read_data, write_data_to_pbz, init_log, print_log, cols_of_ticker, merge_df
import pandas as pd
import numpy as np


def trim_df_by_ticker(df, list1, list2=None):
    # trim off the df's tickers no in list1 and list2
    # return the list found and not found, and col # per ticker
    cols = list(df.columns)
    keep_col_list = []
    found_ticker_list = []
    unfound_list = []
    looking_for_ticker_list = set(list1 + list2)
    for ticker in looking_for_ticker_list:
        found_cols_of_the_ticker = cols_of_ticker(ticker, col_list=cols)
        if len(found_cols_of_the_ticker) == 0:
            unfound_list.append(ticker)
        else:
            col_per_ticker = len(found_cols_of_the_ticker)
            found_ticker_list.append(ticker)
            keep_col_list.extend(found_cols_of_the_ticker)
    drop_col_list = list(set(cols) - set(keep_col_list))
    df = df.drop(columns=drop_col_list)
    return df, unfound_list, found_ticker_list, col_per_ticker


def trim_df_by_time(df1, df2):
    #write_data_to_pbz(df1, "df1")
    df = merge_df(df1, df2)
    df = df.dropna()
    df1 = df.drop(list(df2.columns), axis=1)
    df2 = df.drop(list(df1.columns), axis=1)
    total_days = df.shape[0]
    start_time = df1.index.values[0]
    end_time = df1.index.values[-1]
    return (start_time, end_time, total_days, df1, df2)


def accumulated_change(ticker, df, start, end):
    sublist = df.loc[start:end, ticker]
    sublist = sublist + 1
    sublist[0] = 1
    return np.prod(sublist)


class data_gen:
    def __init__(self,
                 predict_ticker_list,
                 input_ticker_list,
                 av_data_filename="av_seared",
                 fred_data_filename="fred_seared"):
        init_log()
        self.predict_ticker_list = predict_ticker_list
        self.input_ticker_list = input_ticker_list
        self.av_data_filename = av_data_filename
        self.fred_data_filename = fred_data_filename
        av_data_df = read_data(av_data_filename)
        fred_data_df = read_data(fred_data_filename)
        print_log("Done read av and fred seared data.")

        av_data_df, unfound_list_av, self.av_tickers, self.av_col_per_ticker = trim_df_by_ticker(
            av_data_df, predict_ticker_list, input_ticker_list)
        fred_data_df, unfound_list_fred, self.fred_tickers, self.fred_col_per_ticker = trim_df_by_ticker(
            fred_data_df, predict_ticker_list, input_ticker_list)
        self.unfound_list = [
            _ for _ in unfound_list_av if _ in unfound_list_fred]
        print_log(
            "Done trim the dataframe into the interested tickers only, and gen the unfound list.")
        print_log("Found AV %d tickers %d col/ticker, FRED %d tickers, %d col/ticker." %
                  (len(self.av_tickers), self.av_col_per_ticker,
                   len(self.fred_tickers), self.fred_col_per_ticker))
        print_log("%d tickers not found in either fred or av data sets." %
                  len(self.unfound_list))

        (self.start_time, self.end_time, self.total_days, self.av_data_df,
         self.fred_data_df) = trim_df_by_time(av_data_df,
                                              fred_data_df)
        print_log("Done trim data by avaible data points on time span.")

    def time_info_in_one_str(self):
        return "Start,{},end,{},total_days,{}".format(self.start_time,
                                                      self.end_time,
                                                      self.total_days)

    def gen_data_sets(self,
                      predict_dist_list,  # a list of the days to predict after the center day
                      input_dist,  # how many days to look back, this is an int
                      number_of_data_sets):
        full_df = merge_df(self.av_data_df, self.fred_data_df)
        input_df = trim_df_by_ticker(full_df, self.input_ticker_list)
        predict_df = trim_df_by_ticker(full_df, self.predict_ticker_list)
        today_list = np.random.randint(
            input_dist-1, self.total_days-max(predict_dist_list), size=number_of_data_sets)
        x = None
        y = None
        for i in range(number_of_data_sets):
            today = today_list[i]
            input_array = input_df.loc[today+1-input_dist:today, :].values
            predict_array = []
            for dist in predict_dist_list:
                for ticker in self.predict_ticker_list:
                    predict_array.append(accumulated_change(
                        predict_df, ticker, today, today+dist))
                    # the predict array is 1D with [[ticker1,ticker2...],[dist2 set],[dist3 set]...]
            predict_array = np.expand_dims(np.asarray(predict_array), axis=0)
            input_array = np.expand_dims(np.asarray(input_array), axis=0)
            if x is None:
                x = input_array
            else:
                x = x.append(input_array, axis=0)
            if y is None:
                y = predict_array
            else:
                y = y.append(predict_array, axis=0)
        return x, y


def main():
    d = data_gen(['QQQ'], ['QQQ', '^TNX', 'GOOG', 'APPL', '^VIX', 'DGS10'])
    print("Time ", d.start_time, " to ",
          d.end_time, " total days: ", d.total_days)
    print(d.time_info_in_one_str())
    print("not found ", d.unfound_list)
    write_data_to_pbz(d, "test_data_gen")
    print(pd.DataFrame(np.zeros((2)), columns=["0"]))
    print(accumulated_change('QQQ', d.av_data_df, d.start_time, d.end_time))
    x, y = d.gen_data_sets([10, 20], 50, 10)
    print(x.shape, y.shape)


if __name__ == '__main__':
    main()
