# # 用字典 if input做一个流行词判断
# slang_dic = {"去收藏夹吃灰": "表示收藏了，就get了，不管自己有没有用。",
#              "我emo了": "这个情绪一般指抑郁，难过，自卑等负面情绪。",
#              "淦": "只是骂人不想被人发现，语气词。"}
# slang_dic["元宇宙"] = "一个虚拟的现实世界，有点类似于《头号玩家》里的神秘绿洲。"
# slang_dic["内卷"] = "表示竞争激励，大家都各自降低期望值。"
# slang_dic["真不戳"] = "\"真不错\"的可爱谐音。"
# slang_dic["入股不亏"] = "就是说这件事买了不亏，也有很多人用来追星。"
#
# query=input("请输入你想要查询的流行语： ")
# if query in slang_dic:
#     print("您查询的"+query+"含义如下")
#     print(slang_dic[query])
# else:
#     print("您查询的流行语暂未收录")
#     print("当前词典收录流行语"+str(len(slang_dic)) + "条")
info_dic={
    "王力宏":{"部门":"科技部","工资":3000,"级别":1,},
    "周杰伦":{"部门":"市场部","工资":5000,"级别":2,},
    "林俊杰":{"部门":"市场部","工资":7000,"级别":3,},
    "张学友":{"部门":"科技部","工资":4000,"级别":1,},
    "刘德华":{"部门":"市场部","工资":6000,"级别":2,}
}
# for i in info_dic:
#     print(f"{info_dic[i]}")
#     if info_dic[i]["级别"] == 1:
#         info_dic[i]["级别"] += 1
#         info_dic[i]["工资"] += 1000
# print(f"加薪后薪资为{info_dic}")
for name in info_dic:
    if info_dic[name]["级别"] == 1:
        employee_info_dic=info_dic[name]
        employee_info_dic["级别"]=2
        employee_info_dic["工资"] += 1000
        # 将员工信息更新回原字典
        info_dic[name]=employee_info_dic

print(info_dic)