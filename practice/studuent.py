class Student:
    def __init__(self,name,student_id):
        self.name=name
        self.student_id=student_id
        self.grade={"语文":0,"数学":0,"英语":0}

    def  set_grade(self,course,grade):

        if course in self.grade:
              self.grade[course] = grade

    def print_grade(self):
        print(f"学生{self.name}(学号{self.student_id})的成绩为：")
        for course in self.grade:
         print(f"{course}:{self.grade[course]}")



lin = Student("小林",10026)
su = Student("小苏",10053)
print(lin.name)
su.set_grade("数学",90)
# lin.set_grade({"语文",67,"英语",91})
print(su.grade)
print(lin.grade)