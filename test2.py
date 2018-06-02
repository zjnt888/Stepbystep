import urllib.request
import urllib.parse
import json

# request URL
url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"

# From Data数据
form_data = {}
form_data['action'] = 'FY_BY_REALTIME'
form_data['client'] = 'fanyideskweb'
form_data['from'] = 'AUTO'
form_data['i'] = '中国'
form_data['doctype'] = 'json'
form_data['Version'] = '2.1'
form_data['keyfrom'] = 'fanyi.web'
form_data['smartresult'] = 'dict'

data = urllib.parse.urlencode(form_data).encode('utf-8')
# post给服务器，返回res结果
res = urllib.request.urlopen(url, data)
html = res.read().decode('utf-8')

# 转换成json格式
translate_results = json.loads(html)
translate_results = translate_results['translateResult'][0][0]['tgt']
print("翻译的结果是：%s" % translate_results)
