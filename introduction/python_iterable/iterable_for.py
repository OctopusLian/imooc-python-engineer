# coding:utf-8

l = ['dewei', 'xiaomu', 'xiaoman', 'xiaoming']

for i in l:
    print(i)

print('finish')

for i in 'python':
    print(i)

users = ('dewei', 'xiaoman', 'xiaomu', 'xiaoming')

for name in users:
    if name == 'xiaomu':
        print('你好 小慕')
    else:
        print('hello {}, 欢迎学习python'.format(name))
    print('-----')

print('finish---')

users = {'name': 'dewei', 'age': 33}
for i in users:
    print(i, users[i])

items = users.items()
print(items)

for key, value in users.items():
    print(key, value)

users_list = [
    {'username': 'dewei'},
    {'username': 'xiaomu'}
]

for user in users_list:
    print(user.get('username'))
    print(user.get('age'))

l = range(6)
print(l, type(l))

for i in l:
    print(i)
    1 / 0
else:
    print('for循环结束了')






