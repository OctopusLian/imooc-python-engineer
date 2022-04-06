# coding:utf-8

class Test(object):

    def __str__(self):
        return 'this is a test class'

    def __getattr__(self, key):
        return '这个key:{}并不存在'.format(key)

    def __setattr__(self, key, value):
        self.__dict__[key] = value
        print(self.__dict__)

    def __call__(self, a):
        print('call func will start')
        print(a)





t = Test()
print(t)
print(t.a)
print(t.b)
t.name = '小慕'
print(t.name)
t('dewei')
# t.a.b.c 链式操作

class Test2(object):
    def __init__(self, attr=''):
        self.__attr = attr

    def __call__(self, name):
        return name

    def __getattr__(self, key):
        if self.__attr:
            key = '{}.{}'.format(self.__attr, key)
        else:
            key = key
        print(key)
        return Test2(key)

t2 = Test2()
name = t2.a.b.c('dewei')
print(name)

result = t2.name.age.sex('ok')
print(result)



