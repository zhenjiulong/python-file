list = [1,2,3,4,5,6,7,8,9]
new_list = []
index = 0
while index < len(list):
    num = list[index]
    if index % 2 != 0:
       new_list.append(num)
    index += 1
print(f'通过while循环,取列表list中的偶数元素使其组成一个新的列表：{new_list}')


# for x in list:
#     if x%2==0:
#         new_list.append(x)
# print(f'通过f循环,从列表list中的偶数元素使其组成一个新的列表：{new_list}')
# t1=("周杰伦",11,["football","music"])
# print(f"{type(t1)}")
# print(f"学生姓名为{t1[0]}")
# print(f"学生年龄为{t1[1]}")
# del t1[2][0]
# print(t1)
# t1[2].append("coding")
# print(t1)