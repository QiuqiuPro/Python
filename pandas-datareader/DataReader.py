import pandas_datareader.data as web
# https://pandas-datareader.readthedocs.io/en/latest/remote_data.html
from datetime import datetime

end = datetime.now()
start = datetime(end.year - 1, end.month, end.day)
nikkei = web.DataReader('^N225', 'yahoo', start, end)

print(nikkei.head()) # .head()は頭の数行だけ選択するということか。
# print(nikkei)
