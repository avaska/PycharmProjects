
#isinstance(인스턴스,클래스)

class Person:
    pass

a = Person()
print(isinstance(a, Person))

b = 3
print(isinstance(b, Person))

print('--------------------------------------')
class Student:
    def study(self):
        print("공부를 합니다.")

class Teacher:
    def teach(self):
        print("학생을 가르칩니다")

classroom = [ Student(), Student(), Teacher(), Student(), Student() ]
for person in classroom:
    if isinstance(person, Student):
        person.study()
    elif isinstance(person, Teacher):
        person.teach()
    else:
        print("error")
    # result = isinstance(person, Student)
    # print(result)

# a = Student()
# print(isinstance(a, Student))
# b = Teacher()
# print(isinstance(b, Teacher))

#f = open("../6클래스/새파일.txt", 'w')

print('------------------------------------')

