import datetime as dt
#  import matplotlib.pyplot as plt
from matplotlib import style
#  import pandas as pd
import pandas_datareader.data as web
import pickle

style.use("ggplot")

start = dt.datetime(1970, 1, 1)
end = dt.datetime(2017, 8, 16)

df = web.DataReader("NCLH", "yahoo", start, end)
print df.head()

pickle.dump(df, open("NCLH.p", "wb"), protocol=0)
