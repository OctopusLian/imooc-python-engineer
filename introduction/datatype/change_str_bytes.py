# coding:utf-8

a = 'hello xiaomu'
print(a, type(a))

b = b'hello xiaomu'
print(b, type(b))

print(b.capitalize())
print(b.replace(b'xiaomu', b'dewei'))
print(b[:3])
print(b.find(b'x'))

print(dir(b))

c = 'hello 小慕'
d = c.encode('utf-8')
print(d, type(d))
print(d.decode('utf-8'))

