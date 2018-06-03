import requests
from bs4 import BeautifulSoup

res = requests.get(url='http://book.zhulang.com/522150/71888.html')
res.encoding = 'utf-8'
html = res.text
'''
文章包含在(class_="read-content", id="read-content")中
用beautifulsoup将其取出，存到divs
'''
soup = BeautifulSoup(html, 'lxml')
divs = soup.find_all(class_="read-content", id="read-content")

