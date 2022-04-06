# coding:utf-8

name = 'dewei'
age = 33

def test():
    print(name)

test()

def test1():
    name = '小慕'
    print('函数体内', name)

test1()
print('函数外', name)

def test3():
    age = 33
    print(age)

test3()

def test4(a):
    a = 10

test4(name)
print(name)

def test5():
    global name
    global age
    name = 10
    age = 18


test5()
print(name)
print(age)

test_dict = {'a': 1, 'b': 2}

def test6():
    test_dict['c'] = 3
    test_dict.pop('a')


test6()
print(test_dict)
