import bz2
import pickle
import numpy as np


class read_data:
    def __init__(self, good_tickers_list, sample_path="samples", test_points=2000):
        self.data_set = np.zeros((0, 0, 0))
        data_points = 0
        print "Reading data..."
        for ticker in good_tickers_list:
            try:
                with bz2.BZ2File(sample_path + "/" + ticker + "_samples.p.bz2", "r") as pfile_handle:
                    samples = pickle.load(pfile_handle)
                data_points += samples.shape[0]
                if self.data_set.shape[0] < 1:
                    self.data_set = samples
                else:
                    #                  print samples.shape
                    try:
                        self.data_set = np.concatenate(
                            (self.data_set, samples), axis=0)
                    except ValueError:
                        print ticker, "Dimension mismatch.", samples.shape
            except IOError:
                print ticker, "File read error."
        print "Total read data points:", data_points
        self.train_data, self.test_data = self.shuffle_and_split_test(
            test_points)

    def shuffle_and_split_test(self, test_points):
        np.random.shuffle(self.data_set)
        return self.data_set[:self.data_set.shape[0] - test_points, :, :], self.data_set[-test_points:, :, :]


def main():
    good_tickers_list = pickle.load(open("Tickers_with_good_data.p", "rb"))
    data_set = read_data(good_tickers_list)
    print data_set.train_data.shape, data_set.test_data.shape


if __name__ == "__main__":
    main()
