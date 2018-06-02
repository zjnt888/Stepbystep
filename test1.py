'''
将url对应的网页下载到本地，存储成一个文件或字符串。

'''

import urllib.request

response = urllib.request.urlopen('http://www.baidu.com')
buff = response.read()
html = buff.decode("utf8")
print(html)
