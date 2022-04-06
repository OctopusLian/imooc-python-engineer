# coding:utf-8

info = 'my name is xiaomu'

info_list = info.split()
print(info_list)

if info_list[0] == 'xiaomu':
    print(1)
    info_list[0] = 'dewei'

if info_list[1] == 'xiaomu':
    print(2)
    info_list[1] = 'dewei'

if info_list[2] == 'xiaomu':
    print(3)
    info_list[2] = 'dewei'

if info_list[-1] == 'xiaomu':
    print(4)
    info_list[-1] = 'dewei'

print(info_list)
info = ' '.join(info_list)
print(info)

info = 'my name is dewei, i am a pythoner, i love python'
info_list = info.split()

if info_list[0] in ['python', 'i']:
    info_list[0] = '*'

if info_list[1] == 'python' or info_list[1] == 'i':
    info_list[1] = '*'

if info_list[2] == 'python' or info_list[2] == 'i':
    info_list[2] = '*'

if info_list[3] == 'python' or info_list[3] == 'i':
    info_list[3] = '*'

if info_list[4] == 'python' or info_list[4] == 'i':
    info_list[4] = '*'

if info_list[5] == 'python' or info_list[5] == 'i':
    info_list[5] = '*'

if info_list[6] == 'python' or info_list[6] == 'i':
    info_list[6] = '*'

if info_list[7] == 'python' or info_list[7] == 'i':
    info_list[7] = '*'

if info_list[8] == 'python' or info_list[8] == 'i':
    info_list[8] = '*'

if info_list[9] == 'python' or info_list[9] == 'i':
    info_list[9] = '*'

if info_list[-1] in ['python', 'i']:
    info_list[10] = '*'

print(info_list)

info = ' '.join(info_list)
print(info)


info = 'my name is dewei'
print(len(info))

if len(info) > 10 and len(info) != 16:
    print(info.replace('dewei', 'xiaomu'))

print('finish')

