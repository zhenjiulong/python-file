
import re
import os
import requests #发送网络请求
from lxml import html
etree = html.etree
if __name__ == '__main__':
    url_ = input('请输入网址栏的url:')
    #手动构造请求头参数
    headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.58',
'Cookie':'buvid3=692D11AA-2F7B-4696-8AAC-3F72E9685383148831infoc; b_nut=1630754005; LIVE_BUVID=AUTO1516307553378941; buvid_fp_plain=undefined; CURRENT_BLACKGAP=0; i-wanna-go-back=-1; blackside_state=0; fingerprint3=672141134a4fe5d8f535464fac1b7c45; _uuid=7F134F4E-D410D-103FF-EB1A-279B31ABC64988270infoc; DedeUserID=152798122; DedeUserID__ckMd5=00cd8b09d64a654b; go_old_video=1; Hm_lvt_8a6e55dbd2870f0f5bc9194cddf32a02=1662125945,1662203813,1663995026; b_nut=100; hit-new-style-dyn=0; rpdid=0z9ZwfQenO|O3wSI8yI|gAa|3w1OV9h7; buvid4=5F2A2F32-0535-70C5-E4D0-61B357AECF5116406-022012616-gI/69gb4BlvM1JoE6wwBhQ==; header_theme_version=CLOSE; is-2022-channel=1; b_ut=5; nostalgia_conf=-1; CURRENT_PID=b2aae830-cd31-11ed-b350-eb87233a4ffd; hit-dyn-v2=1; FEED_LIVE_VERSION=V8; bp_article_offset_152798122=786937458846597100; CURRENT_FNVAL=4048; CURRENT_QUALITY=80; browser_resolution=1280-609; home_feed_column=4; fingerprint=b60c6610898e9936816b9bfad34dc197; buvid_fp=b60c6610898e9936816b9bfad34dc197; SESSDATA=c009a1e8,1698114017,8dd06*41; bili_jct=9e366c7b4122ef93327c4827a4cba49b; b_lsid=88D752CF_187C1645305; sid=5ljd9a5r; PVID=3; bp_video_offset_152798122=789151875216703500; innersign=1',
        'Referer':'https://www.bilibili.com/'
    }
    #对主页视频发送请求，获取响应
    response=requests.get(url=url_,headers=headers)
    data=response.text
    #转化类型
    tree = etree.HTML(data)
    #提取视频名称  xpath取出列表 再取第零个元素
    name_list = tree.xpath('//div[@id="app"]//div/h1/@title')[0]
    print(name_list)
    #提取音视频的url
    url_str=tree.xpath('//script[contains(text(),"window.__playinfo__")]/text()')[0]
    # print(url_str)
    video_url = re.findall(r'"video":\[{"id":\d+,"baseUrl":"(.*?)"',url_str)[0]
    # print(video_url)
    audio_url = re.findall(r'"audio":\[{"id":\d+,"baseUrl":"(.*?)"',url_str)[0]
    # print(audio_url)
    #重新构造请求头
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.58',
        'Cookie': 'buvid3=692D11AA-2F7B-4696-8AAC-3F72E9685383148831infoc; b_nut=1630754005; LIVE_BUVID=AUTO1516307553378941; buvid_fp_plain=undefined; CURRENT_BLACKGAP=0; i-wanna-go-back=-1; blackside_state=0; fingerprint3=672141134a4fe5d8f535464fac1b7c45; _uuid=7F134F4E-D410D-103FF-EB1A-279B31ABC64988270infoc; DedeUserID=152798122; DedeUserID__ckMd5=00cd8b09d64a654b; go_old_video=1; Hm_lvt_8a6e55dbd2870f0f5bc9194cddf32a02=1662125945,1662203813,1663995026; b_nut=100; hit-new-style-dyn=0; rpdid=0z9ZwfQenO|O3wSI8yI|gAa|3w1OV9h7; buvid4=5F2A2F32-0535-70C5-E4D0-61B357AECF5116406-022012616-gI/69gb4BlvM1JoE6wwBhQ==; header_theme_version=CLOSE; is-2022-channel=1; b_ut=5; nostalgia_conf=-1; CURRENT_PID=b2aae830-cd31-11ed-b350-eb87233a4ffd; hit-dyn-v2=1; FEED_LIVE_VERSION=V8; bp_article_offset_152798122=786937458846597100; CURRENT_FNVAL=4048; CURRENT_QUALITY=80; browser_resolution=1280-609; home_feed_column=4; fingerprint=b60c6610898e9936816b9bfad34dc197; buvid_fp=b60c6610898e9936816b9bfad34dc197; SESSDATA=c009a1e8,1698114017,8dd06*41; bili_jct=9e366c7b4122ef93327c4827a4cba49b; b_lsid=88D752CF_187C1645305; sid=5ljd9a5r; PVID=3; bp_video_offset_152798122=789151875216703500; innersign=1',
        'Referer': url_
    }
    #发送请求 获取响应 保存为字节文件
    response_video = requests.get(url=video_url,headers=headers)
    response_audio = requests.get(url=audio_url,headers=headers)
    data_video = response_video.content#字节类型数据提取  注意是content
    data_audio = response_audio.content#字节类型数据提取  注意是content
    #保存纯视频纯音频文件
    with open (f'{name_list}_100026.mp4','wb') as f:
        f.write(data_video)
    with open (f'{name_list}_30280.mp3','wb') as f:
        f.write(data_audio)
    #视频合成  第三方工具ffmpeg
    os.system(f'ffmpeg -i "{name_list}_30280.mp3" -i "{name_list}_100026.mp4" -c copy "{name_list}.mp4"')
    #移除纯视频 纯音频文件
    os.remove(f'{name_list}_100026.mp4')
    os.remove(f'{name_list}_30280.mp3')
    print('获取完成')

