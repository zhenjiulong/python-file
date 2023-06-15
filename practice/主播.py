import requests #发送网络请求
from lxml import html
import json
from lxml.html import fromstring, tostring
etree = html.etree
# url = 'https://www.huya.com/g/2168#cate-0-0'
url = 'https://www.huya.com/cache.php?m=LiveList&do=getLiveListByPage&gameId=2168&tagAll=0&callback=getLiveListJsonpCallback&page=1'
headers={'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.116 Safari/537.36'}
response = requests.get(url=url,headers=headers)
data=response.text[25:-1]# 去除text格式前后无效字符
# print(data)
json_text = json.loads(data)       # 转为标准json格式数据集
# print(json_text)
data_list = json_text['data']['datas']
for data in data_list:
    name=data['nick']+'.jpg'#主播名字
    img_url= data['screenshot']#图片地址
    print(name,img_url)
    #发送图片数据请求
    img_data = requests.get(url = img_url,headers= headers).content#图片为二进制数据
    #数据保存
    with open (f'D:\img\\{name}',mode='wb') as f:
        f.write(img_data)
        print('保存完成：', name)
# tree1 = html.tostring(tree[0])
# from html import unescape
# tree2 = unescape(tree1.decode('utf-8'))
# tree3 = html.tostring(tree[0],encoding='utf-8').decode('utf-8')
#
# print(tree3)
# name_list = tree.xpath('//*[@id="js-live-list"]/li[2]/a[2]')
# print(name_list)
