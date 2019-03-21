import numpy;
from pandas import read_csv;

data = read_csv('data_jiegoufenxi.csv');

data_pt = data.pivot_table(
    values=['月消费（元）'],
    index=['省份'],
    columns=['通信品牌'],
    aggfunc=[numpy.sum]
)

s=data_pt.sum()

sa0=data_pt.sum(axis=0)

sa1=data_pt.sum(axis=1)

sa10=data_pt.div(data_pt.sum(axis=1), axis=0)

sa01=data_pt.div(data_pt.sum(axis=0), axis=1)

print(s)
print(sa0)
print(sa1)
print(sa10)
print(sa01)