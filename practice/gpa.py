# gpa_dic={"小明": 3.15,"小黄":3.46,"小李":2.94,"小孙":4.1}
# for name,gpa in gpa_dic.items():
#     print("{0}您好，您当前的绩点为{1:.3f}".format(name, gpa))


class Employee:
    def __init__(self,name,id):
        self.name = name
        self.id = id

    def print_info(self):
        print(f"员工姓名：{self.name}, 员工工号：{self.id}")
class FullTimeEmployee(Employee):
    def __init__(self, name, id, monthly_salary):
        super().__init__(name,id)
        self.monthly_salary = monthly_salary

    def calculate_monthly_salary(self):
        return self.monthly_salary

class DayTimeEmployee(Employee):
    def __init__(self, name, id, daily_salary, work_days):
        super().__init__(name, id)
        self.workdays = work_days
        self.daily_salary = daily_salary

    def calculate_daily_salary(self):
        return self.daily_salary*self.workdays
xiaosu = FullTimeEmployee("小苏","10001",7000)
xiaomeng= DayTimeEmployee("小孟","10002",310,12)
xiaosu.print_info()
xiaomeng.print_info()
print(xiaosu.calculate_monthly_salary())
print(xiaomeng.calculate_daily_salary())