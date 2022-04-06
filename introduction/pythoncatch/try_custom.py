# coding:utf-8

def test(number):
    if number == 100:
        raise ValueError('number 不可以是100')
    return number

result = test(50)
print(result)

# result = test(100)

def test2(number):
    try:
        return test(number)
    except ValueError as e:
        return e

result = test2(100)
print(result)

def test3():
    raise '错误了'

# test3()

def test4(name):
    if name == 'dewei':
        raise Exception('dewei不可以被填写')
    return name

# test4('dewei')

class NumberLimitError(Exception):
    def __init__(self, message):
        self.message = message


class NameLimitError(Exception):
    def __init__(self, message):
        self.message = message


def test5(name):
    if name == 'dewei':
        raise NameLimitError('dewei不可以被填写')
    return name

def test6(number):
    if number > 100:
        raise NumberLimitError('数字不可以大于100')
    return number

print('------')

try:
    test5('dewei')
except NameLimitError as e:
    print(e)

try:
    test6(1000)
except NumberLimitError as e:
    print(e)

test5('dewei')

