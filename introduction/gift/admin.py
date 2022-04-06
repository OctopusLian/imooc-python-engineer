# coding:utf-8

"""
   1: admin 的验证（只有admin的用户才能用这个类）
   2: 任何函数都应该动态的更新getuser
   3: 奖品的添加
   4: 奖品的删除
   5: 奖品数量的更新（同步base调整）
"""

import os

from base import Base
from common.error import NotUserError, UserActiveError, RoleError


class Admin(Base):

    def __init__(self, username, user_json, gift_json):
        self.username = username
        super().__init__(user_json, gift_json)
        self.get_user()

    def get_user(self):
        users = self._Base__read_users()
        current_user = users.get(self.username)
        if current_user == None:
            raise NotUserError('not user %s' % self.username)

        if current_user.get('active') == False:
            raise UserActiveError('the user %s had not use' % self.username)

        if current_user.get('role') != 'admin':
            raise RoleError('permission by admin')

        self.user = current_user
        self.role = current_user.get('role')
        self.name = current_user.get('username')
        self.active = current_user.get('active')

    def __check(self, message):
        self.get_user()
        if self.role != 'admin':
            raise Exception(message)

    def add_user(self, username, role):
        self.__check('permission')
        self._Base__write_user(username=username, role=role)

    def update_user_active(self, username):
        self.__check('permission')
        self._Base__change_active(username=username)

    def update_user_role(self, username, role):
        self.__check('permission')
        self._Base__change_role(username=username, role=role)

    def add_gift(self, first_level, second_level,
                     gift_name, gift_count):
        self.__check('permission')
        self._Base__write_gift(first_level=first_level, second_level=second_level,
                               gift_name=gift_name, gift_count=gift_count)


    def delete_gift(self, first_level, second_level, gift_name):
        self.__check('permission')
        self._Base__delete_gift(first_level, second_level, gift_name)

    def update_gift(self, first_level, second_level,
                    gift_name, gift_count):
        self.__check('permission')
        self._Base__gift_update(first_level=first_level, second_level=second_level,
                                gift_name=gift_name,
                                gift_count=gift_count,
                                is_admin=True)



if __name__ == '__main__':
    gift_path = os.path.join(os.getcwd(), 'storage', 'gift.json')
    user_path = os.path.join(os.getcwd(), 'storage', 'user.json')
    admin = Admin('dewei', user_path, gift_path)
    # admin.update_user_role(username='小慕', role='normals')
    admin.update_gift(first_level='level1', second_level='level2',
                      gift_name='iphone11', gift_count=1000)

