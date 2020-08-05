#문자열은 어떻게 만들고 사용할까?

print("Hello World")

print('Python is fun')

print("""큰따옴표 3개""")
print('''작은따옴표 3개''')


food = "Python's good"
print(food)

say = '"Pythons" good'
print(say)

food = 'has\'s'
print(food)

say = "has\"s"
print(say)

multiline = "Life is too short\nYou need python"
print(multiline)

multiline='''
Life is too short
You need python
'''
print(multiline)

multiline="""
Life is too short

You need python

"""
print(multiline)


head = "Python"
tail = " is fun!"
print(head + tail)

a = "python "
print(a * 2)

print("=" * 50)
print("My Program")
print("=" * 50)

a = "Life is good"
print(len(a))

a = "Hello is"
print(a[1])
print(a[4])

b = "Hello is"
print(b[-1])
print(b[-2])



a = "Hello is"
b = a[0 : 4]
print(b)

c = a[3 : 6]
print(c)

a = "Hello is"
c  = a[1 : ]
print(c)

a = "Hello is"
c = a[ : 7]
print(c)

a = "Hello is"
c = a[ : ]
print(c)


a = "20010331Rainy"

year = a[ : 4]
print(year)
day = a[4 : 8]
print(day)
weather = a[8 : ]
print(weather)

print("I eat %d apples." %3)
print("I eat %s apples." %"five")

number=3
print("I eat %d apples." %number)

number=1
day="Hello"
print("%s라고 %d번 인사하기" %(day, number))

print("I have %s apples" %3)

print("rate is %s" %3.234)

print("Error is %d%%" %98)



print("%10s" %"hi")
print("%-10s" %"hi")
print("%-10sJANE" %"hi")


print("%0.4f" %3.42134234)
print("%10.4f" %3.42134234)

print("I eat {0} apples".format(3))
print("I eat {0} apples".format("five"))

number=3
print("I eat {0} apples".format(number))

number=10
day="three"
print("I ate {0} apples. so I was sick for {1} days.".format(number,day))



number=10
day="세계"
a = "Hello {0}번 외치고 {1} 세계여행 가자 {2}".format(number, day, "하하하")
print(a)

print("안녕하세요! {a}! 잘 {b}드립니다".format(a="여러분", b="부탁"))

print("{0:10} hello".format("h1"))
print("{0:<10} hello".format("h1"))
print("{0:>10} hello".format("h1"))


print("{0:^10}".format("hi"))

print("{0:=^10}".format("hi"))
print("{0:!<10}".format("hi"))


y=3.41234234
print("{0:0.4f}".format(y))
print("{0:10.4f}".format(y))
print("{{and}}".format())

name = '홍길동'
age = 30
print(f'나의 이름은 {name}입니다. 나이는 {age}입니다.')

age=30
print(f'나는 내년이면 {age+1}살이 된다')

d={'name':'홍길동','age':30}
print(f'나의 이름은 {d["name"]}입니다. 나이는 {d["age"]}입니다.')

print("{0:!^12}".format("python"))

print(f'{"python":^12}')
print(f'{"python":!^12}')

temp='python'
print(f'!!!{temp}!!!')

a = "hobby"
print(a.count('b'))

a = "Hello World"
b = a.find('H')  # H 문자의 인덱스 위치 0
print(b)
c = a.find('V')
print(c)


a = "Life is too short"
print(a.index('t'))
# print(a.index('A'))

a = ",".join('abcd')
print(a)

a = ",".join(['a','b','c','d'])
print(a)

a="hi"
print(a.upper())

a="HI"
print(a.lower())

a="  hi   "
print(a.lstrip())

a="  hi   "
print(a.rstrip())

a="  hi   "
print(a.strip())

a = "Life is too short"
print(a.replace("Life", "Your leg"))

a = "A B C"
print(a.replace("A","B"))



a = "Life is too short"
print(a.split())

b = "a:b:c:d"
print(b.split(':'))






