#  import pandas
import requests
import datetime
#  import calendar


def dividend_by_date(year, month, day):
    #  calendars = []
    url = 'https://api.nasdaq.com/api/calendar/dividends'
    hdrs = {'Accept': 'application/json, text/plain, */*',
            'DNT': "1",
            'Origin': 'https://www.nasdaq.com/',
            'Sec-Fetch-Mode': 'cors',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0)'}

    date_obj = datetime.date(year, month, day)
    date_str = date_obj.strftime(format='%Y-%m-%d')

    params = {'date': date_str}
    page = requests.get(url, headers=hdrs, params=params)
    return page.json().get('data').get('calendar').get('rows')
#     return rows
#     return pandas.DataFrame(rows)


# concat_df = pandas.concat(
if __name__ == '__main__':
    print(dividend_by_date(2022, 5, 2))
    #  year = 2020
    #  month = 2

#  get number of days in month
#      days_in_month = calendar.monthrange(year, month)[1]
#  create calendar object
#      february = dividend_calendar(year, month)
#  define lambda function to iterate over list of days
#      def function(days): return february.calendar(days)
#
#  define list of ints between 1 and the number of days in the month
#      iterator = list(range(1, days_in_month + 1))
#  Scrape calendar for each day of the month
#      objects = list(map(function, iterator))
#  concatenate all the calendars in the class attribute
#      concat_df = pandas.concat(dividend_by_date(2022, 5, 2))
#
#  Drop any rows with missing data
#      drop_df = concat_df.dropna(how='any')
#
#  set the dataframe's row index to the company name
#      final_df = drop_df.set_index('companyName')
