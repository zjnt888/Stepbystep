import requests
from bs4 import BeautifulSoup

'''
爬取简书作者相关信息
'''
url = 'http://www.jianshu.com/users/65ed1c462691/top_articles'

# 获取网页
header = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:36.0) Gecko/20100101 Firefox/36.0'}
response = requests.get(url, headers=header)
html = response.text
# 传入beautifulsoup 分析
soup = BeautifulSoup(html, 'lxml')
'''
作者信息都是包含在<div class="meta-block">的标签下
用find_all方法将所有符合条件的取出存在列表变量author_info中
可以用author_info[]去除相应内容
'''
author_info = soup.find_all('div', class_='meta-block')
'''
将包含在<p></p>标签下的数字存入列表变量num中
'''
num = []
num = [int(info.p.string) for info in author_info]
# for info in author_info:
#    num = info.p.string
#    print(int(num))
print(num)
