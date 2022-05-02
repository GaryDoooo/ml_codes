import datetime
from next_day_ex import dividend_by_date as dbd
from dividend_ranking import print_by_date


def print_6day_list():
    #  (y, m, d) = get_today_fron_cin()
    date = datetime.datetime.today()
    count = 0
    while True:
        dividend_list = dbd(date.year, date.month, date.day)
        if dividend_list is not None:
            count += 1
            if count == 4:
                break
        #  (y, m, d) = get_yesterday(y, m, d)
        date += datetime.timedelta(days=-1)

    for i in range(6):
        date = print_by_date(date)


if __name__ == '__main__':
    print_6day_list()
