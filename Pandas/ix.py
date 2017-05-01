# REPL
import pandas as pd

s = pd.Series([1, 2, 3], index = ['I1', 'I2', 'I3'])

df = pd.DataFrame( {'C1': [11, 21, 31],
                    'C2': [12, 22, 32],
                    'C3': [13, 23, 33]},
                   index = ['I1', 'I2', 'I3'] )
# >>> s
# I1    1
# I2    2
# I3    3
# dtype: int64
# >>> df
#     C1  C2  C3
# I1  11  12  13
# I2  21  22  23
# I3  31  32  33
# 参考：http://sinhrks.hatenablog.com/entry/2014/11/12/233216

# >>> s[1]
# 2
# >>> s.ix[1]
# 2
