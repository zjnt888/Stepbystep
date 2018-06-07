import requests
from bs4 import BeautifulSoup
import re

'''
到全书爬取小说，然后存到一个文件。
'''

'''
根据网址取出文章一个章节
'''


def get_doc(url):
    res = requests.get(url)
    res.encoding = 'gbk'
    html = res.text
    soup = BeautifulSoup(html, 'lxml')
    '''
    标题在(class_="main b-detail")中 
    '''
    title = soup.find(class_="main b-detail").find('strong', class_="l jieqi_title")

    '''
    文章包含在(class_="mainContenr", id="content")中
    用beautifulsoup将其取出，存到sting变量docs
    '''
    docs = soup.find(class_="mainContenr", id="content")
    docs = docs.get_text()
    '''
    去除没用的前style5()后style6()
    '''
    return (title.get_text() + '\n--------------------\n\n' + docs.strip('style5();').strip('style6();')
            + '\n-----------------------------\n')


'''
根据目录页，取出每一章的链接表
'''


def get_urllist(url):
    res = requests.get(url)
    res.encoding = 'gbk'
    html = res.text
    soup = BeautifulSoup(html, 'lxml')
    ulist = []

    '''
    查找div标签下的li标签，li标签下的a标签
    <a href="http://www.quanshuwang.com/book/9/9055/9674263.html" title="国庆贺文，非盗墓笔记，免费奉送。，共6035字">国庆贺文，非盗墓笔记，免费奉送。</a>
    将链接全部存到ulist这个列表变量中
    '''
    links = soup.find('div', class_='clearfix dirconone').find_all('a')
    for link in links:
        ulist.append(link['href'])
    return ulist


if __name__ == "__main__":
    #url为目录页地址
    url = 'http://www.quanshuwang.com/book/9/9055'
    #取出目录页的地址列表，存入urls
    urls = get_urllist(url)
    #打开一个文件盗墓笔记.txt
    files = open('盗墓笔记.txt', 'w')
    '''
    使用get_doc函数将文章一个一个取出
    '''
    for url in urls:
        print("下载...", url)
        #gbk编码不认识\xa0，使用回车\n替换
        docs = u'\n'.join(get_doc(url).split())
        files.write(docs)

