# import requests
# import os
# #get请求
# #30280音频
# #100026视频
# #程序入口
# if __name__ == '__main__':
#     url_30280 ='https://cn-bj-fx-01-04.bilivideo.com/upgcxcode/89/54/761285489/761285489-1-30280.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1682584459&gen=playurlv2&os=bcache&oi=0&trid=0000bdac1dce2707416db32c7559b026ba06u&mid=152798122&platform=pc&upsig=4a3cf6360dd38ca88f68ec7fca43391c&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform&cdnid=70004&bvc=vod&nettype=0&orderid=0,3&buvid=692D11AA-2F7B-4696-8AAC-3F72E9685383148831infoc&build=0&agrr=1&bw=39960&np=151339102&logo=80000000'
#     url_100026 ='https://cn-bj-fx-01-01.bilivideo.com/upgcxcode/89/54/761285489/761285489-1-100026.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1682584459&gen=playurlv2&os=bcache&oi=0&trid=0000bdac1dce2707416db32c7559b026ba06u&mid=152798122&platform=pc&upsig=0d50250a0d5ef74ba2a6b30719ed71cd&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform&cdnid=70001&bvc=vod&nettype=0&orderid=0,3&buvid=692D11AA-2F7B-4696-8AAC-3F72E9685383148831infoc&build=0&agrr=1&bw=51398&np=151339102&logo=80000000'
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.58',
#         'Referer': 'https://www.bilibili.com/video/BV1vY4y1n79n/?spm_id_from=333.880.my_history.page.click&vd_source=bc1559f77ed6511b795e9a76498a72c7'
#     }
#     response_30280 = requests.get(url=url_30280, headers=headers)
#     response_100026 = requests.get(url=url_100026, headers=headers)
#     data_30280 = response_30280.content  # 字节类型数据提取  注意是content
#     data_100026 = response_100026.content
#     with open('wudao_30280.mp3', 'wb') as f:
#         f.write(data_30280)
#     with open('wudao_100026.mp4', 'wb') as f:
#         f.write(data_100026)
# #     os.system('ffmpeg -i "wudao_30280.MP3" -i "wudao_100026.mp4" -c copy "wudao.mp4"')
import requests #发送网络请求
from lxml import html
etree = html.etree
import parsel
url ='https://www.quge9.cc/book/1198/7.html'
#手动构造请求头参数
headers={
        'User-Agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.58',
'Cookie':
'__cf_bm=Y5QW7N4h5nsx5rqV5MS.M0ngxAGEy1O.uPjthleCX6k-1682648910-0-AZaxQCYCLWmDJM4OWE4Wb5xhvlacgULZGFCm7YEHpvjZJxn1wRr+9XqG+FDw5M+OSjOag2oDcW0vH35qKSN8suLWCIYHRLpmIDULKYmkjSsz',
'Referer':'https://www.beqege.cc/16747/'}
response = requests.get(url=url,headers=headers)
#获取响应体返回的文本数据 网页源代码

data=response.text
# tree = etree.HTML(data)
# name=tree.xpath('//*[@id="read"]//h1/text()')[0]
# content_list= tree.xpath('//*[@id="chaptercontent"]/text()')[:-2]
#
# novel_content = '\n'.join(content_list)
# print(novel_content)
# print(name)

#解析数据 xpath
selector = parsel.Selector(data)
title = selector.css('.bookname h1::text').get()
novel_title = selector.xpath('//*[@id="read"]//h1/text()').get()
novel_content_list = selector.xpath('//*[@id="chaptercontent"]/text()').getall()[:-2]
#需要将列表转成字符串 join方法
novel_content = '\n'.join(novel_content_list)
print(novel_content)
#保存数据
with open(f'{novel_title}.txt', 'w',encoding='utf-8') as f:
        f.write(novel_title)
        f.write('\n')
        f.write(novel_content)
        f.write('\n')
