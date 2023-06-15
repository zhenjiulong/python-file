import requests
import os
from lxml import html
etree = html.etree
from PIL import Image
from multiprocessing import Pool
def get_groups(url, headers):  # 获得重要信息
    """根据传入的最初网址和标题头，获得每个专栏的网址和标题"""
    r = requests.get(url, headers=headers)
    r.encoding = r.apparent_encoding  # 转换编码
    if r.status_code == 200:
        html = etree.HTML(r.text)
        html = etree.tostring(html)
        html = etree.fromstring(html)
        url_list = html.xpath(r"//div[@class='classify clearfix']//a/@href")  # 获得网页分组的url
        name = html.xpath(r"//div[@class='classify clearfix']//a/text()")  # 获得网页分组的标题

    else:
        print('请求错误!')
    return name, url_list  # 把分组标题和分组网址回溯


def begin_down(title, url, headers):  # 下载选择"""这里的参数为刚获取的标题和网址还有请求头"""
    print('白嫖方式下载高清图片'.center(30, '-'))
    for i, j in enumerate(title):
        print(i, '\t\t\t\t\t', j)
    inp = int(input('输入下载选项:'))
    # print(title[inp], url[inp])
    # get_image_1st(title[inp], url[inp], headers)  # 调用第一页的网址进行下载
    get_image(title[inp], url[inp], headers)  # 下载剩下的所有页
    # url = url[inp]
    # return url


def get_image_1st(title, url, headers):  # 得到第一页的图片网址
    url_1st = 'http://pic.netbian.com/' + url  # 拼接分组网址
    r = requests.get(url_1st, headers)
    if r.status_code == 200:
        html = etree.HTML(r.text)
        html = etree.tostring(html)
        html = etree.fromstring(html)
        page_url = html.xpath(r'//ul[@class="clearfix"]//li/a/@href')  # 获得每张图片的真实网址
        #  print(page_url)
        page_url = ['http://pic.netbian.com' + i for i in page_url]  # 网址拼接
        pool_down(title, page_url, headers)  # 调用图片下载函数 下载选择页的 第一页全部图片,因为第一页网址特殊


def get_image(title, url, headers):  # 得到其他页的图片网址
    """找其他页的网址，然后找到每张图片的点击图片网址"""
    pages_url = []
    for i in range(2, 10):  # 我们假定最大翻页为10页
        other_url = 'http://pic.netbian.com' + url + 'index_' + str(i) + '.html'  # 拼接网址
        # print(other_url)
        r = requests.get(other_url, headers=headers)  # 尝试请求第二页 获得图片的点击网址
        if r.status_code == 200:
            html = etree.HTML(r.text)
            html = etree.tostring(html)
            html = etree.fromstring(html)
            page_url = html.xpath(r'//ul[@class="clearfix"]//li/a/@href')  # 获得每张图片的真实网址
            page_url = ['http://pic.netbian.com' + i for i in page_url]  # 网址拼接
            pages_url.append(page_url)
    pool_down(title, pages_url, headers)  # 调用下载


def image_down(title, page_url, headers):  # 下载图片
    if not os.path.exists(title + '//'):
        os.mkdir(title + '//')
        os.chdir(title + '//')
    else:
        os.chdir(title + '//')
    for i, j in enumerate(page_url):  # 遍历第一页的图表列表
        r = requests.get(j, headers=headers)  # 请求这个图片网址
        if r.status_code == 200:
            r.encoding = r.apparent_encoding  # 修改编码
            html = etree.HTML(r.text)
            html = etree.tostring(html)
            html = etree.fromstring(html)  # 以上搭建xpath对象
            url = html.xpath(r'//a[@id="img"]/img/@src')
            name = html.xpath(r'//a[@id="img"]/img/@title')
            rr = requests.get('http://pic.netbian.com' + ''.join(url), headers=headers)
            if rr.status_code == 200:  # 请求下载图片网址
                rr.encoding = rr.apparent_encoding  # 修改编码
                with open(''.join(name) + '.png', 'wb') as fw:
                    fw.write(rr.content)
                img = Image.open(''.join(name) + '.png')
                img = img.resize((4000, 2000), Image.ANTIALIAS)  # 改变大小 抗锯齿
                # print(img.size)
                img.save(''.join(name) + '.png', quality=95)  # 质量分数 95
                print(f'{title} 中第 {i + 1} 张下载完成！')
        else:
            print('错误啦')


def pool_down(title, page_url, headers):  # 线程下载
    # print(title, len(page_url))
    path = 'D://彼岸图库//'
    # 创建总的文件夹
    if not os.path.exists(path):
        os.mkdir(path)
        os.chdir(path)
    else:
        os.chdir(path)
    #  创建一个多线程下载
    pool = Pool(6)  # 一次6下
    if len(page_url) > 2:  # 如果是其他网址
        for i in page_url:
            pool.apply(image_down, args=(title, i, headers))
    elif len(page_url) == 1:  # 如果是第一页
        pool.apply(image_down, args=(title, page_url, headers))  # 调用线程池
    pool.close()
    pool.join()

def main():
    url = 'http://pic.netbian.com/'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.116 Safari/537.36'}
    title = get_groups(url, headers)[0]
    url = get_groups(url, headers)[1]
    # get_groups(url, headers)
    begin_down(title, url, headers)
    # get_image(title, url, headers)

if __name__ == '__main__':
    main()