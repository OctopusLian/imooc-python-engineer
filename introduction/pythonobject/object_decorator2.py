# coding:utf-8

class Test(object):
    def __init__(self, a):
        self.a = a

    def run(self):
        print('run')
        self.dump()
        self.sleep()

    @classmethod
    def dump(cls):
        print('dump')
        #cls.run()

    @staticmethod
    def sleep():
        print('i want sleep')


t = Test('a')
t.run()
# Test.dump()
# print('-----')
# Test.sleep()
# t.sleep()
# t.dump()

class Test1(object):
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value


t1 = Test1(name='dewei')
print(t1.name)
t1.name = '小慕'
print(t1.name)



