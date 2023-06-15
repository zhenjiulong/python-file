import pandas as pd
import numpy as np
obj = pd.Series([4, 7, -5, 3])
print(obj)
#Series的字符串表现形式为：索引在左边，值在右边。由于我们没有为数据指定索引，于是会自动
#创建一个0到N-1（N为数据的长度）的整数型索引。
# print(obj.values)
# print(obj.index) # like range(4)
#重塑索引
obj2 = pd.Series([4, 7, -5, 3], index=list('bdac'))
print(obj2.index)
print(np.exp(obj2))

#如果数据被存放在一个Python字典中，也可以直接通过这个字典来创建Series：
sdata = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}
obj3=pd.Series(sdata)
states = ['California', 'Ohio', 'Oregon', 'Texas']
obj4=pd.Series(sdata,index=states)
print(obj4)
pd.isnull(obj4)
#Series的索引可以通过赋值的方式就地修改
obj4.index = ['Bob', 'Steve', 'Jeff', 'Ryan']
print(obj4)

