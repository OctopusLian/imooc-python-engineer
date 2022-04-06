# coding:utf-8

import re


def had_number(data):
    result = re.findall('\d', data)
    print(result)
    for i in result:
        return True
    return False


def remove_number(data):
    result = re.findall('\D', data)
    print(result)
    return ''.join(result)


def startswith(sub, data):
    _sub = '\A%s' % sub
    result = re.findall(_sub, data)
    for i in result:
        return True
    return False

def endswith(sub, data):
    _sub = '%s\Z' % sub
    print(_sub)
    result = re.findall(_sub, data)
    print(result)
    if len(result) != 0:
        return True
    else:
        return False


def real_len(data):
    result = re.findall('\S', data)
    print(result)
    return len(result)



if __name__ == '__main__':
    data = 'i am dewei, i am 33'
    result = had_number(data)
    print(result)
    result = remove_number(data)
    print(result)

    data = 'hello xiaomu, i am dewei. i am 33 year\'s old'
    print(re.findall('\W', data))

    result = startswith('hell', data)
    print(result)
    result = endswith('olds', data)
    print(result)
    print(len(data))
    result = real_len(data)
    print(result)
