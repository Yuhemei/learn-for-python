def print_a(msg):
    print(msg)
    print("alist:", a_list)


class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age


a_list = [1, 'python', 45.5]
# del a_list
print_a("a_list")
# 原地操作（不改变首地址）
a_list.append('ok')
print_a("a_list.append('ok')")
a_list.insert(1, 2)
print_a("a_list.insert(1, 2)")
b_list = [37, 33]
a_list.extend(b_list)
print_a("a_list.extend(b_list)")
a_list.pop(2)
a_list.remove(1)
print(a_list)
print(b_list)
b_list.clear()
print(b_list)
del a_list[1]
c_list = [2] * 100
print(c_list.count(2))
if 2 in a_list:
    print(c_list, '有2')
d_list = []
for i in range(1, 10):
    d_list.append(i)
print(d_list)
# reverse True 逆排序  False 升序
d_list.sort(reverse=True)
print(d_list)

# 非原地修改
sorted(d_list)
print(sorted(d_list))
print(d_list)
print(reversed(d_list))
len(d_list)
max(d_list)
min(d_list)
sum(d_list)
e_list = zip(c_list, d_list)

for item in enumerate(d_list):

    print(item)

# 遍历列表的三种方式

print('1.')
for i in d_list:
    print(i)
for i, data in enumerate(d_list):
    print(i, data)

for i in range(len(d_list)):
    print(d_list[i])

# 列表推导式
f_list = [i for i in range(100)]
print(f_list)

g_list = [i for i in f_list if i > 50]
print(g_list)

# 列表的切片操作 li[start:end:step],切片返回的是列表元素的浅复制
h_list = g_list
# 指向同一个内存，修改1个将会影响到另一个
print('g_list和h_list是同一个元素吗？', h_list is g_list)
# 元组tuple

a_tuple = (a_list, b_list, c_list)
print(a_tuple)
a_list[1] = 44
print(a_tuple)
# 元组中的元素若为列表可以改，元组对自己本身无法改变

# sort 按某一属性进行升降序排序
a = (0, 8, 2, 6, 3)
b = [('a', 12), ('b', 12), ('c', 1), ('d', 13), ('e', 2)]
person_list = [Person('q', 2), Person('w', 1), Person('e', 3), Person('r', 6)]
a.sort(cmp=None, key=None, reverse=True)  # reverse 参数为 True 时逆向排序
print(a)
b.sort(key=lambda x: x[1])
print(b)
person_list.sort(key=lambda x: x.age)
for i in person_list:
    print i.age
