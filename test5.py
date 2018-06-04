import json
import requests

'''
有道翻译网站
'''
url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
'''
构造一个数据包
'''
data = {}
data['action'] = ['FY_BY_CLICKBUTTON']
data['doctype'] = 'json'
data['from'] = 'AUTO'
data['i'] = 'exciting'
data['keyfrom'] = 'fanyi.web'
data['smartresult'] = 'dict'
data['to'] = 'AUTO'
data['version'] = '2.1'
data['typoResult'] = 'false'

'''
将data发送到url网站。得到一个response的反馈，用get和post都可以
把他解析成json文件格式的target变量
从target中取出翻译结果
'''
response = requests.post(url, data)
target = response.json()
print(target['translateResult'][0][0]['tgt'])
