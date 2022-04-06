# coding:utf-8

a = [1, 2, 3]
b = (1, 2, 3)
c = {1, 2, 3}

print(tuple(a), set(c))
print(type(tuple(a)), type(set(c)))
print(tuple(a) == b)
print(set(a) == c)

print(list(b), set(b))
print(list(c), tuple(c))

print(list(a))

print(str(a), type(str(a)))  # '[1, 2, 3]'
print(str(b), type(str(b)))
print(str(c), type(str(c)))

print(list(str(a)))
print(tuple(str(b)))
print(set(str(c)))

_a = str(a)
_b = list(_a)
print(_b)




