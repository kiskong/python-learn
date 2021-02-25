# 文件操作
# doc : https://docs.python.org/zh-cn/3/tutorial/inputoutput.html#methods-of-file-objects
# 见7.2章节

# 内置函数open介绍 : https://docs.python.org/zh-cn/3/library/functions.html#open

file_path = './doc/test.txt'

print('----------------- write file start -----------------')
print(' write "Hello World!" to {}'.format(file_path))
# 写文件
# 打开一个文件操作对象, 'w' -> 覆盖写  ,'a' -> 追加写
f = open(file_path, 'w')
# 向文件中写入内容
f.write('Hello World!')
# 关闭文件操作对象
f.close()
print('----------------- write file end -------------------')
print()

print('----------------- read file start ------------------')
f = open(file_path, 'r')
content = f.read()
f.close()
print(' read file({}) content: {}'.format(file_path, content))
print('----------------- read file end --------------------')
