# coding:utf-8

import yaml

def read(path):
    with open(path, 'r') as f:
        data = f.read()
    result = yaml.load(data, Loader=yaml.FullLoader)
    return result


if __name__ == '__main__':
    result = read('muke.yaml')
    print(result, type(result))
    print(dir(yaml))
