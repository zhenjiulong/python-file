# import math

# print("Dad!!!")
# # import math
# # math.sin(1)
# print('He said "good"')
# print ('he said \"let\'s go\"')
# print ('he said \n \"let\'s go\"')
# print('您好'+' 这是一串代码'+' hh')
# my_love="13158562337"
# print(f"拨打:{my_love}")
# greet_english="yo, what's up"
# print("小黄 "+greet_english)

total = 0
for i in range(1, 101):
    total = total+i
print(total)
my_str = "wo xi huan sun xue jie"
new_my_str = my_str.replace("wo","aa")
print(new_my_str)
new_my_str2=my_str.split(" ")#split内部要有引号和空格
print(new_my_str2)
my_list=["黑马","船只","best","漂亮妹妹","itcast","黑马","船只","漂亮妹妹","itcast"]
my_set=set()#定义空集合
for element in my_list:
    print(element)
    my_set.add(element)

print(f"集合中的对象为{my_set}")
