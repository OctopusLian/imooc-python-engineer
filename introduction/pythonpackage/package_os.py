# coding:utf-8

import os
import os.path

current_path = os.getcwd()
print(current_path)
print(os.path.isabs(current_path))
print(os.path.isabs('animal'))



new_path = '%s/test1' % current_path
if os.path.exists(new_path):
    os.makedirs(new_path)

data = os.listdir(current_path)
print(data)

new_path2 = os.path.join(current_path, 'test2', 'abc')
print(new_path2)
if os.path.exists(new_path2):
    os.makedirs(new_path2)
if os.path.exists('test3'):
    os.makedirs('test3')

if os.path.exists('test2/abc'):
    os.removedirs('test2/abc')
if os.path.exists('test3'):
    os.rename('test3', 'test3_new')
if os.path.exists('pip_image.py'):
    os.rename('pip_image.py', 'pip3_image.py')
if os.path.exists('%s/test3_new' % current_path):
    os.rmdir('%s/test3_new' % current_path)
if os.path.exists('test1'):
    os.rmdir('test1')

current_path = current_path + '/package_os.py'
print(os.path.isfile(current_path))
print(os.path.split(current_path))
print(os.path.isdir(os.path.split(current_path)[0]))

print(dir(os.path))
