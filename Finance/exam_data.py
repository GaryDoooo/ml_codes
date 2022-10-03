import pickle
import numpy as np
import bz2


class read_data:
    def __init__(self, datafile):
        with bz2.BZ2File(datafile, "r") as pfile_handle:
            self.data = pickle.load(pfile_handle)

    def print_stat(self, input_data):
        for i in range(input_data.shape[-1]):
            print("Row", i, ends=" ")
            print("Avg=%.2f" % np.mean(input_data[:, :, i]), ends=" ")
            print("Std=%.2f" % np.std(input_data[:, :, i]), ends=" ")
            print("Max=%.2f" % np.max(input_data[:, :, i]), ends=" ")
            print("Min=%.2f" % np.min(input_data[:, :, i]), ends=" ")
            print("Nan=%d" % np.sum(1 * np.isnan(input_data[:, :, i])))


def save_data2p(data):
    pickle.dump(data, open("samples/whole.p", "wb"),
                protocol=pickle.HIGHEST_PROTOCOL)


def main():
    data_set = read_data("data/spy.p.bz2")
    print(data_set.data.shape)
    print(data_set.data)
    #  data_set.print_stat(data_set.data[:, 1:, :])

    #  save_data2p(data_set.data[:, :, 1:])


if __name__ == "__main__":
    main()
