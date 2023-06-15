# #账户余额
# account_amount = 0
# #函数
# def atm(num,deposit=True):
#     global account_amount
#     if deposit:
#         account_amount+=num
#         print(f"存款{num},账户余额{account_amount}")
#     else:
#         account_amount-=num
#         print(f"取款{num},账户余额{account_amount}")
#
# atm(300)
# atm(500)
# atm(345,False)

#使用闭包实现atm案例
def account(initial_account=0):

    def atm(num,deposit=True):
        nonlocal initial_account
        if deposit:
            initial_account+=num
            print(f"存款{num},账户余额{initial_account}")
        else:
            initial_account-=num
            print(f"取款{num},账户余额{initial_account}")

    return atm


f=account()
f(200)
f(300)
f(100,False)