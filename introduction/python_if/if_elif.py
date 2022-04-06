# coding:utf-8

number = 20

if number > 10:
    print('number的值大于10')
elif 5 < number <= 10:
    print('number的值在5和10之间')
elif 0 < number <= 5:
    print('number的值是1～5')
else:
    print('number的值是0或者负数')

print('finish')

users = [
    ('dewei', 33, 90),
    ('xiaomu', 10, 99),
    ('xiaoming', 18, 100)
]

xiaoming = ['xiaoming', 19, 90]

if users[0][0]  == xiaoming[0]:
    xiaoming[0] = '%s_new' % xiaoming[0]
    users.append(xiaoming)
elif users[1][0] == xiaoming[0]:
    xiaoming[0] = '%s_new' % xiaoming[0]
    users.append(xiaoming)
elif users[2][0] == xiaoming[0]:
    xiaoming[0] = '%s_new' % xiaoming[0]
    users.append(xiaoming)
else:
    users.append(xiaoming)

print(users)


users = {
    'dewei': {'age': 33, 'count': 90},
    'xiaomu': {'age': 10, 'count': 99},
    'xiaoming': {'age': 18, 'count': 100}
}

if xiaoming[0] in users:
    xiaoming[0] = '%s_new' % xiaoming[0]
else:
    users[xiaoming[0]] = {'age': xiaoming[1], 'count': xiaoming[2]}
print(users)
