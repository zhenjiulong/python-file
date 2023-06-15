from pymysql import  Connection
con=Connection(
    host="localhost",#主机名
    port=3306,#端口
    user="root",
    password="123456"#密码
)
print(con.get_server_info())
#执行非查询性质sql
cursor=con.cursor()#获取游标对象
#选择数据库
con.select_db("world")
#执行数据库
# cursor.execute("create table test_pymysql(id int);")
cursor.execute("select * from city")
con.close()
result=cursor.fetchall()
for i in result:
    print(i)