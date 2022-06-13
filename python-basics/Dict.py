dic0 = {"key": "value"}
len_dic0 = len(dic0)
dic0.clear()
str(dic0)
dic1 = {"key2": "value2"}
dic0.update(dic1)
# dict.get("key")  key不存在的话  不会报错
dic0.get("aaa", 0)
"key" in dic0
for key in dic0:
    print(key)
dic2 = {x: x * 2 for x in range(10) if x % 2 == 0}
# 以列表形式返回 dict  元组形式键值对
dic0.items()
dic0.keys()
dic0.values()