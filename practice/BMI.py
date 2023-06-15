#BMI=体重/身高**2
# 偏瘦:user_BMI <= 18.5
# 正常:18.5 < user_BMI <= 25
# 偏胖:25 < user_BMI <= 30
# 肥胖:user_BMI >= 30
# user_weight = float(input("请输入您的体重(单位：千克): "))
# user_high = float(input("请输入您的身高(单位：米): "))
# user_BMI = user_weight/user_high**2
# print("您的BMI值为： " + str(user_BMI))
#
# if user_BMI <= 18.5:
#     print("您的BMI值属于偏瘦范围")
# elif 18.5 < user_BMI <= 25:
#     print("您的BMI值属于正常范围")
# elif 25 < user_BMI <= 30:
#     print("您的BMI值属于偏胖范围")
# else:
#     print("您的BMI值属于肥胖范围")


def calculate_BMI(weight,high):
    BMI = weight/high**2
    if  BMI <= 18.5:
         category="偏瘦"
    elif BMI <= 25:
        category="正常"
    elif BMI <= 30:
        category="偏胖"
    else:
          category="肥胖"
    print(f"您的BMI分类为{category}")
    return BMI
def main():
    k = "1"
    while k == "1":
        a=float(input("请输入您的体重："))
        b=float(input("请输入您的身高："))
        result = calculate_BMI(a, b)
        print(result)
        k = input("按1键继续使用，按其它任意键退出。")

if __name__ == '__main__':
    main()
