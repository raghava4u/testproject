#%%
import os
from tvDatafeed import TvDatafeed, Interval
tv=TvDatafeed()
import pandas as pd
import numpy as np
import datetime as dt
import matplotlib.pyplot as plt
import mplfinance as mpf
from kiteconnect import *

username = 'raghava4u'
password = 'G00dB00y123'



tv=TvDatafeed(username=username,password=password, chromedriver_path='/Users/d068390/.tv_datafeed')
# %%

''' uncomment below to whenw orking with with kite
def instrumentLookup(instrument_df, symbol):
    """looks up instrument token for a given script from instrument dump. ( basically each token is given with a numaric number,
        everytime we send a ticker query its need to be convreted into number value"""
        try:
            return instrument_df[instrument_df.tradingsymbol == symbol].instrument_token_values[0]
        except:
            return -1

'''

'''uncomment below if you are working with kiteconnect
def kfetchOHLC(ticker, interval, duration):
    """extracts historical token for a given script from instrumewnt dump"""
    instrument= instrumentlookup(instrument_df, ticker)
    data = pd.DataFrame(kite.historical_data(
        instrument, dt.date.today()-dt.timedelta(duration)))
    data.set_index("date", inplace=True)
    return data
'''
#%%
def fetchOHLC(ticker, interval=15, type='h', bars=50):
    ticker=ticker
    n_bars=bars
    if interval.isnumeric()
    interval= 'Interval.in_{interval}_minute'
    print(ticker)
    ohlc_data = tv.get_hist(
        'ticker', 'NSE', Interval.in_30_minute, n_bars=50, fut_contract=1)
    ohlc_data = ohlc_data[(ohlc_data.index.date > ohlc_data.index.date[0]) & (
        ohlc_data.index.time >= dt.time(5, 45)) & (ohlc_data.index.time <= dt.time(12, 00))]
    return ohlc_data

ohlc_data1=fetchOHLC('RELIANCE')
#%%
def macd1(DF, a, b, c):
    df = DF.copy()
    df["MA_Fast"]=df["close"].rolling(a).mean()
    df["MA_Slow"]=df["close"].rolling(b).mean() 
    df["MACD"]=df["MA_Fast"]-df["MA_Slow"]
    df["Signal"]=df["MACD"].rolling(c).mean()
    df.dropna(inplace=True)
    return df


macd1(ohlc_data, 12,26,9)

# %%
