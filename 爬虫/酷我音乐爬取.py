# import requests
# headers = {
#     'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36'
# }
# mid=input("请输入要获取音乐的id: ")
# name=input("请输入要获取音乐: ")
# url=f'http://www.kuwo.cn/api/v1/www/music/playUrl?mid={mid}&type=mp3&httpsStatus=1&reqId=8b823051-f613-11ed-b5e6-91af76ecc29c'
# response = requests.get(url=url,headers=headers)
# result = response.json()
#
# play_url = result['data']['url']
# response_music = requests.get(url=play_url,headers=headers)
# data = response_music.content
# with open(f'D:\music\\{name}.mp3', mode='wb') as f:
#     f.write(data)
#     print('保存完成：', name)

import requests #发送网络请求
import pandas as pd
# while True:
# key_word = input('请输入你想获取的音乐名字：')
key = input("请输入歌曲名或者歌手名: ")
url = f'http://www.kuwo.cn/api/www/search/searchMusicBykeyWord?key={key}&pn=1&rn=20'

headers={
"Cookie":"Hm_lvt_cdb524f42f0ce19b169a8071123a4797=1684479140; _ga=GA1.2.1494462002.1684479140; _gid=GA1.2.1025147538.1684479140; Hm_lpvt_cdb524f42f0ce19b169a8071123a4797=1684484003; kw_token=QN1RMNVUYB",
"csrf":"QN1RMNVUYB",
"Host":"www.kuwo.cn",
"Referer":"http://www.kuwo.cn/search/list?key=%E4%BA%BA%E9%97%B4%E7%83%9F%E7%81%AB",
}
response=requests.get(url=url,headers=headers)
json_data =response.json()
# print(json_data['data']['list'][0])
music_list = json_data['data']['list']
lis=[]
for data in music_list:
    artist = data['artist']
    name = data['name']
    id = data['rid']

    # print(name,artist,id)
    dic = {
        '歌名': name, '歌手': artist,'id':id
    }
    lis.append(dic)
print(f'共搜索到{len(lis)}条数据，结果如下：')
search_data=pd.DataFrame(lis)
# search_data.index=search_data.index+1
print(search_data)
key_num = input('请选择要下载的歌曲序号：')
id2 = lis[int(key_num)]['id']
info_url = f'http://www.kuwo.cn/api/v1/www/music/playUrl?mid={id2}&type=convert_url3&br=320kmp3'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36'
}
response1 = requests.get(url=info_url,headers=headers)
result = response1.json()

play_url = result['data']['url']
response_music = requests.get(url=play_url,headers=headers)
data1 = response_music.content
# print(data1)
name = lis[int(key_num)]['歌名']
artist = lis[int(key_num)]['歌手']
with open(f'D:\music\\{name}-{artist}.mp3', mode='wb') as f:
    f.write(data1)
    print('保存完成：', name)