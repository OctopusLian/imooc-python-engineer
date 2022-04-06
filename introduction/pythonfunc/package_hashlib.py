# coding:utf-8

import hashlib
import time

base_sign = 'muke'

def custom():
    a_timestamp = int(time.time())
    _token = '%s%s' % (base_sign, a_timestamp)
    hashobj = hashlib.sha1(_token.encode('utf-8'))
    a_token = hashobj.hexdigest()
    return a_token, a_timestamp

def b_service_check(token, timestamp):
    _token = '%s%s' % (base_sign, timestamp)
    b_token = hashlib.sha1(_token.encode('utf-8')).hexdigest()
    if token == b_token:
        return True
    else:
        return False


if __name__ == '__main__':
    need_help_token, timestamp = custom()
    time.sleep(1)
    result = b_service_check(need_help_token, int(time.time()))
    if result == True:
        print('a合法，b服务可以进行帮助')
    else:
        print('a不合法，b不可进行帮助')
