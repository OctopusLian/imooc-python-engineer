# coding:utf-8

class Parent(object):
    def __init__(self, p):
        print('hello i am parent %s ' % p)


class Child(Parent):
    def __init__(self, c):
        super().__init__('parent')
        print('hello i am child %s ' % c)


if __name__ == '__main__':
    c = Child(c='Child')
