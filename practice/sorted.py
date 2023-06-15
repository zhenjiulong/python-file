my_list = [["a",33],["b",55],["c",11]]
#带名函数
# def sort_key(element):
#     return element[1]
# my_list.sort(key=sort_key,reverse=True)#由大到小排序
# print(my_list)
#匿名函数
my_list.sort(key=lambda element:element[1],reverse=True)

print(my_list)
