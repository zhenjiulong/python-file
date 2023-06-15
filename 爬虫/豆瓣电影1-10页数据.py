#多页需要下拉网页观察接口规律
#page  1   2   3   4
#start 0   20   30   40
#start = (page-1)*20
#用函数定制请求对象
import urllib.parse
import urllib.request


def creat_request(i):
    base_url='https://movie.douban.com/j/chart/top_list?type=13&interval_id=100%3A90&action=&'
    data={'start':(i-1)*20,'limit':20 }
    #编码数据
    data=urllib.parse.urlencode(data)
    url=base_url+data
    #print(url)
    headers={'Cookie':'T=1665061321:RT=1665061321:S=ALNI_Ma2lDbnObjISSOMr84JzJ1Jb5AwWw; __gpi=UID=00000a17375ddf82:T=1664716720:RT=1665297142:S=ALNI_MZCmtbQjePoDd2ZPtzqOPZq4MaxMQ; __yadk_uid=xGE84o680io9HGLeZkW9wsH2K68O4vBQ; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1682392027%2C%22https%3A%2F%2Fcn.bing.com%2F%22%5D; _pk_ses.100001.4cf6=*; ap_v=0,6.0; __utma=30149280.2020707685.1631283544.1677830923.1682392027.12; __utmb=30149280.0.10.1682392027; __utmc=30149280; __utmz=30149280.1682392027.12.5.utmcsr=cn.bing.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utma=223695111.262439283.1631283544.1677830923.1682392027.11; __utmb=223695111.0.10.1682392027; __utmc=223695111; __utmz=223695111.1682392027.11.5.utmcsr=cn.bing.com|utmccn=(referral)|utmcmd=referral|utmcct=/; _pk_id.100001.4cf6=fa6f3dc122aa06a8.1631283544.11.1682392060.1677832695. ',

        'User-Agent':' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.58'
    }
    #请求对象定制
    request=urllib.request.Request(url=url,headers=headers)
    return request
def get_contect(request):
    response=urllib.request.urlopen(request)
    contect=response.read().decode('utf-8')
    return contect

def down_load(i,contect):
    with open(f'douban_{i}.json','w',encoding='utf-8') as d:
        d.write(contect)

#程序的入口
if __name__=='__main__':
    startpage = int(input('请输入起始页'))
    endpage = int(input('请输入结束页'))

    for i in range(startpage,endpage+1):
       request = creat_request(i)
       contect=get_contect(request)
       down_load(i,contect)
