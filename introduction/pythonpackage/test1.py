# coding:utf-8

from animal import dog_run
from animal import cat_run
from animal.cat.action import cat_name
# from animal.cat.action import Cat
#
# cat = Cat()
# cat.run()

dog_run_result = dog_run()
cat_run_result = cat_run()

print(dog_run_result)
print(cat_run_result)
print(cat_name)
