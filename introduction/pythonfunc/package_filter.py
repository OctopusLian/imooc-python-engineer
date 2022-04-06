# coding:utf-8

from functools import reduce

frunts = ['apple', 'banana', 'orange']

result = filter(lambda x: 'e' in x, frunts)
print(list(result))
print(frunts)

def filter_func(item):
    if 'e' in item:
        return True
print('-------')
filter_result = filter(filter_func, frunts)
print(list(filter_result))

map_result = map(filter_func, frunts)  # > all
print(list(map_result))

reduce_result = reduce(lambda x, y: x * y, [1, 1, 2, 4, 4])
print(reduce_result)

reduce_result_str = reduce(lambda x, y: x * y, frunts)
print(reduce_result_str)
