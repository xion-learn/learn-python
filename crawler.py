import requests


def get_pictures(url, path):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3861.400 QQBrowser/10.7.4313.400'}
    re = requests.get(url, headers=headers)
    print(re.status_code)  # 查看请求状态，返回200说明正常
    with open(path, 'wb') as f:  # 把图片数据写入本地，wb表示二进制储存
        for chunk in re.iter_content(chunk_size=128):
            f.write(chunk)


def get_pictures_urls(text):
    st = 'img src="'
    m = len(st)
    i = 0
    n = len(text)
    urls = []  # 储存url
    while i < n:
        if text[i:i + m] == st:
            url = ''
            for j in range(i + m, n):
                if text[j] == '"':
                    i = j
                    urls.append(url)
                    break
                url += text[j]
        i += 1
    return urls


headers = {
    'Cookie': 't=8f2f9188aae1d07dcfdaa85785d10df9; r=5998; Hm_lpvt_c13cf8e9faf62071ac13fd4eafaf1acf=1708263274; Hm_lvt_a0c29956538209f8d51a5eede55c74f9=1708263275; Hm_lpvt_a0c29956538209f8d51a5eede55c74f9=1708263275',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'
}
url = 'https://www.ivsky.com/tupian/bianxingjingang_v622/'
re = requests.get(url, headers=headers)
print(re.text)
urls = get_pictures_urls(re.text)  # 获取当前页面所有图片的url
print(urls)
for i in range(len(urls)):  # 批量爬取图片
    url = 'https:' + urls[i]
    path = '变形金刚' + str(i) + '.jpg'
    get_pictures(url, path)

# import requests
#
# headers = {
#     'Cookie': 't=8f2f9188aae1d07dcfdaa85785d10df9; r=5998; Hm_lpvt_c13cf8e9faf62071ac13fd4eafaf1acf=1708263274; Hm_lvt_a0c29956538209f8d51a5eede55c74f9=1708263275; Hm_lpvt_a0c29956538209f8d51a5eede55c74f9=1708263275',
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'
# }
# url = 'https://www.ivsky.com/tupian/bianxingjingang_v622/'
# re = requests.get(url, headers=headers)
# print(re.text)
