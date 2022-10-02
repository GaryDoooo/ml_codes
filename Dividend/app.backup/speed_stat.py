import yfinance as yf
#  from github_correlation import CorrelationCoefficient
#  import datetime
from math import isnan
from scipy import stats
from font_tools import parantheses, red_highlight


def avg(alist):
    try:
        return sum(alist) / len(alist)
    except BaseException:
        return 0


#  def corr(listA, listB):
#      t = CorrelationCoefficient()
#      return t.compute_r(listA, listB)
#


def speed_stat(
        show_stat_only=False,
    spans=(("3mo", "1d"), ("5d", "15m")),
    rsq_bar=0.9, slp_bar=0.1
):
    output = ""
    ticker_string_to_download = "DIA SPY QQQ IWM"
    #  grow_list_of_10 = list(range(10))
    for period, interval in spans:
        output += "### Slope by **" + interval + "**\n"
        data = yf.download(
            tickers=ticker_string_to_download,
            period=period,
            interval=interval,
            group_by="ticker",
            auto_adjust=True)
        time1 = []
        for index in data['DIA']['Close'].index:
            if interval.endswith("m"):
                time1.append("%02d%02d" %
                             (index.hour, index.minute))
            else:
                time1.append("%02d/%02d" %
                             (index.month, index.day))
        dia = list(data['DIA']['Close'])
        spy = list(data['SPY']['Close'])
        qqq = list(data['QQQ']['Close'])
        iwm = list(data['IWM']['Close'])
        i, cnt = 1, 0
        dia_r, spy_r, qqq_r, iwm_r, time = [], [], [], [], []
        slope, r2 = [], []
        dia_rate = spy_rate = qqq_rate = iwm_rate = 0
        top, mid, l1, l2, l3, l4, l5, l6 = "| <!-- --> |", "|:---:|", "| DIA |",\
            "| SPY |", "| QQQ |", "| IWM |", "| slp |", "| r^2 |"
        while True:
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
            time.append(time1[-i])
            slope_, _, r_value, _, _ = stats.linregress(
                [1, 2, 3, 4],
                [dia_rate, spy_rate, qqq_rate, iwm_rate]
            )
            slope.append(slope_)
            r2.append(r_value**2)
            #  += " " + bold + parantheses(temp) + bold
            if cnt >= 15 or i + 1 > len(dia):
                break
        for i in range(cnt):
            top += " " + time[-i - 1] + " |"
            mid += ":---:|"
            l1 += parantheses(dia_r[-i - 1]) + " |"
            l2 += parantheses(spy_r[-i - 1]) + " |"
            l3 += parantheses(qqq_r[-i - 1]) + " |"
            l4 += parantheses(iwm_r[-i - 1]) + " |"
            if abs(slope[-i - 1]) >= slp_bar:
                l5 += red_highlight(parantheses(slope[-i - 1])) + " |"
            else:
                l5 += parantheses(slope[-i - 1]) + " |"
            if r2[-i - 1] >= rsq_bar:
                l6 += red_highlight(parantheses(r2[-i - 1])) + " |"
            else:
                l6 += parantheses(r2[-i - 1]) + " |"
        output += top + "\n" + mid + "\n"
        if not show_stat_only:
            output += l1 + "\n" + l2 + "\n" + l3 + "\n" + l4 + "\n"
        output += l5 + "\n" + l6 + "\n"
    return output

    #      for _ in range(20):
    #          while(isnan(vix1[-i] * uvxy1[-i] * spx1[-i])):
    #              i += 1
    #          vix.append(vix1[-i])
    #          uvxy.append(uvxy1[-i])
    #          spx.append(spx1[-i])
    #          time.append(time1[-i])
    #          i += 1
    #      vix = vix[::-1]
    #      uvxy = uvxy[::-1]
    #      spx = spx[::-1]
    #      print(spx, vix, uvxy)
    #      top, mid, bottom1, bottom2, bottom3 = "| <!-- --> |", "|:---:|", "| VIX |", "| UVXY |", "| Inter |"
    #      for ticker in ['^VIX', 'UVXY']:
    #          l = vix if ticker == "^VIX" else uvxy
    #          #  output += "SPY to" + ticker + "\n"
    #          for back in range(10):
    #              temp = corr(l[-11 - back:-1 - back], spx[-11 - back:-1 - back])
    #              temp2 = corr(l[-11 - back:-1 - back], grow_list_of_10) > 0
    #              #  output += ("%.2f" % temp) + " " + temp2 + " "
    #              if ticker == "UVXY":
    #                  top += " " + time[-1 - back] + " |"
    #                  mid += ":---:|"
    #                  bold = "**" if temp > 0 and temp2 else ""
    #                  bottom2 += " " + bold + parantheses(temp) + bold
    #                  if not temp2:
    #                      bottom2 += "f"
    #                  bottom2 += " |"
    #                  temp3 = corr(l[-11 - back:-1 - back],
    #                               vix[-11 - back:-1 - back])
    #                  bold = "**" if temp3 < 0.5 else ""
    #                  bottom3 += " " + bold + parantheses(temp3) + bold + " |"
    #              else:
    #                  bold = "**" if temp > 0 and temp2 else ""
    #                  bottom1 += " " + bold + parantheses(temp) + bold
    #                  if not temp2:
    #                      bottom1 += "f"
    #                  bottom1 += " |"
    #
    #          #  output += "\n"
    #      output += top + "\n" + mid + "\n" + bottom1 + \
    #          "\n" + bottom2 + "\n" + bottom3 + "\n"
    #  return output


if __name__ == '__main__':
    print(speed_stat(show_stat_only=False))
    #  print(volume_change(tickers="^SPX SPY"))
    #  correlation_vix_uvxy(spans=(('1mo', "1d"),))
    #  print(correlation_vix_uvxy())
    #  vix_uvxy_ratio()
    #  print(question_gen())
    pass
