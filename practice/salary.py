import random
T=10000
for i in range(1,21):
    num = random.randint(1,10)
    if num < 5:
        print(f"员工{i}分数为{num},分数不足，不发工资，下一位")
        continue
    if T > 0:
        print(f"员工{i}分数为{num},公司余额为{T}，发工资1000元")
        T-=1000
    else:
        print("余额不足，不发了")
        break



