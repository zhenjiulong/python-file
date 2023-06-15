import pandas as pd
import numpy as np
# obj = pd.Series(range(3), index=['a', 'b', 'c'])
# index = obj.index
# print(index[1:])
# #重新索引
# data=pd.Series([4.5, 7.2, -5.3, 3.6], index=['d', 'b', 'a', 'c'])
# data2=data.reindex(list('abcde'))
# print(data2)
# obj3 = pd.Series(['blue', 'purple', 'yellow'], index=[0, 2, 4])
# obj3=obj3.reindex(range(6), method='ffill')
# print(obj3)
data = pd.DataFrame(np.arange(16).reshape((4, 4)),
index=['Ohio', 'Colorado', 'Utah', 'New York'],
 columns=['one', 'two', 'three', 'four'])
print(data.iloc[:, :3])