# coding:utf-8

drivers = ['dewei', 'xiaomu', 'xiaoming', 'xiaoman']
testers = ['xiaomu', 'xiaoman', 'xiaogang', 'xiaotao']

driver_set = set(drivers)
test_set = set(testers)

sample_drivers = driver_set.difference(test_set)
print(sample_drivers)
