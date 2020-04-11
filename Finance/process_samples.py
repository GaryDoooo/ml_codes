import bz2
import pickle


def main():
    ticker_list = pickle.load(open("Tickers_with_good_data.p", "rb"))
    number_of_samples = 0
    for ticker in ticker_list:
        try:
            with bz2.BZ2File("samples/" + ticker + "_samples.p.bz2", "r") as pfile_handle:
                samples = pickle.load(pfile_handle)
            number_of_samples += samples.shape[0]
        except IOError:
            print "File read error for: " + ticker + "."
    print "Total samples:", number_of_samples


if __name__ == "__main__":
    main()
