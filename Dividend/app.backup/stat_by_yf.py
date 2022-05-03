import yfinance as yf
from github_correlation import CorrelationCoefficient
import datetime


def avg(alist):
    try:
        return sum(alist) / len(alist)
    except BaseException:
        return 0


def parantheses(num):
    return ' {0:.2f} '.format(
        num) if num >= 0 else ' ({0:.2f}) '.format(abs(num))


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
        res = []  # Sum of each hour
        for i in range(24):
            res.append([])
        #  cnt = 0
        for i in data_h[ticker]['Volume'].index:
            vol = data_h[ticker]['Volume'][i]
            if vol > 0:
                res[i.hour].append(vol)
            #  cnt += (i.hour == 9)
        output += "### " + ticker + " Hourly Volume change" + "\n\n"
        today = data_h[ticker]['Volume'].index[-1].day
        top, mid, bottom = "|", "|", "|"
        for i in range(-20, 0):
            index = data_h[ticker]['Volume'].index[i]
            if index.hour == 16 or index.minute != 30:
                continue
            if index.day == today:
                top += (" %02d:%02d |" % (index.hour, index.minute))
                bottom += parantheses(
                    (data_h[ticker]['Volume'][index] /
                     avg(res[index.hour]) * 100 - 100)) + "|"
                mid += ":---:|"
        output += top + "\n" + mid + "\n" + bottom + \
            "\n\n### " + ticker + " Daily Volume change \n"
        #  for i in res:
        #      print(len(i), avg(i))
        avg_dayly_vol = sum([avg(_) for _ in res])
        cnt, today = 0, -1
        for i in range(1, 100):
            index = data_h[ticker]['Volume'].index[-i]
            if index.day != today:
                today = index.day
                cnt += 1
            if cnt == 10 and index.hour == 9 and index.minute == 30:
                start_i = i
                break
        today = -1
        top, mid, bottom = "|", "|", "|"
        for i in range(-start_i, 0):
            index = data_h[ticker]['Volume'].index[i]
            if index.day != today:
                daily_vol = 0
                today = index.day
            daily_vol += data_h[ticker]['Volume'][index]
            if i == -1 or today != data_h[ticker]['Volume'].index[i + 1].day:
                top += (" %02d/%02d |" % (index.month, index.day))
                bottom += parantheses((daily_vol /
                                       avg_dayly_vol * 100 - 100)) + "|"
                mid += ":---:|"
        output += top + "\n" + mid + "\n" + bottom + "\n"
    return output + "\n"


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
        output += "### Correlation Coefficient by **" + interval + "**\n"
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
        top, mid, bottom1, bottom2 = "| <!-- --> |", "|:---:|", "| VIX |", "| UVXY |"
        for ticker in ['^VIX', 'UVXY']:
            l = vix if ticker == "^VIX" else uvxy
            #  output += "SPY to" + ticker + "\n"
            for back in range(10):
                temp = corr(l[-11 - back:-1 - back], spx[-11 - back:-1 - back])
                temp2 = corr(l[-11 - back:-1 - back], grow_list_of_10) > 0
                #  output += ("%.2f" % temp) + " " + temp2 + " "
                if ticker == "UVXY":
                    top += " <!-- --> |"
                    mid += ":---:|"
                    bold = "**" if temp > 0 and temp2 else ""
                    bottom2 += " " + bold + parantheses(temp) + bold
                    if not temp2:
                        bottom2 += "f"
                    bottom2 += " |"
                else:
                    bold = "**" if temp > 0 and temp2 else ""
                    bottom1 += " " + bold + parantheses(temp) + bold
                    if not temp2:
                        bottom1 += "f"
                    bottom1 += " |"

            #  output += "\n"
        output += top + "\n" + mid + "\n" + bottom1 + "\n" + bottom2 + "\n"
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
    output += "### UVXY to VIX ratio" + "\n"
    today = data['^VIX']['Close'].index[-1]
    yesterday = data['^VIX']['Close'].index[-2]
    res = []
    top, mid, bottom = "|", "|", "|"
    for i in ['Open', 'Close', 'High', 'Low']:
        res.append(r(data['UVXY'][i][today] /
                     data['UVXY']['Close'][yesterday] *
                     data['^VIX']['Close'][yesterday] /
                     data['^VIX'][i][today]))
        top += " " + i + " |"
        bottom += parantheses(res[-1]) + "|"
        mid += ":---:|"
    output += top + " Average |\n" + mid + ":---:|\n" + \
        bottom + parantheses(sum(res) / len(res)) + "|\n"
    return output


def question_gen():
    time = "##### Update time " + str(datetime.datetime.today()) + "\n"
    return volume_change() + correlation_vix_uvxy() + vix_uvxy_ratio() + time


if __name__ == '__main__':
    #  volume_change()
    #  correlation_vix_uvxy(spans=(('1mo', "1d"),))
    #  correlation_vix_uvxy()
    #  vix_uvxy_ratio()
    print(question_gen().replace("\n", "\n").replace("\n", "\n"))
    pass
