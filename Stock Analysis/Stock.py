# import pandas
# from pandas import Series, DataFrame
import pandas_datareader.data as web
import matplotlib.pyplot as plt
import datetime
import dateutil.relativedelta


def getStock(companyName, month=12, window=15, plot=False, end=datetime.date.today(), mavgPlot=True):
    # set date for data retrieval
    start = end - dateutil.relativedelta.relativedelta(months=int(month))

    # retrieve data from 'yahoo', type = 'Adj Close'
    df = web.DataReader(companyName, 'yahoo', start, end)['Adj Close']
    type(df)
    df.tail()
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

# getStock(companyName='AAPL')

# Mean Reversions - Using that knowledge to recognise that if it is predicted to go up it will also go back down
# Unsupervised Learning
# PSO, LS-SVM, ANN LM,
