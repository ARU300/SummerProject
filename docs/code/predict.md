# Predict

## Imports


```python
try:
    from StockAnalysis.Stock import *
except:
    from Stock import *
import pandas_datareader.data as web
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import datetime
import dateutil.relativedelta
import quandl
from sklearn.svm import SVR
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import numpy as np
```
These are the current imports used in this file.

**As said before:** If you use the **Published PyPi Package**, the requirements will be downloaded automatically.

The first line reads:

```python
try:
    from StockAnalysis.Stock import *
except:
    from Stock import *
```
as depending on the location of the`__main__` file, the import name can change. In future dev, this may be changed to:

```python
if __name__ == '__main__':
    from Stock import *
else:
    from StockAnalysis.Stock import *
```
as this would also fix the problem and would not catch **all errors** which could present larger problems or unmissed problems in the future.

```python
matplotlib.use('Agg')
```

This is done in order to make the plot usable in the API. `# Comment` this line if you do not wish to use this. In future updates this will also be made more **packaging** friendly.

## Code

```python
def stockPredict(future: bool = False, companyName: str = 'AAPL', SVM: bool = True, LR: bool = True, LSTM: bool = True,
                 plot_getStock: bool = False, plot_stockPredict: bool = False, month: int = 12, test_size: int = 0.2,
                 svr_C: int = 1e3, svr_gamma: int = 0.1, confidence_test: bool = True):
    
    today = datetime.date.today()
    if not future:
        end = today - dateutil.relativedelta.relativedelta(days=30)
        df, mavg, start = getStock(companyName=companyName, month=month, plot=plot_getStock, end=end)
    elif future:
        end = today
        df, mavg, start = getStock(companyName=companyName, month=month, plot=plot_getStock)
    pred_num = 60

    x = 0
    dayslist = []
    while x != pred_num:
        day = end + dateutil.relativedelta.relativedelta(days=x)
        dayslist.append(day)
        x += 1

    dates = np.array(dayslist)
    prediction_out = pred_num

    df['Prediction'] = df.shift(-prediction_out)
    #print(df.tail())

    x = np.array(df.drop(['Prediction']))
    y = np.array(df["Prediction"])
    x = x[:-prediction_out]
    y = y[:-prediction_out]

    x = x.reshape(-1, 1)
    #y = y.reshape(-1, 1)

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=test_size)
    x_test = np.resize(x_test, x_test.size - 1)
    y_test = np.resize(y_test, y_test.size - 1)

    x_forecast = np.array(df.drop(['Prediction']))[-prediction_out:]
    x_forecast = x_forecast.reshape(-1, 1)
```
These lines are used to set up the model. We first set up the `datetime` module and utilise the functions in [`stock.py`](https://aru300.gitbook.io/summer-project/code/getstock)

I shall not be going into detail in the Machine Learning Algorithms as they are a major part of the project and require a **firm** understanding of Neural Networks before being explained. The code can be found [here.](https://github.com/ARU300/SummerProject/blob/master/StockAnalysis/Predict.py) If you have any issues feel free to may an `Issue Request`.

## Future Development

We will iron out **major** and **minor** bugs in the Models as well as try and make it run **faster** and more seamlessly. The `LSTM` model can take a while to load due to the larger computational power + the number of `Epochs` used to make the function reliable and decrease _loss_.

We would also need to make sure our **arrays** are in the correct shape to decrease constant:
```python
arr = arr.reshape(-1, 1, 2)
```
which could lead to errors and have major effects on the accuracy of the `ML` models.
