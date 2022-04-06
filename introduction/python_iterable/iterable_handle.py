# coding:utf-8

users = [
    {'username': 'dewei', 'age': 33, 'top': 174, 'sex': '男'},
    {'username': '小慕', 'age': 10, 'top': 175, 'sex': '男'},
    {'username': 'xiaoyun', 'age': 18, 'top': 165, 'sex': '女'},
    {'username': 'xiaogao', 'age': 18, 'top': 188, 'sex': '男'}
]

man = []

for user in users:
    if user.get('sex') == '女':
        continue
    man.append(user)
    print('%s 加入了帮忙的行列' % user.get('username'))

print(man)

l = range(100)

for i in l:
    if i == 80:
        print('----')
        print('已经循环80次了，程序要退出啦')
    print(i)
else:
    print('循环正常退出了！')

print('start hello!')




