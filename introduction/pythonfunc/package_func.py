# coding:utf-8

# food = input('你想吃什么呢：')
# print(food)
#
# help(input)

class Test(object):
    a = 1
    b = 2

    def __init__(self):
        self.a = self.a
        self.b = self.b


test = Test()
print(test.a)
result = vars(test)
print(result)

print(hasattr(test, 'a'))
print(hasattr(list, 'appends'))

setattr(test, 'c', 3)
print(test.c)
print(vars(test))

# setattr(list, 'c', 1)
if hasattr(list, 'appends'):
    print(getattr(list, 'appends'))
else:
    print('不能存在')

a = ['', None, True, 0]
print(any(a))
# all - > and
# any - > or



