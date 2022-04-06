# coding:utf-8

a_list = ['python', 'django', 'django', 'flask']

a_set = set()

a_set.add(a_list[0])
a_set.add(a_list[1])
a_set.add(a_list[2])
a_set.add(a_list[-1])
print(a_set)

a_set.add(True)
a_set.add(None)
print(a_set)

a_tuple = ('a', 'b', 'c')
a_set.update(a_tuple)
print(a_set)
a_set.update('python')
print(a_set)

a_set.remove('python')
print(a_set)

a_set.clear()
print(a_set)

a_set.remove('flask')
