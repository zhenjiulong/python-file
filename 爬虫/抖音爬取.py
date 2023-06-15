from selenium import webdriver
import requests
import re
import os
import time
url = 'https://www.douyin.com/video/6972150528818138406'
driver = webdriver.Chrome()
driver.get(url)
time.sleep(15)

headers = {'cookie':'',
    'user-agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36'
}