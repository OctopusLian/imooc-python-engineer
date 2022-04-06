# coding:utf-8

class Parent(object):
    def __init__(self, name, sex):
        self.name = name
        self.sex = sex

    def talk(self):
        return f'{self.name} are walking'

    def is_sex(self):
        if self.sex == 'boy':
            return f'{self.name} is a boy'
        else:
            return f'{self.name} is a girl'

class ChildOne(Parent):
    def play_football(self):
        return f'{self.name} are playing football'

class ChildTwo(Parent):
    def play_pingpong(self):
        return f'{self.name} are playing pingpong'


c_one = ChildOne(name='小慕', sex='boy')
result = c_one.play_football()
print(result)
result = c_one.talk()
print(result)

c_two = ChildTwo(name='小云', sex='girl')
result = c_two.play_pingpong()
print(result)
result = c_two.talk()
print(result)

p = Parent(name='小慕爸爸', sex='boy')
result = p.talk()
print(result)
result = p.is_sex()
print(result)
result = p.play_pingpong()
print(result)
