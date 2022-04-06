# coding:utf-8

def add(a, b, c=3):
    return a + b + c

result = add(1, 2)
print(result)

result = add(1, 2, 6)
print(result)

def test_args(*args, **kwargs):
    print(args, type(args))
    print(kwargs, type(kwargs))

test_args(1, 2, 3, 4, 5, 6, name='dewei', age=33, top=174)

def test_args_super(*args, **kwargs):
    if len(args) >= 1:
        print(args[0])

    if 'name' in kwargs:
        print(kwargs['name'])
    else:
        print('no name')
    print(args, len(args))
    print(kwargs, len(kwargs))


test_args_super(1, name='dewei')
a = ('python', 'django')
b = {'name': 'dewei'}
test_args_super(*a, **b)

def add(a, b=1):
    print(a + b)

add(1, 2)
add(1)
add(a=1, b=2)
add(b=2, a=1)
# add(b=2)  # 会报错

def test(a, b=1, *args):
    print(a, b, args)

s = (1, 2)
test(1, 2, *s)


def test2(*sss, a, b=1):
    print(a, b, sss)

test2(a=1, b=2, *s)
''
def test3(a, b=1, **kwargs):
    print(a, b, kwargs)

test3(1, 2, name='dewei')
test3(a=1, b=2, name='dewei')
test3(name='dewei', age=33, a=1, b=2)

d = {'name': '小慕'}
test3(a=1, b=2, **d)
test3(**d, a=1, b=2)
test3(**d, a=1, b=2)
