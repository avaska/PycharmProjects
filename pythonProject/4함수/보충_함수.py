
#2. 함수를 사용하는 이유는?
#큰 이유는 프로그램 내에서 중복적인 코드의 작성을 최소화하고,
#코드의 재사용성을 높여주기 때문입니다.

#3. 함수 선언하고 호출하기
#파이썬에서는 파이썬이 제공하는 내장함수를 그대로 사용하는 것 뿐만 아니라
#자신만의 함수를 직접 만들어서 사용할 수도 있다.


def hello():
    print("-함수 시작-")
    print("hi")
    print('-함수 끝-')

hello()


def sum(a,b):
    print(a+b)

sum(1,2)
sum(3,4)


def print_kwargs(**kwargs):
    print(kwargs)

print_kwargs(a=1)
print_kwargs(name='foo', age=3)


def sum1(a,b):
    print('-함수시작-')
    return a+b
    print('-함수 끝')

c = sum1(1,2)
print(c)

def add_and_mul(a,b):
    return a+b, a*b

result = add_and_mul(3,4)
print(result)

result1, result2 = add_and_mul(3,4)
print(result1, ',', result2)


add = lambda a,b:a+b
result = add(3,4)
print(result)

def add(a,b):
    return a+b
result = add(3,4)
print(result)


a = 1
def vartest(a):
    a = a+1
    return a
a = vartest(a)
print(a)

a = 1
def vartest():
    global a
    a = a+1

vartest()
print('global ', a)


print('---------------------------------')
def sub(a,b):
    print(a-b)

print(sub(1,2))
print(sub(a=1,b=2))
print(sub(b=1,a=2))


print('---------------------------------')
def total(a, b=5, c=10):
    print(a+b+c)
total(1)
total(1,2)
total(1,2,3)

#에러 발생 코드
# total(1,2,3,4)
# total(b=2,c=3)
#에러 설명 : 매개변수의 기본값을 설정해도 기본값을 설정하지 않은 매개변수에 인수를 전달하지 않거나
#매개변수의 수보다 많은 인수를 전달하여 함수를 호출하면 TypeError가 발생한다.

print('---------------------------------')

#선언된 매개변수에는 함수가 호출될 때 전달된 모든 인수가 튜플의 형태로 저장됩니다.
#가변 매개변수는 함수내에서 반복문을 통해 자유롭게 접근하여 사용할 수 있습니다.
def add(*paras):  #튜플형태로 매개변수로 전달
    print(paras)  #확인용 출력
    total = 0
    for para in paras:
        total += para
    return total

print(add(10))
print(add(10,2))


#가변매개변수로 딕셔너리를 사용하려면, 하나의 별 * 기호가 아닌 두개의 별 ** 기호를 사용하여 함수를 선언함
def print_map(**dicts):
    # print(dicts)
    # print(dicts.items())
    for item in dicts.items(): #items() 함수는 key,value의 쌍을 튜플로 묶은 값을 dict_items 객체로 돌려준다.
        print(item)


print_map(하나=1)
print_map(one=1, two=2)
print_map(하나=1, 둘=2, 셋=3)

print('------------------------')
#함수에서 return문을 통해 반환할 수 있는 결괏값은 언제나 하나입니다
#따라서 2개 이상의 결괏값을 반환하고 싶다면 튜플을 사용해야 합니다

def arith(a,b):
    add = a + b
    sub = a - b
    return add, sub #반환하고 싶은 모든 결괏값을 하나의 튜플로 만들어 반환할 수 있다.

a = arith(3,4)
print(a)

i,j = arith(10,1)
print(i, ',', j)


#람다
def add(a,b):
    return a+b

print(add(1,2))

#이처럼 람다는 단 한번만 사용할 함수를 간단하게 선언하고 호출할 때 매우 유용하게 사용할 수 있다.
a = (lambda a,b : a+b)(1,2)
print(a)


# (lambda 매개변수 : 리턴값)(인수1,인수2)

(lambda : print("안녕"))()



# def makeFunc(n):
#     return lambda a : a % n == 1
#
# isOdd = makeFunc(2)
# print(isOdd(11))
