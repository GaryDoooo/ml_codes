import pandas as pd
import pickle
import numpy as np
import bz2


def find_index(input_array, number_to_find):
    return np.argmin(np.abs(input_array - number_to_find))


class process_data:
    def __init__(self, file_handle):
        df_1D = pickle.load(file_handle)
        df_1D['day'] = pd.to_datetime(df_1D.index)
        start_date = df_1D['day'][0]
        df_1D = self.adjust_to_adj_close(df_1D)
        df_5D = self.resample(df_1D, '5D')
        df_10D = self.resample(df_1D, '10D')
        df_1D = self.add_macd_ma(df_1D)
        df_10D = self.add_macd_ma(df_10D)
        df_5D = self.add_macd_ma(df_5D)
        df_1D = self.normalize_data(df_1D)
        df_5D = self.normalize_data(df_5D)
        df_10D = self.normalize_data(df_10D)
        self.array_1D = self.convert_to_array(start_date, df_1D)
        self.array_5D = self.convert_to_array(start_date, df_5D)
        self.array_10D = self.convert_to_array(start_date, df_10D)

    def sampling(self, sample_distance=100, sample_len=260):
        sample_range = self.array_1D.shape[0] - sample_len
        N_of_samples = int(sample_range / sample_distance * 2)
        sample_len_in_10D = find_index(
            self.array_10D[:, 0], self.array_1D[sample_len, 0])
        for i in range(N_of_samples):
            end_date_index_in_10D = np.random.randint(
                low=sample_len_in_10D, high=self.array_10D.shape[0] - 2)
            end_date_index_in_1D = find_index(
                self.array_1D[:, 0], self.array_10D[end_date_index_in_10D, 0])
            end_date_index_in_5D = find_index(
                self.array_5D[:, 0], self.array_10D[end_date_index_in_10D, 0])
            #  np.where(self.array_1D == self.array_10D[end_date_index_in_10D, 0])
            #  (self.array_10D < self.array_1D[end_date_index_in_1D, 0] + 0.5) & (self.array_10D > self.array_1D[end_date_index_in_1D, 0] - 0.5))
            #  print self.array_1D[end_date_index_in_1D, 0], self.array_1D[end_date_index_in_1D - 1, 0], self.array_5D[end_date_index_in_5D, 0], self.array_10D[end_date_index_in_10D, 0], end_date_index_in_1D, end_date_index_in_5D, end_date_index_in_10D,
            sample1D = self.array_1D[end_date_index_in_1D -
                                     sample_len:end_date_index_in_1D + 1, :]
            sample5D = self.array_5D[end_date_index_in_5D -
                                     int(sample_len / 5):end_date_index_in_5D + 1, :]
            sample10D = self.array_10D[end_date_index_in_10D -
                                       int(sample_len / 10):end_date_index_in_10D + 1, :]
            # 4 is adj close
            change_in_10D = self.array_10D[end_date_index_in_10D + 1, 4]
            change_in_20D = (1 + change_in_10D) * (1 +
                                                   self.array_10D[end_date_index_in_10D + 2, 4]) - 1
            colume_0 = [[
                change_in_10D,
                change_in_20D,
                self.array_1D.shape[0],
                self.array_5D.shape[0],
                self.array_10D.shape[0],
                sample_distance,
                sample_len,
                N_of_samples,
                0, 0, 0, 0, 0, 0]]
            # print sample1D.shape, sample5D.shape, sample10D.shape, colume_0.shape, colume_1.shape
            unit_sample = np.concatenate(
                (colume_0, sample1D, sample5D, sample10D), axis=0)
            unit_sample = np.expand_dims(unit_sample, axis=0)
            if i == 0:
                all_samples = np.copy(unit_sample)
            else:
                try:
                    all_samples = np.concatenate(
                        (all_samples, np.copy(unit_sample)), axis=0)
                except ValueError:
                    print "ValueError", all_samples.shape, unit_sample.shape
        # print all_samples.shape, all_samples[0, 0, :]
        if 'all_samples' in locals():
            return all_samples
        else:
            return np.zeros((1, 1, 1))

    def normalize_data(self, dataframe):
        dataframe = self.relative_deviation(dataframe, 'Open', 'Adj Close')
        dataframe = self.relative_deviation(dataframe, 'High', 'Adj Close')
        dataframe = self.relative_deviation(dataframe, 'Low', 'Adj Close')
        dataframe = self.relative_deviation(
            dataframe, 'Adj Close', 'Adj Close')
        dataframe = self.relative_deviation(dataframe, 'Volume', 'Volume')
        dataframe = self.relative_deviation(dataframe, '5ma', '5ma')
        dataframe = self.relative_deviation(dataframe, '10ma', '10ma')
        dataframe = self.relative_deviation(dataframe, '20ma', '20ma')
        dataframe = self.relative_deviation(dataframe, '50ma', '50ma')
        dataframe = self.relative_deviation(dataframe, '100ma', '100ma')
        return dataframe

    def relative_deviation(self, dataframe, col_change, col_ref):
        #  colume = dataframe[col_change].as_matrix()
        #  colume_ref = dataframe[col_ref].as_matrix()
        #  for i in range(1, colume.shape[0]):
            #  colume[i] = colume[i] / colume_ref[i - 1]
        #  colume[0] = colume[0] / colume_ref[0]
        #  dataframe[col_change] = colume
        reference = dataframe[col_ref]
        reference = reference.shift(1)
        reference[0] = reference[1]
        dataframe[col_change] = dataframe[col_change] / reference - 1
        return dataframe

    def adjust_to_adj_close(self, dataframe):
        dataframe['adj'] = dataframe['Close'] / dataframe['Adj Close']
        dataframe['Open'] = dataframe['Open'] / dataframe['adj']
        dataframe['High'] = dataframe['High'] / dataframe['adj']
        dataframe['Low'] = dataframe['Low'] / dataframe['adj']
        return dataframe

    def resample(self, dataframe, resample_range):
        df_ohlc_new = dataframe.resample(resample_range).agg(
            {'Open': 'first',
             'High': 'max',
             'Low': 'min',
             'Adj Close': 'last'})
        df_ohlc_new['Volume'] = dataframe['Volume'].resample(
            resample_range).sum()
        return df_ohlc_new

    def add_macd_ma(self, dataframe):
        # Calculate moving average lines
        dataframe['100ma'] = dataframe['Adj Close'].rolling(
            window=100, min_periods=0).mean()
        dataframe['5ma'] = dataframe['Adj Close'].rolling(
            window=5, min_periods=0).mean()
        dataframe['10ma'] = dataframe['Adj Close'].rolling(
            window=10, min_periods=0).mean()
        dataframe['20ma'] = dataframe['Adj Close'].rolling(
            window=20, min_periods=0).mean()
        dataframe['50ma'] = dataframe['Adj Close'].rolling(
            window=50, min_periods=0).mean()
        # Calculate MACD
        dataframe['26 ema'] = dataframe['Adj Close'].ewm(span=26).mean()
        dataframe['12 ema'] = dataframe['Adj Close'].ewm(span=12).mean()
        dataframe['macd'] = dataframe['12 ema'] - dataframe['26 ema']
        dataframe['signal'] = dataframe['macd'].ewm(span=9).mean()
        dataframe['hist'] = dataframe['macd'] - dataframe['signal']
        return dataframe

    def convert_to_array(self, start_date, dataframe):
        dataframe['day'] = pd.to_datetime(dataframe.index)
        dataframe['day'] = dataframe['day'] - start_date
        dataframe['day'] = dataframe['day'].astype('timedelta64[D]')
        new_array = dataframe[['day', 'Open', 'High', 'Low',
                               'Adj Close', 'Volume', '5ma',
                               '10ma', '20ma', '50ma',
                               '100ma', 'macd', 'signal',
                               'hist']].as_matrix()
        return new_array


def process_stock(stock_name):
    with bz2.BZ2File(stock_name + ".p.bz2", "r") as pfile:
        data_cooked = process_data(pfile)
    #  print data_cooked.array_1D[:8, 1:8]
    #  print data_cooked.array_1D.shape
    samples = data_cooked.sampling(sample_distance=100, sample_len=260)
    #  for i in range(0, samples.shape[0]):
    #  print samples[i, 1, 1],
    #  print ""
    #  for i in range(0, samples.shape[0]):
    #  print samples[i, 0, 0],
    #  print ""
    if samples.shape[1] > 1:  # if has no sample extracted, return a 1,1,1 zero array
        print "Saving..." + stock_name + " extracted samples:", samples.shape
        with bz2.BZ2File(stock_name + "_samples.p.bz2", "w") as pfile:
            pickle.dump(samples, pfile,
                        protocol=pickle.HIGHEST_PROTOCOL)


def main():
    # process_stock("GOOGL")
    total_list = pickle.load(open("Tickers_with_good_data.p", "rb"))
    for ticker in total_list:
        process_stock("data/" + ticker)


if __name__ == "__main__":
    main()
