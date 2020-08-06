
test_list = ['one','two','three']
for i in test_list:
    print(i)

a = [(1,2),(3,4),(5,6)]
for (first,last) in a:
    print(first + last)

marks = [90,25,67,45,80]

number = 0
for mark in marks:
    number = number + 1
    if mark >= 60:
        print("%d번 학생은 합격입니다." %number)
    else:
        print("%d번 학생은 불합격입니다." %number)


print("--------------------------------------")
marks = [90,25,67,45,80]
number = 0
for mark in marks:
    number = number + 1
    if mark < 60:
        continue
    print("%d번 학생은 합격입니다." % number)

print("--------------------------------------")

a = range(10)
print(a)

a = range(1, 11)
print(a)

add = 0
for i in range(1, 11):
    add = add + i
print(add)


marks = [90,25,67,45,80]
for number in range(len(marks)):
    if marks[number] < 60:
        continue
    print("%d번 학생 축하합니다. 합격입니다." %(number+1))



for i in range(2,10):
    for j in range(1,10):
        print(i * j, end=" ")
    print(' ') #파이썬의 print : 개행 기능 포함



print(123)
print('hi') #print : 자동 개행 기능



#for 반복문과 딕셔너리 함께 사용하기

#for key를 저장할 변수 in 딕셔너리 :
#   코드


print('-------------------------------------------')
#예제
#딕셔너리를 선언합니다
# dictionary = {키:값, 키:값, 키:값 }
dictionary = {  "name":"7D 건조 망고",
                "type": "당절임",
                "ingredient":["망고","설탕","메타중아황산나트륨","치자황색소"],
                "origin":"필리핀"
             }
for key in dictionary:
    print(key, ":", dictionary[key])

print('--------------------------')
index = 2
print("ingredient",'[', index, '] : ',  dictionary["ingredient"][index])
