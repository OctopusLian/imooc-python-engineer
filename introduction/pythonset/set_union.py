# coding:utf-8

a_school = ['周五半天', '免费周末培训', '周五休息']
b_school = ['放学时间从6点改为5点', '作业少留点', '换舒服的座椅']
c_school = ['作业少留点', '周五半天', '伙食改善']

a_set = set(a_school)
b_set = set(b_school)
c_set = set(c_school)

print(a_set)
print(b_set)
print(c_set)

# help_data = a_set.union(b_set, c_set)
help_data = a_set.union(b_school, c_school)
print(help_data)
print(len(help_data))
