import pandas as pd
from pandas import Series, DataFrame
import pandas_datareader.data as web
import matplotlib.pyplot as plt
from matplotlib import style
import matplotlib as mpl
import datetime

start = datetime.datetime(2020, 1, 1)
end = datetime.date.today()

company = ['APPL', 'GE', 'GOOG', 'IBM']

df = web.DataReader(company[1], 'yahoo', start, end)['Adj Close']
type(df)
df.head()
mavg = df.rolling(window=10).mean()

df.plot(label='APPL')
mavg.plot(label='mavg')
plt.legend()
plt.show()
