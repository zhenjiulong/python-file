import pandas as pd
import numpy as np
# path=r"C:\Users\宇智波纱雾\Desktop\python practice\pandas教程\课件026\分组聚合.xlsx"
# data=pd.read_excel(path)
# data1=data.groupby(['城市','区'])[['人数','金额']].sum()
# print(data1)

# path=r"C:\Users\宇智波纱雾\Desktop\python practice\pandas教程\课件026\分组聚合2.xlsx"
# data=pd.read_excel(path,index_col='店号')
# dic={'1月':sum,'2月':min,'3月':'count','4月':max}
# dic2={'1月':'一季度','2月':'一季度','3月':'一季度','4月':'二季度'}
# data2=data.groupby('店号').agg(dic)
# data3=data.groupby(dic2,axis=1)
# print(data2)
# print(data3.sum())

# path=r"C:\Users\宇智波纱雾\Desktop\python practice\pandas教程\课件026\分组聚合3.xlsx"
# data=pd.read_excel(path)
# data2=data.groupby(['班级','性别']).sum()
# print(data2)

#创建series
# data=pd.Series(['甄久龙','男','22岁','喜欢sun'],index=list('abcd'))
# print(data)


# path=r"C:\Users\宇智波纱雾\Desktop\python practice\pandas教程\课件027\分组.xlsx"
# data=pd.read_excel(path)
# data['序号']=range(1,11)
# data.set_index('序号',inplace=True)
# for i in data.index:
#    data['序号']=i+1
# print(data)
# for i in data.index:
#    data['序号'].at[i]=i+1
# data2=data.groupby(data['姓名'].str[0])[['数学','语文','英语']]
# data3=data.groupby([data['时间'].dt.year,data['时间'].dt.month])[['数学','语文','英语']].sum()
# print(data3)
# print(data2.sum())
#
# df1 = pd.DataFrame({'key': ['b', 'b', 'a', 'c', 'a', 'a', 'b'],
# 'data1': range(7)})
# df2 = pd.DataFrame({'key': ['a', 'b', 'd','a'],
# 'data2': range(4)})
# print(pd.merge(df1, df2, on='key'))

data = pd.DataFrame({'a':[1,2,3],'b':[4,5,6],'c':[7,8,9]})
data.index=list('abc')
data.columns=[0,1,2]
print(data)
print(data[0])

