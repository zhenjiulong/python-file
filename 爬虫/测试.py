import requests
from bs4 import BeautifulSoup
import os

def download_image(url, name):
    response = requests.get(url)
    with open(name, 'wb') as f:
        f.write(response.content)

def get_images(keywords):
    url = 'https://www.baidu.com.hk/search?q=' + keywords + '&tbm=isch'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    results = soup.find_all('img', {'class': 'rg_i'})

    if not os.path.exists(keywords):
        os.makedirs(keywords)

    for result in results:
        try:
            image_url = result['data-src']
            if 'http' in image_url and 'jpg' in image_url:
                name = keywords + '/' + image_url.split('/')[-1]
                download_image(image_url, name)
        except KeyError:
            pass

if __name__ == '__main__':
    keywords = input('请输入要搜索的关键词：')
    get_images(keywords)