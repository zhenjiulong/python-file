import requests #发送网络请求
import re
import parsel
import pandas as pd


# 构造请求头处理反爬
url='https://www.quge9.cc/book/1198/'
headers = {'Cookie':
'Hm_lvt_7069209d76184c3513ce3df5e48fdbd6=1682649670; Hm_lpvt_7069209d76184c3513ce3df5e48fdbd6=1682668868',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
    }
# 请求网页内容 赋值给response
novel_response = requests.get(url=url,headers=headers)
novel_data=novel_response.text
print(novel_data)
#使用正则表达式获取url和章节名  正则表达式提取出来的是列表形式
# novel_name = re.findall('<h1>(.*?)</h1>',novel_data)[0]
# novel_info = re.findall('<dd><a href ="(.*?)">(.*?)</a></dd>',novel_data)[6:-6]
# # print(novel_info)
# # print(novel_info) 将url在循环中拼接完整
# for novel_url,charper_name in novel_info:
#     novel_url = 'https://www.quge9.cc'+ novel_url
#     response = requests.get(url=novel_url, headers=headers)
#     data = response.text
#     selector = parsel.Selector(data)
#     novel_content_list = selector.xpath('//*[@id="chaptercontent"]/text()').getall()[:-2]
#     novel_content = '\n'.join(novel_content_list)
#     with open(f'{novel_name}.txt', 'a', encoding='utf-8') as f:
#         f.write(charper_name)
#         f.write('\n')
#         f.write(novel_content)
#         f.write('\n')
#     print('正在保存',charper_name)
