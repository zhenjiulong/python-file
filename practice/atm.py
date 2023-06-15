money=5000000
name=input("请输入您的姓名：")
def query(show_header):
    if show_header:
        print("---------查询余额----------")
    print(f"{name}您好，您的余额为{money}元")

def save_money():
    num1 = int(input("请输入您要存入的钱数："))
    global money
    money+=num1
    print(f"您已存入{num1}元")
    query(False)

def get_money():
    num2 = int(input("请输入您要取出的钱数："))
    global money
    money -= num2
    print(f"您已取出{num2}元")
    query(False)

def main():
    print(f"欢迎{name}使用ATM取款机，请选择操作：")
    print("查询余额\t【输入1】")
    print("存款\t\t【输入2】")
    print("取款\t\t【输入3】")
    print("主菜单\t【输入4】")
    return input("请输入您的选择：")

while True:
    key_input=main()
    if key_input=="1":
        query(True)
        continue
    if key_input=="2":
        save_money()
        continue
    if key_input=="3":
        get_money()
        continue
    if key_input == "4":
        continue
    else:
        print("程序退出了~")
        break