

class Test(object):
    def __getattr__(self, key):
        print('这个key：{} 不存在'.format(key))

test = Test()
test.a

