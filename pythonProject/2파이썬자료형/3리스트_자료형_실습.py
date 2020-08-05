
odd=[1,3,5,7,9]
print(odd)

d=[1,2,'Life','is']
print(d)

a=list()
print(a)

a=[1,2,3]
print(a)
print(a[0])

print(a[0]+a[2])
print(a[-1])

a=[1,2,3,['a','b','c']]
print(a[0])
print(a[-1])
print(a[3])
print(a[3][0])
print(a[-1][0])
print(a[-1][1])
print(a[-1][2])

a=[1,2,['a','b',['Life','is']]]
print(a[-1][-1][0])
print(a[2][2][1])

a=[1,2,3,4,5]
print(a[0:2])

a="12345"
print(a[0:2])

a=[1,2,3,4,5]
b=a[:2]
c=a[2:]
print(b)
print(c)

a=[1,2,3,['a','b','c'],4,5]
print(a[2:5])
print(a[3][:2])

a=[1,2,3]
b=[4,5,6]
print(a+b)

a=[1,2,3]
print(a*3)

a=[1,2,3]
print(len(a))

a=[1,2,3]
print(str(a[2]) + "hi")

a=[1,2,3]
a[2]=4
print(a)

a = [1,2,3]
del a[1]
print(a)

a = [1,2,3,4,5]
del a[2:]
print(a)

a=[1,2,3]
a.append(4)
print(a)

a.append([5,6])
print(a)


a=[1,4,3,2]
a.sort()
print(a)

a=['a','c','b']
a.sort()
print(a)

a=['a','c','b']
a.reverse()
print(a)

a=[1,2,3]
print(a.index(3))
print(a.index(1))
# print(a.index(0))

a=[1,2,3]
a.insert(0, 4)
print(a)
a.insert(3, 5)
print(a)

a=[1,2,3,1,2,3]
a.remove(3)
print(a)

a=[1,2,3]
print(a.pop())
print(a)

a=[1,2,3]
print(a.pop(1))
print(a)

a=[1,2,3,1]
print(a.count(1))

a=[1,2,3]
# a.extend([4, 5])
a += [4,5]
print(a)

b=[6,7]
a.extend(b)
print(a)

a = ['a','c','b']
a.reverse()
print(a)

a=[1,2,3]
print(a.index(3))
print(a.index(1))

a=[1,2,3]
a.insert(0,4)
print(a)
a.insert(3, 5)
print(a)

a=[1,2,3,1,2,3]
a.remove(3)
print(a)
a.remove(3)
print(a)

a=[1,2,3]
print(a.pop())

a=[1,2,3]
print(a.pop(1))
print(a)

a=[1,2,3,1]
print(a.count(1))
print(a.count(2))


a=[1,2,3]
a.extend([4,5])
print(a)

a.extend([6,7])
print(a)

a += [8,9]
print(a)