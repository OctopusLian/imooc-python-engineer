# coding:utf-8

def sleep(name):
    return name

class Person(object):

    def __init__(self, name, age=None):
        self.name = name
        self.age = age

    def run(self):
        print(f'{self.name} 在奔跑')

    def dump(self):
        print(f'{self.name} 在跳跃')

    def work(self):
        self.run()
        self.dump()

        result = sleep(self.name)
        print('sleep result is ', result)




xiaomu = Person(name='小慕', age=10)
xiaomu.name = 'xiaomu'
xiaomu.dump()

dewei = Person(name='dewei')
dewei.dump()


dewei.top = 174
print(dewei.top)
print(dewei.age)
print('------')
xiaomu.work()


