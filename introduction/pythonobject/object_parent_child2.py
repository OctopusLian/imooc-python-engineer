# coding:utf-8

# 1 2个父类

class Tool(object):
    def work(self):
        return 'tool work'

    def car(self):
        return 'car will run'


class Food(object):
    def work(self):
        return 'food work'

    def cake(self):
        return 'i like cake'


# 继承父类的子类吧
class Person(Food, Tool):
    pass


if __name__ == '__main__':
    p = Person()
    p_car = p.car()
    p_cake = p.cake()
    print(p_car)
    print(p_cake)
    p_work = p.work()
    print(p_work)
    print(Person.__mro__)
