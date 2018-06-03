import requests
from bs4 import BeautifulSoup

res = requests.get(url='http://book.zhulang.com/522150/71888.html')
res.encoding = 'utf-8'
html = res.text

soup = BeautifulSoup(html, 'lxml')
'''
在(class_="read-top")中  文章名在<p></p>标签下，章节名在<span>标签下
用beautifulsoup将其取出，分别打印
'''
title = soup.find(class_="read-top").find('h2')
print('书名  ',title.a.get_text())
print('章节  ',title.span.get_text())
'''
文章包含在(class_="read-content", id="read-content")中的<p></p>标签下
用beautifulsoup将其取出，存到列表变量docs
'''
docs = soup.find(class_="read-content", id="read-content").find_all('p')
'''
将文章段使用for语句一一取出打印，用if语句将最后含有打击盗版的一段不打印。
'''
for doc in docs:
    if '打击盗版' not in doc.get_text():
        print(doc.get_text())
        print('------------------')
