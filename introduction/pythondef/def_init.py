# coding:utf-8

def capitalize(data):
    index = 0
    temp = ''

    for item in data:
        if index == 0:
            temp = item.upper()
        else:
            temp += item
        index += 1
    print('for结束了')
    return temp
    print('finish')


result = capitalize(data='hello xiaomu')
print(result)

def message(message, message_type):
    new_message = '[%s] %s' % (message_type, message)
    print(new_message)

result = message(message='今天天气真好', message_type='info')
print('message result', result)

def test():
    for i in range(10):
        if i == 5:
            return i

print('test结果是:', test())
