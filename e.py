# 逻辑控制
# doc : https://docs.python.org/zh-cn/3/tutorial/controlflow.html#if-statements
x = 100

print('----------------- if start -----------------')
# if  见doc 4.1
print(' 1. if -> else 逻辑控制 >> ')
if x > 100:
    print(' x > 100 , x={}'.format(x))
else:
    print(' x <= 100, x={}'.format(x))
print()
print(' 2. if -> elif -> else 逻辑控制 >> ')
if x > 100:
    print(' x > 100, x={}'.format(x))
elif x > 50:
    print(' 50 < x <= 100, x={}'.format(x))
else:
    print(' x <= 50, x={}'.format(x))
print('----------------- if end -----------------')

print()
print('----------------- for start -----------------')
# for 见doc 4.2
print('一般的for循环 >> ')
numbers = [1, 2, 3, 4, 5]
for i in numbers:
    print(i)

print()
print('带下标的for循环 >> ')
for i, v in enumerate(numbers):
    print('index:{}, value:{}'.format(i, v))

print('----------------- for end -----------------')

print()
print('----------------- while start -----------------')
y = 3
# while
while y > 0:
    print('y={}'.format(y))
    y -= 1

# Question: 最终y值是多少？ while子句执行了几次?
print('----------------- while end -----------------')
#
