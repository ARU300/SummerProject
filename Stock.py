# import pandas
# from pandas import Series, DataFrame
import pandas_datareader.data as web
import matplotlib.pyplot as plt
import datetime
import dateutil.relativedelta


def getStock(companyName, month=12, window=15):
    # set date for data retrieval
    end = datetime.date.today()
    start = end - dateutil.relativedelta.relativedelta(months=int(month))

    # retrieve data from 'yahoo', type = 'Adj Close'
    df = web.DataReader(companyName, 'yahoo', start, end)['Adj Close']
    type(df)
    df.head()
    mavg = df.rolling(window=window).mean()
    # label and plot chart
    df.plot(label=companyName)
    end -= dateutil.relativedelta.relativedelta(months=int(month))

    mavg.plot(label='mavg')
    plt.ylabel('Price')
    plt.xlabel('Year')
    plt.legend()
    plt.show()
    return mavg, companyName

# Mean Reversions - Using that knowledge to recognise that if it is predicted to go up it will also go back down
# Unsupervised Learning
# PSO, LS-SVM, ANN LM,
