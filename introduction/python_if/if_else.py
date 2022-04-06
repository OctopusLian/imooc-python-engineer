# coding:utf-8

url = 'https://www.imooc.com'

if 'www.imaoc.com' in url:
    print('你进入了慕课网的世界，请好好学习')
else:
    print('请前往慕课网学习python知识')

if 'www.imaoc.com' in url:
    _url = 'www.imooc.com'
else:
    _url = None
print('_url is %s' % _url)
