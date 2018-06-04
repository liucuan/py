# == ：Python标准操作符中的比较操作符，用来比较判断两个对象的value（值）是否相等。
# is ：Python中的身份操作符，也叫同一性运算符。用于比较判断对象间的唯一id（身份标识）是否相同。
# 判断a和b，只有数值型和字符串型的情况下，a is b 才为True；当a和b是元组（tuple），列表（list），字典（dict）或 集合（set）型时，a is b 为False。

print('a和b为数值类型'.center(50,'-'))
a = 1
b = 1
print('a', a)
print('b', b)
print('a is b', a is b)
print('a == b', a == b)
print('a的id:', id(a))
print('b的id:', id(b))

print('a和b为字符串类型'.center(50,'-'))
a = 'china'
b = 'china'
print('a', a)
print('b', b)
print('a is b', a is b)
print('a == b', a == b)
print('a的id:', id(a))
print('b的id:', id(b))

print('a和b为元组类型'.center(50,'-'))
a = (1,2,3)
b = (1,2,3)
print('a', a)
print('b', b)
print('a is b', a is b)
print('a == b', a == b)
print('a的id:', id(a))
print('b的id:', id(b))

print('a和b为列表类型'.center(50,'-'))
a = [1,2,3]
b = [1,2,3]
print('a', a)
print('b', b)
print('a is b', a is b)
print('a == b', a == b)
print('a的id:', id(a))
print('b的id:', id(b))

print('a和b为字典类型'.center(50,'-'))
a = {'name':'Tom','age':20}
b = {'name':'Tom','age':20}
print('a', a)
print('b', b)
print('a is b', a is b)
print('a == b', a == b)
print('a的id:', id(a))
print('b的id:', id(b))

print('a和b为集合类型'.center(50,'-'))
a = set([1,2,3])
b = set([1,2,3])
print('a', a)
print('b', b)
print('a is b', a is b)
print('a == b', a == b)
print('a的id:', id(a))
print('b的id:', id(b))