# coding:utf-8

info = ('要从小白到一个有经验的开发者，无论是通过视频还是文字教程学习，你会发现很'
        '少有初级课程就非常贴近实际工作的，作为一个刚入坑的小白通常并不知道需要学'
        '习什么，往往是自认为入门的时候都学习了，到了公司里才发现很多都不会。'
        '我希望做这样一个课程，虽是入门课程，但涉及相关领域的多处知识，让小白在学'
        '习后进入公司岗位不会因为没听过而蒙圈；同时希望这个课也可以帮助非Python工'
        '程师快速转型或者快速转职能')

a = '小白'
b = '一个'
c = '蒙圈'
d = '课程'
e = '*'
f = '0'
g = '$'
o = '@'

test = info.replace(a, e).replace(b, f).replace(c, g).replace(d, o)
print(test)


# test = info.replace(a, e)
# print(test)
# test = test.replace(b, f)
# print(test)
# test = test.replace(c, g)
# test = test.replace(d, o)
# print(test)



