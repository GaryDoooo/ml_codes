import yfinance as yf
from github_correlation import CorrelationCoefficient
#  import datetime


def volume_change(tickers="^SPX SPY QQQ", period="1y"):
    output = ""
    data_h = yf.download(
        tickers=tickers,
        period=period,
        interval="1h",
        group_by="ticker")
    ticker_list = tickers.split()
    #  new_hour=data_h[ticker_list[0]]['Volume'].index[-1].hour
    for ticker in ticker_list:
        res = [0] * 24  # Sum of each hour
        cnt = 0
        for i in data_h[ticker]['Volume'].index:
            res[i.hour] += data_h[ticker]['Volume'][i]
            cnt += (i.hour == 9)
        output += ticker + " Hourly Volume change" + "<br>"
        today = data_h[ticker]['Volume'].index[-1].day
        for i in range(-20, 0):
            index = data_h[ticker]['Volume'].index[i]
            if index.hour == 16:
                continue
            if index.day == today:
                output += ("%02d:%02d %.2f" %
                           (index.hour, index.minute, (data_h[ticker]['Volume'][index] /
                                                       (res[index.hour] /
                                                        cnt) -
                                                       1) *
                            100)) + " "
        output += "<br>" + ticker + " Daily Volume change <br>"
        avg_dayly_vol = sum(res) / cnt
        cnt, today = 0, -1
        for i in range(1, 100):
            index = data_h[ticker]['Volume'].index[-i]
            if index.day != today:
                today = index.day
                cnt += 1
            if cnt == 10 and index.hour == 9:
                start_i = i
                break
        today = -1
        for i in range(-start_i, 0):
            index = data_h[ticker]['Volume'].index[i]
            if index.day != today:
                daily_vol = 0
                today = index.day
            daily_vol += data_h[ticker]['Volume'][index]
            if i == -1 or today != data_h[ticker]['Volume'].index[i + 1].day:
                output += ("%02d/%02d %.2f" % (index.month, index.day,
                                               (daily_vol / avg_dayly_vol - 1) * 100)) + " "
    return output + "<br>"


def corr(listA, listB):
    t = CorrelationCoefficient()
    return t.compute_r(listA, listB)


def correlation_vix_uvxy(
    spans=(("1mo", "1d"), ("5d", "1h"), ("5d", "15m"), ("5d", "5m"))
):
    output = ""
    ticker_string_to_download = "SPY UVXY ^VIX"
    grow_list_of_10 = list(range(10))
    for period, interval in spans:
        output += "Correlation Coefficient by " + interval + "<br>"
        data = yf.download(
            tickers=ticker_string_to_download,
            period=period,
            interval=interval,
            group_by="ticker",
            auto_adjust=True)
        vix = list(data['^VIX']['Close'])
        uvxy = list(data['UVXY']['Close'])
        spx = list(data['SPY']['Close'])
        #  print(spx)
        for ticker in ['^VIX', 'UVXY']:
            l = vix if ticker == "^VIX" else uvxy
            output += "SPY to" + ticker + "<br>"
            for back in range(10):
                temp = corr(l[-11 - back:-1 - back], spx[-11 - back:-1 - back])
                temp2 = ("T" if corr(
                    l[-11 - back:-1 - back], grow_list_of_10) > 0 else "F")
                output += ("%.2f" % temp) + " " + temp2 + " "
            output += "<br>"
    return output


def vix_uvxy_ratio():
    def r(x): return (x - 1) * 100
    output = ""
    data = yf.download(
        tickers="UVXY ^VIX",
        period="5d",
        interval="1d",
        group_by="ticker",
        auto_adjust=True)
    output += "UVXY to VIX ratio" + "<br>"
    today = data['^VIX']['Close'].index[-1]
    yesterday = data['^VIX']['Close'].index[-2]
    res = []
    for i in ['Open', 'Close', 'High', 'Low']:
        res.append(r(data['UVXY'][i][today] /
                     data['UVXY']['Close'][yesterday] *
                     data['^VIX']['Close'][yesterday] /
                     data['^VIX'][i][today]))
        output += i + " %.2f" % res[-1] + "  "
    output += "Average %.2f" % (sum(res) / len(res)) + "<br>"
    return output


def question_gen():
    return volume_change() + correlation_vix_uvxy() + vix_uvxy_ratio()


if __name__ == '__main__':
    #  volume_change()
    #  correlation_vix_uvxy(spans=(('1mo', "1d"),))
    #  correlation_vix_uvxy()
    #  vix_uvxy_ratio()
    print(question_gen())
    pass
