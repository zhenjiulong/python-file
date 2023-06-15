import pandas as pd
import numpy as np
# 建DataFrame的办法有很多，最常用的一种是直接传入一个
# 由等长列表或NumPy数组组成的字典
# data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada', 'Nevada'],
# 'year': [2000, 2001, 2002, 2001, 2002, 2003],
# 'pop': [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]}
# frame = pd.DataFrame(data)
# print(frame)
# #如果指定了列序列，则DataFrame的列就会按照指定顺序进行排列：
# frame2=pd.DataFrame(data, columns=['year', 'state', 'pop'])
# print(frame2)
# # #如果传入的列在数据中找不到，就会在结果中产生缺失值
# frame3 = pd.DataFrame(data, columns=['year', 'state', 'pop', 'debt'],
#  index=['one', 'two', 'three', 'four','five', 'six'])
# print(frame3)
# #通过类似字典标记的方式或属性的方式，可以将DataFrame的列获取为一个Series：
# print(frame2['state'])
# print(frame2.iloc[2][1])
# #将列表或数组赋值给某个列时，其长度必须跟DataFrame的长度相匹配。如果赋值的是一个
# #Series，就会精确匹配DataFrame的索引，所有的空位都将被填上缺失值：
# val = pd.Series([-1.2, -1.5, -1.7], index=['two', 'four', 'five'])
# frame3['debt'] = val
# print(frame3)
# #添加一个新的布尔值的列，state是否为'Ohio
# frame2['eastern'] = frame2.state == 'Ohio'#注意：不能用frame2.eastern创建新的列
# print(frame2)
# #del方法可以用来删除这列：
# del frame2['eastern']

# #另一种常见的数据形式是嵌套字典：
# pop = {'Nevada': {2001: 2.4, 2002: 2.9},
# 'Ohio': {2000: 1.5, 2001: 1.7, 2002: 3.6}}
# frame3 = pd.DataFrame(pop,index=[2000,2001,2002])
# #如果嵌套字典传给DataFrame，pandas就会被解释为：外层字典的键作为列，内层键则作为行索引：
# print(frame3)
# print(frame3['Ohio'][:-1])
# frame4=pd.DataFrame(pop, index=[2001, 2002, 2003])
# print(frame4)
# pdata = {'Ohio': frame3['Ohio'][:-1],
# 'Nevada': frame3['Nevada'][:2]}
# frame5=pd.DataFrame(pdata)
# print(frame5)



#给D添加一列

data2 = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), columns=['a', 'b', 'c'])
print(data2)
# data2.insert(1, 'd', [0,1,2])
#
# # data2['e','f'] = [[1,2,3],[3,2,1]]
# data2=pd.concat([data2, pd.DataFrame(columns=list('DE'))])
# print(data2)
#
#
#
test1 = pd.DataFrame([[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7]], columns=list('ABCD'))  #
print(test1)
test2 = pd.DataFrame([[8, 9, 10, 11],[9,8,7,6]],columns=list('FGhi'))
test1 = pd.concat([test1, test2],axis=1)
print(test1.fillna(0))