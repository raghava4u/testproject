#%%
import os
from tvDatafeed import TvDatafeed, Interval
import datetime as dt
import ta
import matplotlib.pyplot as pl
#%%
username = 'raghava4u'
password = 'G00dB00y123'
tv=TvDatafeed(username=username, password=password, chromedriver_path='/Users/d068390/.tv_datafeed/chromedriver')
# %%
# ticker = 'BANKNIFTY'
# ohlc_data = tv.get_hist(
#     ticker, 'NSE', Interval.in_30_minute, n_bars=50, fut_contract=1)
# ohlc_data = ohlc_data[(ohlc_data.index.date > ohlc_data.index.date[0]) & (
#     ohlc_data.index.time >= dt.time(5, 45)) & (ohlc_data.index.time <= dt.time(12, 00))]

#%%
def fetchOHLC(ticker, interval=15, bars=1000):
    ticker=ticker
    n_bars=bars
    print(ticker)
    ohlc_data = tv.get_hist(
        ticker, 'NSE', Interval.in_5_minute, bars, fut_contract=1)
    ohlc_data = ohlc_data[(ohlc_data.index.date > ohlc_data.index.date[0])]
     # & (ohlc_data.index.time >= dt.time(5, 00)) & (ohlc_data.index.time <= dt.time(16, 00))]
    return ohlc_data

ohlc_data1=fetchOHLC('BANKNIFTY')

# %%
def macd1(DF, a, b, c):
    df = DF.copy()
    df["MA_Fast"]=df["close"].rolling(a).mean()
    df["MA_Slow"]=df["close"].rolling(b).mean() 
    df["MACD"]=df["MA_Fast"]-df["MA_Slow"]
    df["Signal"]=df["MACD"].rolling(c).mean()
    df.dropna(inplace=True)
    return df


macd1(ohlc_data1, 12,26,9)

#%%
ohlc_data1 = ta.utils.dropna(ohlc_data1)
df= ohlc_data1
# %%
df = ta.add_all_ta_features(
    df, open="open", high="high", low="low", close="close", volume="volume", fillna=True)
# %%
vdf= ohlc_data1
# %%
vdf= ta.add_volume_ta(vdf, high="high", low="low", close="close", volume="volume", fillna=True)
# %%
