# coding:utf-8

a = ['dewei', 'xiaomu', 'xiaohua', 'xiaoguo']
b = ['xiaohua', 'dewei', 'xiaoman', 'xiaolin']
c = ['xiaoguang', 'xiobai', 'dewei', 'xiaoyuan']

a_set = set(a)
b_set = set(b)
c_set = set(c)

print(a_set, b_set, c_set)

result = a_set.intersection(b_set, c_set)
xiaotou = list(result)
print('{} 是 这个小偷'.format(xiaotou[0]))


