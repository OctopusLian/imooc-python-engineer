# coding:utf-8

a = 'abc'
print(a.split())

b = 'a,b,cd'
print(b.split(','))

c = 'a|b|c|d'
print(c.split('|', 1))

d = 'a|b|c|d'
print(d.split('|', 2))

# f = ''
# print(f.split(''))

test = ['a', 'b', 'c']
test_str = '|'.join(test)
print(test_str)

test2 = ['c', 'a', 'b']
print('|'.join(test2))


sort_str = 'a b d f i p q c'
sort_list = sort_str.split(' ')
print(sort_list)
sort_list.sort()
print(sort_list)
sort_str = ' '.join(sort_list)
print(sort_str)

sort_str_new = 'abdfipqc'
print(sort_str_new)
res = sorted(sort_str_new)
print(''.join(res))





