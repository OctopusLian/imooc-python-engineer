# coding:utf-8

import re

def check_url(url):
    re_g = re.compile('[a-zA-Z]{4,5}://\w*\.*\w+\.\w+')
    print(re_g)
    result = re_g.findall(url)
    if len(result) != 0:
        return True
    else:
        return False

def get_url(url):
    re_g = re.compile('[https://|http://](\w*\.*\w+\.\w+)')
    result = re_g.findall(url)
    if len(result) != 0:
        return result[0]
    else:
        return ''


def get_email(data):
    re_g = re.compile('.+@.+\.[a-zA-Z]+')
    result = re_g.findall(data)
    return result


html = ('<div class="s-top-nav" style="display:none;">'
        '</div><div class="s-center-box"></div>')


def get_html_data(data):
    re_g = re.compile('style="(.*?)"')
    result = re_g.findall(data)
    return result

def get_all_data_html(data):
    re_g = re.compile('="(.+?)"')
    result = re_g.findall(data)
    return result


if __name__ == '__main__':
    result = check_url('http://www.baidu.com/')
    print(result)
    result = get_url('https://www.baidu.com/')
    print(result, 'get_url')
    result = get_email('dewei@imooc.net')
    print(result)
    result = get_html_data(html)
    print(result)
    result = get_all_data_html(html)
    print(result)
    re_g = re.compile(('<div class="(.*?)" style="(.*?)">'
        '</div><div class="(.*?)"></div>'))
    result = re_g.search(html)
    print(result.groups())
    print(result.group(1))
    print(result.group(2))
    print(result.group(3))
    # print(result.group(4))
    re_g = re.compile('\s')
    result = re_g.split(html)
    print(result)

    re_g = re.compile('<div class="(.*?)"')
    result = re_g.match(html)
    print(result.span())
    print(html[: 22])


