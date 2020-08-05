a = {'a':[1,2,3]}

a={1:'a'}
a[2] = 'b'
print(a)
a['name'] = 'pey'
print(a)
a[3] =[1,2,3]
print(a)

del a[1]
print(a)

a = {"김연아":"피겨스케이팅", "류현진":"야구", "박지성":"축구", "귀도":"파이썬"}
print(a)

grade = {'pey':10,'julliet':99}
print(grade['pey'])
print(grade['julliet'])

a={1:'a',2:'b'}
print(a[1])
print(a[2])

a={'a':1, 'b':2}
print(a['a'])
print(a['b'])


a = {'name':'pey', 'phone':'011', 'birth':'1118'}
d = a.keys()
print(d)

list = list(a.keys())
print(list)


a = {'name':'pey', 'phone':'011', 'birth':'1118'}
d = a.values()
print(d)
# list = list(a.values())

print(a.items())

a.clear()
print(a)

a = {'name':'pey', 'phone':'011', 'birth':'1118'}
print(a.get('name'))
print(a.get('phone'))
print(a.get('nokey'))
# print(a['nokey'])

print(a.get('foo', 'bar'))

a = {'name':'pey', 'phone':'011', 'birth':'1118'}
print('name' in a)
print('none' in a)
print('email' in a)

a={1:'a', 1:'b'}
print(a)

# a={[1,2] : 'hi'}
# print(a)

a = {'name':'pey', 'phone':'011', 'birth':'1118'}
for k in a.keys():
    print(k)

print(a.keys())

