# f = open(r"C:\Users\宇智波纱雾\Desktop\研究生\matlab\区域图\参数.txt","r",encoding="utf-8")
# #可改写为 with open(r"C:\Users\宇智波纱雾\Desktop\研究生\matlab\区域图\参数.txt","r",encoding="utf-8") as f:
# #可省略close  后面要缩进
# content = f.read()
# print(content)
# f.close()


# with open(r"C:\Users\宇智波纱雾\Desktop\研究生\matlab\区域图\参数.txt","r",encoding="utf-8") as f:
#     content = f.read()
#     print(content)
# with open(r"C:\Users\宇智波纱雾\Desktop\pythonforbenginner\test.txt","w",encoding="utf-8") as f:
#     f.write("motherfucker")
# with open(r"C:\Users\宇智波纱雾\Desktop\pythonforbenginner\test.txt","w",encoding="utf-8") as f:
#     f.write("I LOVE YOU")
#打开一个已存在的文件 追加写入
with open(r"C:\Users\宇智波纱雾\Desktop\pythonforbenginner\test.txt","a",encoding="utf-8") as f:
    f.write("\nsunxuejie")