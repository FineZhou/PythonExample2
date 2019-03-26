'''
导入csv文件
'''

from pandas import read_csv

if __name__ == '__main__':
    file = read_csv("data.csv", encoding="utf-8")
    print(file)


