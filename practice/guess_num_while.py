import random
num = random.randint(1, 100)
flag = True
count=0
while flag:
    guess_num = int(input("请输入你猜的数字："))
    count += 1
    if guess_num == num:
        print("恭喜你猜中了")
        flag=False
    else:
        if guess_num > num:
            print("你猜的数字大了")
        else:
            print("你猜的数字小了")
print(f"您一共猜了{count}次才猜中数字")

