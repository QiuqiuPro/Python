# http://matplotlib.org/api/finance_api.html

# データを準備
import pandas_datareader.data as web
from datetime import datetime
end = datetime.now()
start = datetime(end.year - 1, end.month, end.day)
nikkei = web.DataReader('^N225', 'yahoo', start, end)
print(nikkei.head()[['Open','High','Low','Close']])#[['Open','High','Low','Close']]で列を選択
# nikkei_ohlc = nikkei[['Open','High','Low','Close']]
# nikkei_tohlc = nikkei[['Open','High','Low','Close']]
# nikkei_tohlc['t'] = nikkei_ohlc.index

########
import numpy as np
import pandas as pd
idx = pd.date_range('2016/06/01', '2016/07/31 23:59', freq='T')
dn = np.random.randint(2, size=len(idx))*2-1
rnd_walk = np.cumprod(np.exp(dn*0.0002))*100
df = pd.Series(rnd_walk, index=idx).resample('B').ohlc()
df.plot()
import matplotlib.pyplot as plt
import matplotlib.finance as mpf
from matplotlib.dates import date2num

fig = plt.figure()
ax = plt.subplot()

xdate = [x.date() for x in df.index] #Timestamp -> datetime
ohlc = np.vstack((date2num(xdate), df.values.T)).T #datetime -> float
mpf.candlestick_ohlc(ax, ohlc, width=0.7, colorup='g', colordown='r')

ax.grid() #グリッド表示
ax.set_xlim(df.index[0].date(), df.index[-1].date()) #x軸の範囲
fig.autofmt_xdate() #x軸のオートフォーマット
plt.show()

# 営業日のみにする
fig = plt.figure()
ax = plt.subplot()

ohlc = np.vstack((range(len(df)), df.values.T)).T #x軸データを整数に
mpf.candlestick_ohlc(ax, ohlc, width=0.7, colorup='g', colordown='r')

xtick0 = (5-df.index[0].weekday())%5 #最初の月曜日のインデックス
plt.xticks(range(xtick0,len(df),5), [x.strftime('%Y-%m-%d') for x in df.index][xtick0::5])
ax.grid() #グリッド表示
ax.set_xlim(-1, len(df)) #x軸の範囲
fig.autofmt_xdate() #x軸のオートフォーマット
########

# # ローソク足
# # http://qiita.com/toyolab/items/1b5d11b5d376bd542022
# import matplotlib.pyplot as plt
# import matplotlib.finance as mpf # The finance module has been deprecated in mpl 2.0 and will be removed in mpl 2.2. Please use the module mpl_finance instead.
# from matplotlib.dates import date2num
#
# fig = plt.figure()
# ax = plt.subplot()
# mpf.candlestick_ohlc(ax, nikkei_ohlc['Open'], nikkei_ohlc['High'], nikkei_ohlc['Low'], nikkei_ohlc['Close'])
# # mpf.candlestick_ohlc(ax, nikkei_ohlc)
# plt.show()
