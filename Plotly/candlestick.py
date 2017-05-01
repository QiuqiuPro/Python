# ????

# import numpy as np
# import pandas as pd
#
# idx = pd.date_range('2015/01/01', '2015/12/31 23:59', freq='T')
# dn = np.random.randint(2, size=len(idx))*2-1
# rnd_walk = np.cumprod(np.exp(dn*0.0002))*100
# df = pd.Series(rnd_walk, index=idx).resample('B').ohlc()
#
# from plotly.offline import init_notebook_mode, iplot
# from plotly.tools import FigureFactory as FF
#
# init_notebook_mode(connected=True) # Jupyter notebook用設定
#
# fig = FF.create_candlestick(df.open, df.high, df.low, df.close, dates=df.index)
#
# iplot(fig)

import plotly.plotly as py
import plotly.figure_factory as FF
from datetime import datetime

import pandas_datareader.data as web

df = web.DataReader("aapl", 'yahoo', datetime(2007, 10, 1), datetime(2009, 4, 1))
fig = FF.create_candlestick(df.Open, df.High, df.Low, df.Close, dates=df.index)
py.iplot(fig)
