# class Phone:
#     __is_5g_enable=False
#     def __check_5g(self):
#         if self.__is_5g_enable:
#             print("5g开启")
#         else:
#             print('5g关闭，使用4g网络')
#     def call_by_5g(self):
#        self.__check_5g()
#        print("正在通话中")
# phone=Phone()
# phone.call_by_5g()

# queue = [1, 2, 3, 4, 5]
# for i in range(3):
#     if i<2:
#         queue.pop(0)
#         print(queue)
#     else:
#         queue.append(int(input('请输入你想获取的数字：')))
#         print(queue)

# def cal(x,y):
#     multi = x*y
#     power = x**y
#     return print(multi, power, sep="\n")
#
# x=int(input())
# y=int(input())
# cal(x,y)


# x=int(input())
# y=int(input())
# print(x//y,x%y) x//y 求商 不考虑余数  x%y 求余数
# print(f'{x/y:.2f}')

# k,x,y= map(float,input().split())
# print(k <= x, k >= y, sep = "\n")

# x,y = map(int,input().split())
# print(x and y,x or y,not x,not y,sep="\n")

s1=input()
s2=input()
def compare_str(s1,s2):
    if len(s1)!=len(s2):#判断长度
        return False
    else:
        for i in range(len(s1)):
            if s1[i]!=s2[i]:
                return False
                break
            return True
print(compare_str(s1,s2))
print(compare_str(s1.lower(),s2.lower()))

