from Stock import *
import pandas_datareader.data as web
import matplotlib.pyplot as plt
import datetime
import dateutil.relativedelta
import quandl
from sklearn.svm import SVR
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import numpy as np

x = 0
today = datetime.date.today()
end = today - dateutil.relativedelta.relativedelta(days=x)
df, mavg, start = getStock(companyName='AAPL', month=36, plot=True, end=end)
pred_num = 30

dayslist = []
while x != pred_num:
    day = end + dateutil.relativedelta.relativedelta(days=x)
    dayslist.append(day)
    x += 1

dates = np.array(dayslist)
prediction_out = pred_num

df['Prediction'] = df.shift(-prediction_out)
print(df.tail())

x = np.array(df.drop(['Prediction']))
y = np.array(df["Prediction"])
x = x[:-prediction_out]
y = y[:-prediction_out]

x = x.reshape(-1, 1)
y = y.reshape(-1, 1)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.1)

svm_rbf = SVR(kernel='rbf', C=1e3, gamma=0.1)
svm_rbf.fit(x_train, y_train)

svm_confidence = svm_rbf.score(x_test, y_test)
print('SVM confidence is {}.'.format(svm_confidence))

x_forecast = np.array(df.drop(['Prediction']))[-prediction_out:]
print('PREDICTION: ')
print(x_forecast)

dfActual, mavgActual, startActual = getStock(companyName='AAPL', month=1, plot=True, end=today, mavgPlot=False)
print('ACTUAL: ')
print(dfActual)

plt.plot(dates, x_forecast)
plt.show()


# TODO: Add iteration to find best settings with highest confidence rating
