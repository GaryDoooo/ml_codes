import yfinance as yf
#  from github_correlation import CorrelationCoefficient
#  import datetime
from math import isnan
from scipy import stats
#  from font_tools import parantheses, red_highlight
import pandas as pd

FILE_NAME = "slope.pickle"


def avg(alist):
    try:
        return sum(alist) / len(alist)
    except BaseException:
        return 0


def read_save_data(
        #  show_stat_only=False,
    spans=(("1mo", "1d"), ),
    filename=FILE_NAME
):
    #  output = ""
    ticker_string_to_download = "DIA SPY QQQ IWM"
    #  grow_list_of_10 = list(range(10))
    #  for period, interval in spans:
    period, interval = spans[0]
    #  output += "### Slope by **" + interval + "**\n"
    data = yf.download(
        tickers=ticker_string_to_download,
        period=period,
        interval=interval,
        group_by="ticker",
        auto_adjust=True)
    data.to_pickle(filename)
    return


def data_analysis(
    rsq_bar=0.9, slp_bar=0.1, filename=FILE_NAME
):
    data = pd.read_pickle(filename)
    #  time1 = []
    #  for index in data['DIA']['Close'].index:
    #      if interval.endswith("m"):
    #          time1.append("%02d%02d" %
    #                       (index.hour, index.minute))
    #      else:
    #          time1.append("%02d/%02d" %
    #                       (index.month, index.day))
    dia = list(data['DIA']['Close'])
    spy = list(data['SPY']['Close'])
    qqq = list(data['QQQ']['Close'])
    iwm = list(data['IWM']['Close'])
    i, cnt = 1, 0
    dia_r, spy_r, qqq_r, iwm_r = [], [], [], []
    slope, r2 = [], []
    dia_rate = spy_rate = qqq_rate = iwm_rate = 0
    #  top, mid, l1, l2, l3, l4, l5, l6 = "| <!-- --> |", "|:---:|", "| DIA |",\
    #      "| SPY |", "| QQQ |", "| IWM |", "| slp |", "| r^2 |"
    print("Read data points", len(dia), len(spy), len(qqq), len(iwm))
    while True:
        if i + 1 > len(dia):
            break
        try:
            dia_rate = (dia[-i] / dia[-i - 1] - 1) * 100
            spy_rate = (spy[-i] / spy[-i - 1] - 1) * 100
            qqq_rate = (qqq[-i] / qqq[-i - 1] - 1) * 100
            iwm_rate = (iwm[-i] / iwm[-i - 1] - 1) * 100
        except BaseException:
            i += 1
            continue
        i += 1
        if isnan(dia_rate * spy_rate * qqq_rate * iwm_rate):
            continue
        cnt += 1
        dia_r.append(dia_rate)
        spy_r.append(spy_rate)
        qqq_r.append(qqq_rate)
        iwm_r.append(iwm_rate)
        #  time.append(time1[-i])
        slope_, _, r_value, _, _ = stats.linregress(
            [1, 2, 3, 4],
            [dia_rate, spy_rate, qqq_rate, iwm_rate]
        )
        slope.append(slope_)
        r2.append(r_value**2)
        #  += " " + bold + parantheses(temp) + bold
        #  if i % 100 == 0:
        #      print(i)
    print("Valid data points:", len(dia_r))
    ttl_hits = true_hits = dia_win = spy_win = qqq_win = iwm_win = 0
    for i in range(len(dia_r)):
        slp, rsq = slope[i], r2[i]
        #  if slp >= slp_bar and rsq >= rsq_bar:
        #      ttl_hits += 1
        #      if (dia_r[i + 1] > 0) + (spy_r[i + 1] > 0) + \
        #              (qqq_r[i + 1] > 0) + (iwm_r[i + 1] > 0) > 2:
        #          true_hits += 1
        #      dia_win += dia_r[i + 1] > 0
        #      spy_win += spy_r[i + 1] > 0
        #      qqq_win += qqq_r[i + 1] > 0
        #      iwm_win += iwm_r[i + 1] > 0
        if slp <= -slp_bar and rsq >= rsq_bar:
            ttl_hits += 1
            if (dia_r[i + 1] < 0) + (spy_r[i + 1] < 0) + \
                    (qqq_r[i + 1] < 0) + (iwm_r[i + 1] < 0) > 2:
                true_hits += 1
            dia_win += dia_r[i + 1] < 0
            spy_win += spy_r[i + 1] < 0
            qqq_win += qqq_r[i + 1] < 0
            iwm_win += iwm_r[i + 1] < 0
    print("Total hits", ttl_hits)
    print("True hits", true_hits, "ratio", true_hits / ttl_hits)
    print("DIA", dia_win, "ratio", dia_win / ttl_hits)
    print("Spy", spy_win, "ratio", spy_win / ttl_hits)
    print("QQQ", qqq_win, "ratio", qqq_win / ttl_hits)
    print("IWM", iwm_win, "ratio", iwm_win / ttl_hits)


if __name__ == '__main__':
    #  read_save_data(spans=(("max", "1d"),), filename="max_1d.pickle")
    #  data_analysis(rsq_bar=0.95, slp_bar=0.01, filename="max_1d.pickle")
    #  read_save_data(spans=(("2y", "1h"),), filename="max_1h.pickle")
    data_analysis(rsq_bar=0.9, slp_bar=0.001, filename="max_1h.pickle")
    #  read_save_data(spans=(("60d", "15m"),), filename="max_15m.pickle")
    #  data_analysis(rsq_bar=0.9, slp_bar=0.1, filename="max_15m.pickle")
    #  print(speed_stat(show_stat_only=False))
    pass
