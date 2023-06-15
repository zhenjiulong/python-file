import requests
headers = {
    "UserAgent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.57"
}
response=requests.get("https://www.jdlingyu.com", headers=headers)
print(response.status_code)
print(response.text)
