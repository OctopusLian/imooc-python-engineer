# coding:utf-8

info = 'this is a string example!!'

result = info.startswith('this')
print(result)

result = info.startswith('this is a string example!!')
print(result)

print(bool(info == 'this is a string example!!'))

result = info.endswith('this is a string example!!')
print('result:', result)



