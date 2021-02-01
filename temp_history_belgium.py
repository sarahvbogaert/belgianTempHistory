import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import numpy as np
import seaborn as sns
sns.set()
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

# load data from 1981-2010
df_brugge_old = pd.read_csv("data/brugge_1981_2010.csv", usecols=range(2,14))
df_brugge_old.index = ["mean temp", "max temp", "min temp"]
df_brugge_old.columns = months

df_marche_old = pd.read_csv("data/marche-famennes_1981_2010.csv", usecols=range(2,14))
df_marche_old.index = ["mean temp", "max temp", "min temp"]
df_marche_old.columns = months

# load data from 2017-2021
df_recent = pd.read_csv("data/belgian_climate_2017_2021.csv")
df_recent["timestamp"] = pd.to_datetime(df_recent["timestamp"])
df_recent = df_recent.iloc[:, [1, 2, 4, 5, 6]]
df_recent.columns = ["code", "timestamp", "mean temp", "max temp", "min temp"]
df_recent["year"] = df_recent["timestamp"].dt.year
df_recent["month"] = df_recent["timestamp"].dt.month
df_recent["day"] = df_recent["timestamp"].dt.day
# column code shows at which station (Brugge or Marche-en-Famennes) the measurements were made
df_brugge_recent = df_recent[df_recent['code'] == 6418]
df_marche_recent = df_recent[df_recent['code'] == 6472]

# group measurements by month and calculate mean values (and number of measurements in column "code")
df_brugge_recent = df_brugge_recent.groupby("month").agg({"code": len, "mean temp": np.nanmean,
                                                          "max temp": np.nanmean, "min temp": np.nanmean})
df_marche_recent = df_marche_recent.groupby("month").agg({"code": len, "mean temp": np.nanmean,
                                                          "max temp": np.nanmean, "min temp": np.nanmean})
# drawing of figure
col1 = "C0"
col2 = "C1"
plt.figure(figsize=(5, 8))
plt.subplot(311)
plt.plot(months, df_brugge_old.loc["mean temp"], color=col1, linestyle="--")
plt.plot(months, df_marche_old.loc["mean temp"], color=col2, linestyle="--")
plt.plot(months, df_brugge_recent["mean temp"], color=col1, label="Brugge")
plt.plot(months, df_marche_recent["mean temp"], color=col2, label="Marche")
plt.title("Mean Temperature (°C)", fontweight="bold")
plt.legend(loc="best")
plt.subplot(312)
plt.plot(months, df_brugge_old.loc["max temp"], color=col1, linestyle="--")
plt.plot(months, df_marche_old.loc["max temp"], color=col2, linestyle="--")
plt.plot(months, df_brugge_recent["max temp"], color=col1)
plt.plot(months, df_marche_recent["max temp"], color=col2)
plt.plot([], [], color="grey", linestyle="--", label="1981-2010")
plt.plot([], [], color="grey", label="2017-2021")
plt.title("Mean Daily Max Temperature (°C)", fontweight="bold")
plt.legend(loc="best")
plt.subplot(313)
plt.plot(months, df_brugge_old.loc["min temp"], color=col1, linestyle="--")
plt.plot(months, df_marche_old.loc["min temp"], color=col2, linestyle="--")
plt.plot(months, df_brugge_recent["min temp"], color=col1)
plt.plot(months, df_marche_recent["min temp"], color=col2)
plt.title("Mean Daily Min Temperature (°C)", fontweight="bold")
plt.subplots_adjust(hspace=0.45)
txt = ("The graphs show the mean daily mean/max/min temperatures in Belgium (in Brugge, at the sea, and"
       " in Marche-en-Famennes, inland) during the two periods of 1981-2010 and 2017-2021")
plt.figtext(0.5, 0.01, txt, wrap=True, horizontalalignment='center', fontsize=9)
plt.suptitle("Temperature evolution in Belgium".upper(), fontweight="bold")
plt.savefig("TempHistoryBelgium2.png", dpi=150)
