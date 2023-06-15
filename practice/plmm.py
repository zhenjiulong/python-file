import requests
import parsel
import os
url='https://www.jdlingyu.com/tag/%e5%b0%91%e5%a5%b3'
headers={'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.116 Safari/537.36'}
#发送指定地址请求，请求数据 get post 请求 响应 请求的数据
response=requests.get(url=url,headers=headers)
html_str=response.text  #text 获取对象里面的额文数据 字符串 --> 正则表达式
#print(html_str)
#通过xpath提取数据
selector=parsel.Selector(html_str)      #转换数据类型
lis=selector.xpath('//div[@id="post-list"]/ul/li')  #所有的li标签
for li in lis:
    pic_title=li.xpath('.//h2/a/text()').get()  #相册标题，用于保存相册的文件夹名
    pic_url = li.xpath('.//h2/a/@href').get()   #相册链接
    print('正在下载相册',pic_title)
    #创建相册文件夹
    if not os.path.exists('img\\' + pic_title):
        os.mkdir('D:\img\\' + pic_title)
    #发送相册详情页地址请求
    response_pic=requests.get(url=pic_url,headers=headers).text #详情页数据
    selector_2=parsel.Selector(response_pic)
    pic_url_list = selector_2.xpath('//div[@class="entry-content"]//img/@src').getall()
    #print(pic_url_list)
    #遍历每一个图片链接
    for pic_url in pic_url_list:
        #发送图片链接请求，获取图片数据
        img_data=requests.get(url=pic_url,headers=headers).content
        #准备图片的文件名
        file_name=pic_url.split('/')[-1]
        #print(file_name)
        with open(f'D:\img\\{pic_title}\\{file_name}',mode='wb') as f:
            f.write(img_data)
            print('保存完成：',file_name)
