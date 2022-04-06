# coding:utf-8

import random

gifts = ['iphone', 'ipad', 'car', 'tv']

def chioce_gifts():
    gift = random.choice(gifts)
    print('你得到了%s' % gift)


def chioce_gift_new():
    count = random.randrange(0, 100, 1)
    if 0 <= count <= 50:
        print('你中了一个iphone')
    elif 50 < count <= 70:
        print('你中了一个ipad')
    elif 70 < count < 90:
        print('你中了一个tv电视')
    elif count >= 90:
        print('恭喜你中了一辆小汽车')

if __name__ == '__main__':
    chioce_gift_new()
