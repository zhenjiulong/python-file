print("哈喽啊~ 我是一个求平均值的程序")
userinput = input("请输入数字(完成所有数字输入后，请输入q终止程序): ")
count = 0
total = 0
while userinput != "q":
    num = float(userinput)
    total = total+num # 等价于 total += num
    count = count+1 #等价于 count += 1

    userinput = input("请输入数字，完成所有数字输入后，请输入q终止程序")

if count == 0:
    print("你是来捣乱的吧")
    result = 0
else:
    result = total/count
print("您输入数字的平均值为"+str(result))

