a = True
b = False
print(type(a))
print(type(b))

print(1==1)
print(1>2)


a = [1,2,3,4]
while a:
    print(a.pop())

if [1,2,3]:
    print("참")
else:
    print("거짓")

print(bool('python'))
print(bool(''))
print('--------------------------')
print(bool([1,2,3]))
print(bool([]))
print(bool(0))
print(bool(()))
print(bool({}))
print(bool(None))
