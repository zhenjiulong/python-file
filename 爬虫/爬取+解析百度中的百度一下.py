#首先获取网页源码 然后再解析
import urllib.request
from lxml import html
etree = html.etree
url='https://www.baidu.com/'

headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'}
#请求对象定制
request=urllib.request.Request(url=url,headers=headers)
#模拟服务器向浏览器发送请求
response=urllib.request.urlopen(request)
#获取源码
contect=response.read().decode('utf-8')


#解析网页源码 获取数据 xpath
tree=etree.HTML(contect)
result=tree.xpath('//input[@id="su"]/@value')
print(result)