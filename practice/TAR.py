import pandas as pd
import numpy as np
import statsmodels
from statsmodels.tsa.ar_model import AutoReg

# 读取CSV文件，假设待预测列为'col1'
df = pd.read_excel(r'C:\Users\宇智波纱雾\Desktop\python practice\1.xlsx',header=None)
df.columns = ['col1']
data = df['col1'].values

# 定义阈值和滞后期
threshold =620
lag = 12

# 训练门限自回归模型
train_data = data[:672]
test_data = data[672:]
model = AutoReg(train_data, lags=lag, trend='c')
res = model.fit()

# 预测剩余数据
preds = []
for i in range(len(test_data)):
    if i == 0:
        preds.append(test_data[i])
    else:
        if preds[i-1] > threshold:
            pred = res.predict(start=len(train_data)+i-lag, end=len(train_data)+i-1, dynamic=False)[-1]
            preds.append(pred)
        else:
            preds.append(test_data[i])

# 计算预测误差
mse = np.mean((preds - test_data)**2)
print("Mean Squared Error: ", mse)