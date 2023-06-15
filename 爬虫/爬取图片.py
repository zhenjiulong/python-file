import urllib.request
from lxml import html
etree = html.etree
#//div[@class="item masonry-brick"]//img/@alt
#需求： 下载前五页图片
#https://sc.chinaz.com/tupian/qinglvtupian.html  1
#https://sc.chinaz.com/tupian/qinglvtupian_2.html 2
#请求对象定制
def creat_request(page):
    if page == 1:
        url ='https://sc.chinaz.com/tupian/qinglvtupian.html'
    else:
        url='https://sc.chinaz.com/tupian/qinglvtupian_'+str(page)+'.html'

    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'}
    request = urllib.request.Request(url=url,headers=headers)
    return request
#模拟浏览器向服务器发送请求
def get_response(request):
    response=urllib.request.urlopen(request)
    contect=response.read().decode('utf-8')

    return contect
def down_load(page,contect):#利用解析浏览器方式
    tree = etree.HTML(contect)
    name_list = tree.xpath('//div[@class="container"]//div[@class="item"]/img/@alt')
    src_list = tree.xpath('//div[@class="item"]//img/@data-original')


    for i in range(len(name_list)):
        name=name_list[i]
        src=src_list[i]
        url='https:'+src
        url = url.replace('_s', '')
        urllib.request.urlretrieve(url=url,filename='D:/img/love/'+name+'.jpg')
        print(f"第{(page-1)*40+i+1}张提取完毕^_^")


#urllib.request.urlretrieve('文件地址','文件名')

if __name__=='__main__':
    startpage=int(input('请输入起始页码'))
    endpage=int(input('请输入结束页码'))
    for page in range(startpage,endpage+1):
        request = creat_request(page)
        contect = get_response(request)
        down_load(page,contect)
