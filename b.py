# 注释
# 这是单行注释，此行内容编译过程会忽略，程序运行时不会产生任何影响
print('------------------- 输出分割线1 -------------------')

# 没有多行注释
print('------------------- 输出分割线2 -------------------')


def my_function():
    # 以下双引号包括的内容为文档内容
    """Do nothing, but document it.

    No, really, it doesn't do anything.
    """
    pass


# 打印函数"my_function"的文档描述
print(my_function.__doc__)
print('------------------- 输出分割线3 -------------------')


class car:
    """Car document.
    用于描述类作用
    """

    def __init__(self):
        """类的初始化函数
        初始化类时运行
        """
        pass


print('class car 的描述 >> ')
print(car().__doc__)
print('class car init方法的描述 >> ')
print(car().__init__.__doc__)

