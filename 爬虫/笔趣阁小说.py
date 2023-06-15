import requests #发送网络请求
import re
import parsel
import pandas as pd
# while True:
key_word = input('请输入你想获取的小说名字：')
# if key_word==0:
#     break
search_url=f'https://www.quge9.cc/s?q={key_word}'
headers = {
'Cookie':'Hm_lvt_7069209d76184c3513ce3df5e48fdbd6=1682649670; Hm_lpvt_7069209d76184c3513ce3df5e48fdbd6=1682682975',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 SLBrowser/8.0.1.4031 SLBChan/33'
           # 'referer':f'https://www.quge9.cc/s?q={key_word}'}
    }
response=requests.get(url=search_url,headers=headers)
novel_data =response.text
novel_info1 = re.findall('class="bookname"><a href="(.*?)">(.*?)</a></h4><div class="author">(.*?)</div>',novel_data)
if novel_info1:
    i=0
    lis=[]
    for novel_id,name,author in novel_info1:
        novel_id=novel_info1[i][0]
        name=novel_info1[i][1]
        author=novel_info1[i][2]
        i+=1
        print(novel_id,name,author)
        dic={
            '书名':name,'id':novel_id,'作者':author
        }
        lis.append(dic)
    print(f'共搜索到{len(lis)}条数据，结果如下：')
    search_data=pd.DataFrame(lis)
    print(search_data)
    key_num = input('请选择要下载的小说序号：')
    novel_id2 = lis[int(key_num)]['id']
    url=f'https://www.quge9.cc{novel_id2}'
    headers = {'Cookie':
    'Hm_lvt_7069209d76184c3513ce3df5e48fdbd6=1682649670; Hm_lpvt_7069209d76184c3513ce3df5e48fdbd6=1682668868',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
        }
    # 请求网页内容 赋值给response
    novel_response = requests.get(url=url,headers=headers)
    novel_data=novel_response.text
    # print(novel_data)
    #使用正则表达式获取url和章节名  正则表达式提取出来的是列表形式
    novel_name = re.findall('<h1>(.*?)</h1>',novel_data)[0]
    novel_info = re.findall('<dd><a href ="(.*?)">(.*?)</a></dd>',novel_data)
    # print(novel_info)
    # print(novel_info) 将url在循环中拼接完整
    for novel_url,charper_name in novel_info:
        novel_url = 'https://www.quge9.cc'+ novel_url
        response = requests.get(url=novel_url, headers=headers)
        data = response.text
        selector = parsel.Selector(data)
        novel_content_list = selector.xpath('//*[@id="chaptercontent"]/text()').getall()[:-2]
        novel_content = '\n'.join(novel_content_list)
        with open(f'{novel_name}.txt', 'a', encoding='utf-8') as f:
            f.write(charper_name)
            f.write('\n')
            f.write(novel_content)
            f.write('\n')
        print('正在保存',charper_name)
else:
        print('请输入正确的小说名字')
