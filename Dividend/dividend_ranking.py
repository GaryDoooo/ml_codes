import sys
import datetime
from next_day_ex import dividend_by_date as dbd
#  from read_by_yf import read_current_price as rcp
from read_by_yf import adj_close_by_list as ACbL


def get_today_fron_cin():
    for line in sys.stdin:
        if len(line) > 0:
            [month, day, year, hour, minute] = line.split('-')
            break
        #  print("readline: ", line)
    year = int(year)
    month = int(month)
    day = int(day)
    hour = int(hour)
    minute = int(minute)
    #  print(year, month, day)
    return (year, month, day, hour, minute)


def get_tomorrow(year, month, day):
    gDate = datetime.datetime(year, month, day)
    #  print("Given date is: ", gDate)
    tmw = gDate + datetime.timedelta(days=1)
    #  print("Next date will be : ", tmw)
    return (tmw.year, tmw.month, tmw.day)


def read_and_sort_div_list_by_date(date):
    while True:
        #  (y, m, d) = get_tomorrow(y, m, d)
        date += datetime.timedelta(days=1)
        dividend_list = dbd(date.year, date.month, date.day)
        if dividend_list is not None:
            break

    new_list = []
    ticker_list = [_['symbol'] for _ in dividend_list]
    #  for stock in dividend_list:
    #      ticker_list.append(stock['symbol'])
    today = datetime.datetime.today()
    back_7days = today + datetime.timedelta(days=-7)
    fwd_7days = today + datetime.timedelta(days=7)
    price_list = ACbL(ticker_list,
                      str(back_7days).split()[0],
                      str(fwd_7days).split()[0])
    #  price = rcp(ticker=stock['symbol'])
    for stock in dividend_list:
        try:
            stock['price'] = price_list[stock['symbol']]
            stock['dividend_Rate'] = float(stock['dividend_Rate'])
            stock['rate'] = stock['dividend_Rate'] * \
                100 / stock['price']
            print(
                stock['symbol'],
                stock['dividend_Rate'],
                stock['price'])
            new_list.append(stock)
        except BaseException:
            pass

    new_list.sort(
        key=lambda x: x['rate'],
        reverse=True)
    return new_list, date


#  def print_by_date(y, m, d, h, minute):
def print_by_date(date):
    #  print("##### Updated at", date)
    dlist, date = read_and_sort_div_list_by_date(date)
    #  print("OUTPUT")
    print("### %d-%02d-%02d " % (date.year, date.month, date.day))
    print("| Ticker | Rate% | Dividend | Price | ex-date | record | Full name |")
    print("|:---:|:---:|:---:|:---:|:---:|:---:|:---:|")
    for stock in dlist:
        print(
            "|",
            stock['symbol'],
            "|",
            "%.2f" %
            stock['rate'],
            "|",
            "%.2f" %
            stock['dividend_Rate'],
            "|",
            "%.2f" %
            stock['price'],
            "|",
            stock['dividend_Ex_Date'],
            "|",
            stock['record_Date'],
            "|",
            stock['companyName'],
            "|")
    return date


def print_today_list():
    #  (y, m, d, h, minute) = get_today_fron_cin()
    date = datetime.datetime.today()
    print_by_date(date)


if __name__ == '__main__':
    print_today_list()
