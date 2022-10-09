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


def save_data2p(data, filename="data/save.pickle.bz2"):
    #  pickle.dump(data, open("samples/whole.p", "wb"),
    #              protocol=pickle.HIGHEST_PROTOCOL )
    with bz2.BZ2File(filename, "w") as pfile:
        pickle.dump(data, pfile,
                    protocol=pickle.HIGHEST_PROTOCOL)


class process_data:
    def __init__(self, filename):
        with bz2.BZ2File(filename, "r") as pfile_handle:
            self.data = pickle.load(pfile_handle)
        date_set = set()
        for i in self.data.index:
            date_set.add(str(i).split()[0])
        self.date_list = sorted(list(date_set))
        self.time_idx_str_list = [str(_) for _ in self.data.index]

    def query_by_date(
            self,
            date,
            end_date=None,
            before="16:01",
            after="09:29"):
        date = date.strip()
        if end_date is None:
            end_date = date
        return self.data[[_ >= date + " " +
                          after.strip() and _ <= end_date + " " +
                          before.strip() for _ in self.time_idx_str_list]]

    def get_OHLCV(self, date, end_date=None, before="16:01", after="09:29"):
        date = date.strip()
        if end_date is None:
            end_date = date
        d = self.data[[_ >= date + " " +
                       after.strip() and _ <= end_date + " " +
                       before.strip() for _ in self.time_idx_str_list]]
        #  print(d)
        res = dict()
        res["open"] = d["1. open"][d.index[0]]
        res["close"] = d["4. close"][d.index[-1]]
        res["vol"], res["low"], res["high"] = 0, 1e9, -1e9
        for i in d.index:
            res["high"] = max(res["high"], d["2. high"][i])
            res["low"] = min(res["low"], d["3. low"][i])
            res["vol"] += d["5. volume"][i]
        return res


def get_decimal_time(time_idx_str_list, out_days):
    if out_days == int(out_days):
        return "09:29", "16:01"
    out_days = out_days - int(out_days)
    day = time_idx_str_list[0].split()[0]
    time_stamps_one_day = [_.split()[1] for _ in time_idx_str_list if day in _]
    #  print(time_stamps_one_day)
    split_idx = int(len(time_stamps_one_day) * out_days)
    return time_stamps_one_day[split_idx + 1], time_stamps_one_day[split_idx]


def several_days_to_trade_range(
    file_prefix="data/", file_suffix=".p.bz2",
    in_files=("SPY", "QQQ", "UVXY"), out_file="SPY",
    include=("4. close", "5. volume"),
    in_days=3.5, out_days=0.5,
    oscillate_range=(-.8, -.4, -.2, -.1, .1, .2, .4, .8)
):
    indata = []
    for ticker in in_files:
        indata.append(process_data(file_prefix + ticker + file_suffix))
        print("Read", ticker, "for", len(indata[-1].date_list), "days")
    outdata = process_data(file_prefix + out_file + file_suffix)
    print("Read", out_file, "for", len(outdata.date_list), "days")
    date_list = outdata.date_list
    #  print(date_list)
    for i in indata:
        if len(date_list) != len(i.date_list):
            print("Data length mismatch.")
            return
    total_days = int(in_days + out_days)
    in_res, out_res = [], []
    out_start_time, in_end_time = get_decimal_time(
        outdata.time_idx_str_list,
        in_days)
    #  print(out_start_time, in_end_time)
    in_end_idx_offset = int(in_days + 0.999) - 1
    out_start_idx_offset = total_days - int(out_days + 0.999)
    for i in range(len(date_list) - total_days + 1):
        in_start_date = date_list[i]
        in_end_date = date_list[i + in_end_idx_offset]
        out_start_date = date_list[i + out_start_idx_offset]
        out_end_date = date_list[i + total_days - 1]
        #  print(in_start_date, in_end_date, out_start_date, out_end_date)
        temp = []
        for j in indata:
            temp2 = j.query_by_date(
                date=in_start_date,
                end_date=in_end_date,
                before=in_end_time)
            for k in include:
                #  print(temp2[k])
                #  print(temp2[k].to_numpy())
                #  return
                temp.append(temp2[k].to_numpy())
        in_res.append(temp)
        temp = outdata.get_OHLCV(
            date=out_start_date,
            end_date=out_end_date,
            after=out_start_time)
        high = (temp['high'] / temp['open'] - 1) * 100
        low = (temp['low'] / temp['open'] - 1) * 100
        temp = []
        for j in oscillate_range:
            temp.append(1 if low <= j <= high else 0)
        out_res.append(temp)
    #  print(in_res)
    return np.asarray(in_res)
    #  return np.asarray(out_res)


if __name__ == "__main__":
    #  several_days_to_trade_range()
    several_days_to_trade_range(
        in_files=(
            "spy",
            "qqq"),
        out_file="spy")
    #  s = process_data("data/SPY.p.bz2")
    #  print(s.query_by_date(s.date_list[0]))
    #  print(len(s.date_list))
    #  print(s.get_OHLCV(s.date_list[0]))
    #  d = s.query_by_date(s.date_list[0], after="15:45")
    #  print(d.to_numpy().transpose())
    #  s = old_data("data/spy.p.bz2")
    #  print(s.query_by_date(s.date_list[0]))
    #  print(len(s.date_list))
    pass
    #  main()
