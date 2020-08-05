a = 1
b = "python"
c = [1,2,3]
print(id(a))

a=[1,2,3]
b = a
print(id(a))
print(id(b))
print(a is b)

a[1] = 4
print(a)
print(b)

print('---------------------------------------')
a=[1,2,3]
b=a[:]
# print(b)
a[1] = 4
print(a)
print(b)

print('---------------------------------------')
from copy import copy
# b = a[:]
b = copy(a)
print(a)
print(b)
print(b is a)

print('---------------------------------------')
a,b = ('python', 'life')
# (a,b) = 'python', 'life'
print(a)
print(b)

[a,b] = ['python', 'life']
# a = b = 'pyhon'

a=3
b=5
a,b = b,a
print(a)
print(b)