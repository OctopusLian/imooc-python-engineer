# coding:utf-8

int_data = 12
float_data = 3.14

str_int_data = str(int_data)
str_float_data = str(float_data)
print(str_int_data, str_float_data, type(str_int_data), type(str_float_data))

zero_number = 0
_number = -1

str_zero_number = str(zero_number)
str_number = str(_number)
print(str_zero_number, str_number, type(str_zero_number), type(str_number))

str_float = '3.14'
str_int = 123456

real_float = float(str_float)
real_int = int(str_int)

print(real_float, real_int, type(real_float), type(real_int))

mix_str = '123'
print(float(mix_str))
float_data_str = '3.14'
test_data = float(float_data_str)
print(test_data, type(test_data))

int_data_str = '123'
test_data = float(int_data_str)
print(test_data, type(test_data))

