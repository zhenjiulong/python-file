class Studens:
    # name=None
    # age=None
    # adr=None
    def __init__(self,name,age,adr):
        self.name=name
        self.age=age
        self.adr=adr
for x in range(1,11):
    print(f"当前第{x}位学生信息，总需要录入10位学生信息")
    stu=Studens(input("请输入学生姓名："),input("请输入学生年龄："),input("请输入学生地址："))

    print(f"学生信息录入完成信息为：【学生姓名：{stu.name}，年纪：{stu.age}，地址：{stu.adr}】")
