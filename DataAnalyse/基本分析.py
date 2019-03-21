from pandas import read_csv

data = read_csv('data81.csv')


a = data.score.describe()

b = data.score.size

c = data.score.max()

d = data.score.min

e = data.score.sum

f = data.score.mean

g = data.score.var

h = data.score.std



l = []

l.append(a)
l.append(b)
l.append(c)
l.append(d)
l.append(e)
l.append(f)
l.append(g)
l.append(h)

print(l)