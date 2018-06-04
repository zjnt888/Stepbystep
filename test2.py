import requests

'''
将url对应的网页下载到本地，存储成一个文件或字符串。
使用第三方库requests

'''

res = requests.get(url='http://www.baidu.com')
res.encoding = 'utf-8'
html = res.text
print(html)
