#1
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose

airline = pd.read_csv('airPassengers.csv', index_col='Month', parse_dates=True)
airline.head()

result = seasonal_decompose(airline['Passengers'], model='multiplicative')

result.plot();

#2
from pmdarima import auto_arima

import warnings
warnings.filterwarnings('ignore')

stepwise_fit = auto_arima(airline['Passengers'],    start_p=1,start_q=1,
                                                    max_p=3,max_q=3,m=12,
                                                    start_p=0,seasonal=True,
                                                    d=None,D=1,trace=True,
                                                    error_action='ignore',
                                                    suppress_warnings=True,
                                                    stepwise=True)
stepwise_fit.summary()

#3
train = airline.iloc[:len(airline)-12]
test = airline.iloc[len(airline)-12:]

from statsmodels.tsa.statespace.sarimax import SARIMAX

model = SARIMAX(train['Passengers'], order=(0,1,1), seasonal_order=(2,1,1,12))
results = model.fit()
results.summary()

#4
start=len(train)
end=len(train)+len(test)-1

predictions = results.predict(start, end, typ='levels').rename('Predictions')
predictions.plot(legend=True)
test['Passengers'].plot(legend=True)

#5
from sklearn.metrics import mean_squared_error
from statsmodels.tools.eval_measures import rmse

rmse(test['Passengers'], predictions)

mean_squared_error(test['Passengers'], predictions)

#6
model = model = SARIMAX(airline['Passengers'], order=(0,1,1), seasonal_order=(2,1,1,12))
result = model.fit()
forecast = result.predict(start = len(airline), end= (len(airline)-1)+3*12, typ='levels').rename('Forecast')

airline['Passengers'].plot(figsize=(12,5), legend=True)
forecast.plot(legend=True)