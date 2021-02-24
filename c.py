# 变量和常量
# 单一变量声明和赋值
# doc: https://docs.python.org/zh-cn/3/reference/lexical_analysis.html#identifiers
# 见2.3章节
name = 'nick'
print(name)
print('name : {}'.format(name))

# 多个变量声明和复制
age, name = 30, 'nick'
print(age, name)
print('name : {} , age : {} '.format(name, age))

print('------------------- 输出分割线1 -------------------')

# 内置常量
# doc: https://docs.python.org/zh-cn/3/library/constants.html
print(False)
print(True)
print(None)
