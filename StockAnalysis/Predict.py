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

    #if not future:
    #    dfActual, mavgActual, startActual = getStock(companyName=companyName, month=month, plot=plot_getStock,
    #                                                 end=today, mavgPlot=False)
        #print('ACTUAL: ')
        #print(dfActual)

    if LR:
        lr = LinearRegression()
        lr.fit(x_train, y_train)

        lr_prediction = lr.predict(x_forecast)
        #print('LR Prediction')
        #print(lr_prediction)

        if plot_stockPredict:
            multi = df[-2] / lr_prediction[0]
            x = 0
            for i in lr_prediction:
                lr_prediction[x] = i * multi
                x += 1
            plt.plot(dates, lr_prediction)
            plt.title('Linear Regression')
            plt.show()

        if confidence_test:
            lr_confidence = lr.score(x_test, y_test)
            #print("lr confidence: ", lr_confidence)
            dates = dates.tolist()
            lr_prediction = lr_prediction.tolist()
            return lr_confidence, lr_prediction, dates

        dates = dates.tolist()
        lr_prediction = lr_prediction.tolist()
        return lr_prediction, dates

    if SVM:
        svr_rbf = SVR(kernel='rbf', C=svr_C, gamma=svr_gamma)
        svr_rbf.fit(x_train, y_train)
        svm_prediction = svr_rbf.predict(x_forecast)
        #print('SVM Prediction')
        #print(svm_prediction)


        if plot_stockPredict:
            multi = df[-2] / svm_prediction[0]
            x = 0
            for i in svm_prediction:
                svm_prediction[x] = i * multi
                x += 1
            plt.plot(dates, svm_prediction)
            plt.title('Support Vector Regression')
            plt.show()

        if confidence_test:
            svm_confidence = svr_rbf.score(x_test, y_test)
            #print('SVM confidence is {}.'.format(svm_confidence))
            dates = dates.tolist()
            svm_prediction = svm_prediction.tolist()
            return svm_confidence, svm_prediction, dates

        dates = dates.tolist()
        svm_prediction = svm_prediction.tolist()
        return svm_prediction, dates

    if LSTM:
        from keras.models import Sequential, load_model
        from keras.layers import Dense
        from keras.layers import LSTM
        from keras.layers import Dropout
        x = 1
        if x == 0:
            x_train = np.asarray(x_train).astype(np.float32)
            y_train = np.asarray(y_train).astype(np.float32)
            #x_forecast = np.asarray(x_forecast).astype(np.float32)
            x_train = x_train.reshape(-1, 1, 2)
            y_train = y_train.reshape(-1, 1, 2)
            x_forecast = x_forecast.reshape(-1, 1, 2)
            model = Sequential()
            model.add(LSTM(50, input_shape=(x_train.shape[1], x_train.shape[2])))
            model.add(Dropout(0.2))
            model.add(Dense(1))
            model.compile(loss='mae', optimizer='adam')
            model.fit(x_train, y_train, epochs=100, batch_size=70, verbose=1)
            LSTM_prediction = model.predict(x_forecast)
            print(LSTM_prediction)
        elif x == 1:
            x_train = x_train.reshape(-1, 1, 2)
            y_train = y_train.reshape(-1, 1, 2)
            x_test = x_test.reshape(-1, 1, 2)
            y_test = y_test.reshape(-1, 1, 2)
            #print('\n\n\n' + str(x_train.shape) + '\n\n\n' + str(y_train.shape) + '\n\n\n')
            #print(x_forecast.shape)
            x_forecast = x_forecast.reshape(-1, 1, 2)
            x_train = np.asarray(x_train).astype(np.float32)
            y_train = np.asarray(y_train).astype(np.float32)
            x_forecast = np.asarray(x_forecast).astype(np.float32)
            x_test = np.asarray(x_test).astype(np.float32)
            y_test = np.asarray(y_test).astype(np.float32)
            #from keras import backend as K
            #x_test = K.cast_to_floatx(x_test)
            #y_test = K.cast_to_floatx(y_test)
            #x_forecast = K.cast_to_floatx(x_forecast)
            look_back = int(month * 30)
            forward_days = 2
            num_periods = month

            #NUM_NEURONS_FirstLayer = 128
            #NUM_NEURONS_SecondLayer = 64
            EPOCHS = 200
            #Build the model
            LSTM_model = Sequential()
            LSTM_model.add(LSTM(256, batch_input_shape=(None, 1, 2), return_sequences=True))
            LSTM_model.add(Dropout(0.2))
            #LSTM_model.add(LSTM(256, batch_input_shape=(None, 1, 2), return_sequences=True))
            #LSTM_model.add(Dropout(0.2))
            #LSTM_model.add(LSTM(128, batch_input_shape=(None, 1, 2), return_sequences=True))
            #LSTM_model.add(Dropout(0.2))
            #LSTM_model.add(LSTM(64))
            #LSTM_model.add(Dropout(0.2))
            LSTM_model.add(Dense(1))
            LSTM_model.compile(loss='mae', optimizer='adam', metrics=['accuracy'])
            LSTM_model.fit(x_train, y_train, epochs=EPOCHS, verbose=1, batch_size=32, validation_data=(x_test, y_test), validation_freq = 1)
            LSTM_prediction = LSTM_model.predict(x_forecast)
        
        if plot_stockPredict:
            import tensorflow as tf
            LSTM_prediction = tf.reshape(LSTM_prediction, [30, -1])
            print(f'\n\n\n{LSTM_prediction.get_shape()}\n\n\n')
            #LSTM_prediction = LSTM_prediction.tolist()
            LSTM_prediction = np.asarray(LSTM_prediction).astype(np.float32)
            dates = dates.reshape(30, -1)
            x = 0
            print(LSTM_prediction[0])
            print(df[-2])
            multi = df[-2] / LSTM_prediction[0]
            print(multi)
            for i in LSTM_prediction:
                LSTM_prediction[x] = i * multi
                x += 1
            plt.plot(dates, LSTM_prediction)
            plt.title('LSTM')
            plt.show()

        if confidence_test:
            LSTM_confidence = LSTM_model.evaluate(x_test, y_test, verbose = 0)
            print('LSTM confidence is {}.'.format(LSTM_confidence[1]))
            dates = dates.tolist()
            LSTM_prediction = LSTM_prediction.tolist()
            return LSTM_confidence[1], LSTM_prediction, dates

        dates = dates.tolist()
        LSTM_prediction = LSTM_prediction.reshape(-1)
        LSTM_prediction = LSTM_prediction.tolist()
        return LSTM_prediction, dates
        
if __name__ == "__main__":
    LSTM_prediction, dates = stockPredict(future=True, companyName='AAPL', month = 24, SVM=False, LR=False, LSTM=True, confidence_test=False, plot_stockPredict=True)

# TODO: Add iteration to find best settings with highest confidence rating
