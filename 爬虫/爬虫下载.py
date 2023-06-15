import urllib.request
#下载网页
url_page='http://www.baidu.com'
urllib.request.urlretrieve(url_page, '../baidu.html')
url_img='https://img0.baidu.com/it/u=420527391,4002026639&fm=253&fmt=auto&app=138&f=JPEG?w=500&h=502'
urllib.request.urlretrieve(url_img, '../cx.jpg')
url_video='https://bf1.semaobf1.com/20230424/BB73EBFBEC8DE413/hls/1500k/index.m3u8'
urllib.request.urlretrieve(url_video,'video.mp4')