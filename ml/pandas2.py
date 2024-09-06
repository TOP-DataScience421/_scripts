from pandas import DataFrame

from pprint import pprint


numbers = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
ndf = DataFrame(numbers)

# >>> ndf
   # 0   1   2   3
# 0  1   2   3   4
# 1  5   6   7   8
# 2  9  10  11  12
# >>>
# >>> ndf[0]
# 0    1
# 1    5
# 2    9
# Name: 0, dtype: int64
# >>>
# >>> ndf[1]
# 0     2
# 1     6
# 2    10
# Name: 1, dtype: int64


# >>> ndf.columns
# RangeIndex(start=0, stop=4, step=1)
# >>>
# >>> ndf.index
# RangeIndex(start=0, stop=3, step=1)


ndf.columns = ['col1', 'col2', 'col3', 'col4']

# >>> ndf
#    col1  col2  col3  col4
# 0     1     2     3     4
# 1     5     6     7     8
# 2     9    10    11    12
# >>>

ndf.index = ['row1', 'row2', 'row3']

# >>> ndf
#       col1  col2  col3  col4
# row1     1     2     3     4
# row2     5     6     7     8
# row3     9    10    11    12
# >>>
# >>> ndf['col1']
# row1    1
# row2    5
# row3    9
# Name: col1, dtype: int64
# >>>
# >>> ndf.loc['row1']
# col1    1
# col2    2
# col3    3
# col4    4
# Name: row1, dtype: int64
# >>>
# >>> ndf.loc['row2':'row3', 'col2':'col3']
#       col2  col3
# row2     6     7
# row3    10    11


# >>> ndf.to_dict()
# {0: {0: 1, 1: 5, 2: 9}, 1: {0: 2, 1: 6, 2: 10}, 2: {0: 3, 1: 7, 2: 11}, 3: {0: 4, 1: 8, 2: 12}}
# >>>
# >>> ndf.to_numpy()
# array([[ 1,  2,  3,  4],
#        [ 5,  6,  7,  8],
#        [ 9, 10, 11, 12]])
# >>>
# >>> ndf.to_csv()
# ',0,1,2,3\r\n0,1,2,3,4\r\n1,5,6,7,8\r\n2,9,10,11,12\r\n'


# >>> ndf.info()
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 3 entries, 0 to 2
# Data columns (total 4 columns):
#  #   Column  Non-Null Count  Dtype
# ---  ------  --------------  -----
#  0   col1    3 non-null      int64
#  1   col2    3 non-null      int64
#  2   col3    3 non-null      int64
#  3   col4    3 non-null      int64
# dtypes: int64(4)
# memory usage: 228.0 bytes

