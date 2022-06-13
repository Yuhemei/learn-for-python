# set 只能放可以被hash的值  不可变  放[]  dict 什么的是不行的

l0 = ['222', "tyt", "b"]
s0 = set(l0)
len(s0)
s0.add(5)
s0.remove('222')

for x in s0:
    print(x)

s0.clear()
s1 = {7, 8, 9}
s0.update(s1)
s0 & s1
s0 | s1
s0.intersection(s1)
s0.union(s1)
s0.difference(s1)
{x for x in range(10) if x % 2 == 0}
{x for x in "abcdef" if x not in "bc"}