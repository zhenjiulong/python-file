#定义外层变量
# i = 1
# while i <= 9:
#     j = 1
#     while j <= i:
#         print(f"{j}*{i}={j*i}\t",end='')
#         #内层循环不换行
#         j += 1
#     i += 1
#     print()#打印空格为换行
# i = 1
for i in range(1,10):
    # j = 1
    for j in range(1,i+1):
        print(f"{j}*{i}={j*i}\t",end='')
    print()



