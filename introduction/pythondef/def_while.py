# coding:utf-8

count = 0

def test():
    global count
    count += 1

    if count != 5:
        print('count条件不满足， 我要重新执行我自己！当前count是%s' % count)
        return test()
    else:
        print('count is %s' % count)

test()
