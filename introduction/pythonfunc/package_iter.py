# coding:utf-8

iter_obj = iter((1, 2, 3))

def _next(iter_obj):
    try:
        return next(iter_obj)
    except StopIteration:
        return None

# print(_next(iter_obj))
# print(_next(iter_obj))
# print(_next(iter_obj))
# print(_next(iter_obj))

def make_iter():
    for i in range(10):
        yield i

iter_obj = make_iter()

for i in iter_obj:
    print(i)
print('----')
for i in iter_obj:
    print(i)


iter_obj = (i for i in range(10))

for i in iter_obj:
    print(i)
print('=====')
for i in iter_obj:
    print(i)

