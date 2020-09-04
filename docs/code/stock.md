---
description: File used to retrieve stock market data.
---

# Stock

## Imports

These are the following imports used in this file:

{% tabs %}
{% tab title="Python" %}
{% code title="" %}
```python
import pandas_datareader.data as web
import matplotlib
import matplotlib.pyplot as plt
import datetime
import dateutil.relativedelta
import numpy as np
```
{% endcode %}
{% endtab %}
{% endtabs %}

{% hint style="success" %}
If you use the **Published PyPi Package**, the requirements will be downloaded automatically.
{% endhint %}

`Pandas_datareader` is used to retrieve the data from _Yahoo! Finance_.   
`Matplotlib` is used as a graphing tool and is imported as **plt** for easier usage. The `datetime` module is install in Python by default and is used for _DateTime_ objects. `Numpy` is a scientific module which gives access to _NumPy Arrays_ which are easier and more useful for handling data in comparison to _Python Lists_.

## Code

{% tabs %}
{% tab title="Python" %}
{% code title="" %}
```python
today = datetime.date.today()
def getStock(companyName: str, month: int = 1, plot: bool = False, end=today, mavgPlot: bool = False):
    # set date for data retrieval
    window = 2 * month
    start = end - dateutil.relativedelta.relativedelta(months=int(month))
    print('start: ' + str(start))
    print('end: ' + str(end))

    #try:
    # retrieve data from 'yahoo', type = 'Adj Close'
    df = web.DataReader(companyName, 'yahoo', start, end)['Adj Close']

    type(df)
    df.tail()
    df.fillna(value='', inplace=True)
    mavg = df.rolling(window=window).mean()
    # label and plot chart
    df.plot(label=companyName)
    end -= dateutil.relativedelta.relativedelta(months=int(month))

    if plot:
        if mavgPlot:
            mavg.plot(label='mavg')
        plt.ylabel('Price')
        plt.xlabel('Year')
        plt.legend()
        plt.show()
    return df, mavg, start
```
{% endcode %}
{% endtab %}
{% endtabs %}

First we define the times using `datetime` and a variable called today. Then we define the function and setup the dates using the variables set by the user. 

{% code title="Stock.py \# v2" %}
```python
def getStock(companyName: str, month: int = 1, plot: bool = False, end=today, mavgPlot: bool = False):
```
{% endcode %}

{% hint style="warning" %}
 The only required arguement for the above function is `companyName` so this must be defined when using the function.
{% endhint %}

`df` is a variable for a Pandas Dataframe. This allows us to plot and visualise the data using `plt` which is very useful in determining the results of our algorithms and seeing whether our predictions are accurate instead of reading an array of `floats`.

For testing, you can use the following line _\(which has been commented on the_ [_`file`_](https://github.com/ARU300/SummerProject/blob/master/StockAnalysis/Stock.py)_\)_

## Future Development

In the future, we may be able to integrate _different methods_ of accessing stock data within this file. For example, we could use the built-in `Requests` module to make **API requests** to servers and access data from multiple sources and therefore attain **more reliable and accurate data.**

We could also use the `re` module or make `API` requests and define regex in order to find the Stock Market name of a company via a **User Input** as names such as 'AAPL' and 'MSFT' are hard to remember and not very user-friendly.

