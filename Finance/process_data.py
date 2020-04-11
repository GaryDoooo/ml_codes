# import datetime as dt
# import matplotlib.pyplot as plt
# from matplotlib import style
import pandas as pd
# import pandas_datareader.data as web
import pickle

df = pickle.load(open("MMM.p", "rb"))

# Calculate moving average lines
df['100ma'] = df['Adj Close'].rolling(window=100, min_periods=0).mean()
df['5ma'] = df['Adj Close'].rolling(window=5, min_periods=0).mean()
df['10ma'] = df['Adj Close'].rolling(window=10, min_periods=0).mean()
df['20ma'] = df['Adj Close'].rolling(window=20, min_periods=0).mean()
df['50ma'] = df['Adj Close'].rolling(window=50, min_periods=0).mean()

# adjust all the ochl data
df['adj'] = df['Close'] / df['Adj Close']
df['Open'] = df['Open'] / df['adj']
df['High'] = df['High'] / df['adj']
df['Low'] = df['Low'] / df['adj']

# Calculate MACD
df['26 ema'] = df['Adj Close'].ewm(span=26).mean()
df['12 ema'] = df['Adj Close'].ewm(span=12).mean()
df['macd'] = df['12 ema'] - df['26 ema']
df['signal'] = df['macd'].ewm(span=9).mean()
df['hist'] = df['macd'] - df['signal']

#  print df.head()
#  print "Max and Min of MACD", df['macd'].max(), df['macd'].min()
#  print df[df['macd'] > 2]

# Calculate weekly ochl
df_ohlc10D = df.resample('10D').agg({'Open': 'first',
                                     'High': 'max',
                                     'Low': 'min',
                                     'Adj Close': 'last'})
df_ohlc10D['Volume'] = df['Volume'].resample('10D').sum()

df_ohlc5D = df.resample('5D').agg({'Open': 'first',
                                   'High': 'max',
                                   'Low': 'min',
                                   'Adj Close': 'last'})
df_ohlc5D['Volume'] = df['Volume'].resample('5D').sum()

print df_ohlc5D.head(), df_ohlc10D.head()


df['day'] = pd.to_datetime(df.index)
df['day'] = df['day'] - df['day'][0]
df['day'] = df['day'].astype('timedelta64[D]')
print df.head()

fivedarray = df[['day', 'Open', 'High', 'Low', 'Adj Close']].as_matrix()

print fivedarray.shape
print fivedarray[:8, :]
