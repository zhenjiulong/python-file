import urllib.parse
import json
import requests
import jsonpath
url = 'https://www.duitang.com/napi/blog/list/by_search/?kw={}&start={}'
label = '爱豆'
label = urllib.parse.quote(label)
num = 0
for index in range(0,2400,24):
    u = url.format(label,index)
    we_data = requests.get(u).text
html = json.loads(we_data)
photo = jsonpath.jsonpath(html,"$..path")
for i in photo:
        a = requests.get(i)
        with open(r'D:\img\tupian\{}.jpg'.format(num),'wb') as f:
            f.write(a.content)  # 二进制
        num += 1
