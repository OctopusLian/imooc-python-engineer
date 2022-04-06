# coding:utf-8

"""
    抽奖函数 随机判断第一层(level1) 1:50% 2:30% 3:15% 4:5%
    抽奖函数 随机判断第二层(level2) 1:80% 2:15% 3:5%
    抽奖函数 获取到对应层级的真实奖品,并随机一个奖品,查看奖品count是否为0:
            不为零——中奖,提示用户,并且奖品数量-1,并为用户更新奖品到user表中的gifts中,
            数量为零——未中奖.

    课后作业：
    1: 防止并发操作userjson与giftjson
    2: 用__gift_update替代抽奖函数中手动更改奖品数量
    3: 登录体系优化 regist (username, password) role = normal active False
                  base 获取所有active为false的用户 __check_by_acitve(active)
                  get_user, abc, hashlib md5 sha1 xxxaslkdfjal;dskfjx
    4: 每日抽奖次数限制 userjson count 每天抽奖次数 check_gift_count
"""
import os
import random

from base import Base
from common.utils import timestamp_to_string
from common.error import (NotUserError, RoleError,
                          UserActiveError, CountError)


class User(Base):
    def __init__(self, username, user_json, gift_json):
        self.username = username
        self.gift_random = list(range(1, 101))

        super().__init__(user_json, gift_json)
        self.get_user()

    def get_user(self):
        users = self._Base__read_users()

        if self.username not in users:
            raise NotUserError('not user %s' % self.username)

        current_user = users.get(self.username)
        if current_user.get('active') == False:
            raise UserActiveError('the user %s had not use'
                                  % self.username)
        if current_user.get('role') != 'normal':
            raise RoleError('permission by normal')

        self.user = current_user
        self.name = current_user.get('username')
        self.role = current_user.get('role')
        self.gifts = current_user.get('gifts')
        self.create_time = timestamp_to_string(current_user.get(
            'create_time'))

    def get_gifts(self):
        gifts = self._Base__read_gifts()
        gift_lists = []

        for level_one, level_one_pool in gifts.items():
            for level_two, level_two_pool in level_one_pool.items():
                for gift_name, gift_info in level_two_pool.items():
                    gift_lists.append(gift_info.get('name'))
        return gift_lists

    def choice_gift(self):
        self.get_user()

        # level1 get
        first_level, second_level = None, None
        level_one_count = random.choice(self.gift_random)
        if 1 <= level_one_count <= 50:
            first_level = 'level1'
        elif 51 <= level_one_count <= 80:
            first_level = 'level2'
        elif 81 <= level_one_count < 95:
            first_level = 'level3'
        elif level_one_count >= 95:
            first_level = 'level4'
        else:
            raise CountError('level_one_count need 0~100')

        gifts = self._Base__read_gifts()
        level_one = gifts.get(first_level)

        level_two_count = random.choice(self.gift_random)

        if 1 <= level_two_count <= 80:
            second_level = 'level1'
        elif 81 <= level_two_count < 95:
            second_level = 'level2'
        elif 95 <= level_two_count < 100:
            second_level = 'level3'
        else:
            raise CountError('level_two_count need 0~100')

        level_two = level_one.get(second_level)
        if len(level_two) == 0:
            print('哦可惜 您没有中奖')
            return

        gift_names = []
        for k, _ in level_two.items():
            gift_names.append(k)

        gift_name = random.choice(gift_names)
        gift_info = level_two.get(gift_name)
        if gift_info.get('count') <= 0:
            print('哦可惜 您没有中奖')
            return
        gift_info['count'] -= 1
        level_two[gift_name] = gift_info
        level_one[second_level] = level_two
        gifts[first_level] = level_one

        self._Base__save(gifts, self.gift_json)
        self.user['gifts'].append(gift_name)
        self.update()
        print('恭喜您 获得 %s 奖品' % gift_name)

    def update(self):
        users = self._Base__read_users()
        users[self.username] = self.user

        self._Base__save(users, self.user_json)


if __name__ == '__main__':
    gift_path = os.path.join(os.getcwd(), 'storage', 'gift.json')
    user_path = os.path.join(os.getcwd(), 'storage', 'user.json')
    user = User('小慕', user_path, gift_path)
    user.choice_gift()
