#!/usr/bin/env python
# coding: utf-8

# In[1]:


import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web
import pickle                                                                


# In[2]:


df = pickle.load(open("MMM.p", "rb"))                                        
                                                                             
print df.head()


# In[ ]:


# Calculate moving average lines
df['100ma']=df['Adj Close'].rolling(window=100,min_periods=0).mean()
df['5ma']=df['Adj Close'].rolling(window=5,min_periods=0).mean()
df['10ma']=df['Adj Close'].rolling(window=10,min_periods=0).mean()
df['20ma']=df['Adj Close'].rolling(window=20,min_periods=0).mean()
df['50ma']=df['Adj Close'].rolling(window=50,min_periods=0).mean()


# In[ ]:


print df['10ma'].head()


# In[49]:


import bz2
with bz2.BZ2File("data/SPY.p.bz2", "r") as pfile_handle:
    data = pickle.load(pfile_handle)

    #data_set = read_data("data/spy.p.bz2")
print(data.shape)
print(data)


# In[50]:


data.index
data.columns
data.dtypes


# In[51]:


data.info


# In[52]:


data[["2018-12-06" in _ for _ in data.index]]


# In[48]:


d=data[["2018-12-06" in _ for _ in data.index]]['4. close']


# In[54]:


date_set=set()
for i in data.index:
    date_set.add(str(i).split()[0])
print(sorted(list(date_set)))


# In[ ]:


len(date_set)


# In[53]:


type(data.index)


# In[56]:


from datetime import date
dd=date.fromisoformat('2020-12-04')
# datetime.date(2019, 12, 4)

data[data.index.date==dd]


# In[65]:


for i in list(data['4. close'].index):
    print(type(i))


# In[66]:


time_list=[str(_) for _ in data.index]


# In[67]:


len(time_list)


# In[70]:


data[[ _ >= '2020-10-01 09:30' and _<='2020-10-01 16:00' for _ in time_list]]


# In[ ]:




