#1
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#2
df = pd.read_csv('stock_data.csv', parse_dates=True, index_col="Date")
df.head()

#3
df.drop(columns="Unamed: 0")

#4
df['volume'].plot()

#5
df.plot(subplots=True, figsize=(4,4))

#6
df.Low.diff(2).plot(figsize=(6,6,))

#7
df.High.diff(2).plot(figsize=(10,6,))

#8
window_size = 50
rolling_mean = df['Open'].rolling(window_size).mean()
rolling_mean.plot()

#9
df['Change'] = df.Close.div(df.Close.shift())
df['Change'].plot(figsize=(10,8), fontsize=16)

#10
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv('stock_data.csv', parse_dates=True, index_col="Date")
df.drop(columns="Unamed: 0", inplace=True)

df['Date'] = pd.to_datetime(df['Date'])

df['Year'] = df['Date'].dt.year

sns.boxplot(x='Year', y='Open')
