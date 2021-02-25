# 字符操作
# doc : https://docs.python.org/zh-cn/3/library/stdtypes.html#text-sequence-type-str

name = 'nick'

# 大写
print(name.upper())

# 小写
print(name.lower())

# 首字母大写
print(name.capitalize())

# 字符串反转
# method 1
print(name[::-1])

# method 2
name_array = list(name)
name_array.reverse()
print(''.join(name_array))

# method 3
# TODO
pass