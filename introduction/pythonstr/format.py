# coding:utf-8

info = 'my name is %s, my age is %s'

name_01 = '小慕'
age_01 = 10
name_02 = 'dewei'
age_02 = 33
print(info % (name_01, age_01))
print(info % (name_02, age_02))

message = '您好， 今天是%s, 您的手机号码：%s 已经欠费了，请尽快充值'
print(message % ('星期一', 123456789))

print(message % (1234567, '星期2'))
print(message)

books = ['python', 'django', 'flask']
info_2 = 'my name is %s, my age is %s, my book is %s'
print(info_2 % (name_01, age_01, books))

dict_01 = {'a': 'a', 'b': 'b'}
print('dict is %s' % dict_01)

info_3 = 'my name is {0}, my age is {1}, my book is {2}'
print(info_3.format(name_02, age_02, books))

info_4 = f'my name is {name_02}, my age is {age_02}'
print(info_4)

print(info_3.format('dewei', 33, ['python']))


