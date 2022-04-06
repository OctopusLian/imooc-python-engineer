# coding:utf-8

def check_str(func):
    print('func:', func)
    def inner(*args, **kwargs):
        print('args:', args, kwargs)
        result = func(*args, **kwargs)
        if result == 'ok':
            return 'result is %s' % result
        else:
            return 'result is failed:%s' % result
    return inner

@check_str
def test(data):
    return data

result = test(data='no')
print(result)

result = test(data='ok')
print(result)
