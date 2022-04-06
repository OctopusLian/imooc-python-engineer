# coding:utf-8

class Cat(object):
    __cat_type = 'cat'

    def __init__(self, name, sex):
        self.name = name
        self.__sex = sex

    def run(self):
        result = self.__run()
        print(result)

    def __run(self):
        return f'{self.__cat_type}, 小猫 {self.name} {self.__sex} 开心的奔跑着'

    def dump(self):
        result = self.__dump()
        print(result)

    def __dump(self):
        return f'{self.__cat_type} 小猫 {self.name} {self.__sex} 开心的跳着'


class Test(object):
    pass


cat  = Cat(name='米粒儿', sex='boy')
cat.run()
cat.dump()
print(dir(cat))
print(cat._Cat__dump())
print(cat._Cat__cat_type)
