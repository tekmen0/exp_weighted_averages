import matplotlib
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter, drange
import numpy as np
import pandas as pd
from datetime import datetime

df = df = pd.read_csv("gemini_BTCUSD_day.csv", skiprows=[0], usecols=["Date","Low","High"], index_col = "Date")

start_Date = df.index[-1]
end_Date = df.index[0]

beta = float(input("enter the beta value : "))

vals = list((df.Low + df.High)/2)[::-1]
imgs = []
v = vals[0];

for i in range(len(vals)):
    v = (beta*v)+((1-beta)*vals[i])
    imgs.append(v)

fig, ax = plt.subplots()
ax.plot(range(len(vals)), vals, color="black")
ax.plot(range(len(vals)), imgs, color="red")


ax.set(xlabel='sample_no', ylabel='value')
ax.grid()

plt.axhline(0, color='black')
plt.axvline(0, color='black')

plt.show()
