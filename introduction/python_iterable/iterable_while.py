# coding:utf-8

count = 0
total = 0

while count <= 100:
    total += count
    count += 1

    if count == 10:
        print('count 已经 到 10了')
    elif count == 50:
        print('count 已经到 50了')
    elif count == 99:
        print('count 马上就要100了！')

print(total)

users = ['dewei', 'xiaomu', 'xiaogang', 'xiaoming']
index = 0
length = len(users)

while index <= length - 1:
    print(users[index])
    index += 1

while True:
    print('xx')
