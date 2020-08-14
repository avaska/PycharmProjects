
#class 클래스이름:
#def __init__(self, 추가적인 매개변수):
#   코드 작성

class Dog:
    def __init__(self, name):
        self.name = name;

    def bark(self):
        print(self.name + "가 멍멍하고 짖는다.")

my_dog = Dog("삼식이")
my_dog.bark()

print('-----------------------------')
result = 0
def add(num):
    global result
    result += num
    return result

print(add(3))
print(add(4))

print('-----------------------------')
class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, num):
        self.result += num
        return self.result

cal1 = Calculator()
cal2 = Calculator()

print(cal1.add(3))
print(cal1.add(4))
print(cal2.add(3))
print(cal2.add(7))
print('-----------------------------')


class FourCal:
    pass

    # def __init__(self):
    #     self.a = 0
    #     self.b = 0

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def setdata(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b
    def sub(self):
        return self.a - self.b
    def mul(self):
        return self.a * self.b
    def div(self):
        return self.a / self.b

# a = FourCal()
# print(type(a))
# a.setdata(4,2)

a= FourCal(4,2)
print(a.add())
print(a.sub())
print(a.mul())
print(a.div())

print('a 인스턴스의 주소 : ', id(a))
print('a 인스턴스의 a변수의 주소 : ', id(a.a))

print('----------------------')

class MoreFourCal(FourCal):
    # pass
    def pow(self):
        result = self.a ** self.b
        return result

a = MoreFourCal(4,2)
# a.add()
print(a.pow())

class SafeFourCal(FourCal):
    def div(self):
        if self.b == 0:
            return 0
        else:
            return self.a / self.b

a = SafeFourCal(4, 0)
print(a.div())






print('----------------------')
class Student:
    def __init__(self,name,korean,math,english,science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science

    def get_sum(self):
        return self.korean + self.math + \
               self.english + self.science

    def get_avg(self):
        return self.get_sum() / 4

    def to_string(self):
        return "{}\t{}\t{}".format(self.name, self.get_sum(), self.get_avg())

    def print(self):
        print(self.name, self.korean, self.math, self.english, self.science)
        print('합 : ', self.get_sum())
        print('평균 : ', self.get_avg())

#-----------------------------------------------------------
# stu = Student("윤인성", 89, 100, 20, 96)
# stu.print()
# stu.to_string()

students = [
    Student("윤인성", 89, 100, 20, 96),
    Student("연하진", 92, 98, 96, 98),
    Student("구지연", 76, 96, 94, 90),
    Student("나선주", 98, 92, 96, 92),
    Student("윤하진", 95, 98, 98, 98),
    Student("윤명월", 64, 88, 92, 92)
]
# print(students[0].to_string())

print("이름", "총점", "평균", sep="\t |") #seperate
for student in students:
    print(student.to_string())

print('----------------------')

class Dog:
    #클래스 변수 선언
    sound = "멍멍"

    #생성자 선언
    def __init__(self, name):
        self.name = name

    #일반 메소드 선언
    def bark(self):
        print(self.name + "가 멍멍하고 짖는다")

#인스턴스 생성
my_dog = Dog("삼식이")
your_dog = Dog("콩이")

#클래스 변수에 접근
print(my_dog.sound)
#인스턴스 변수에 접근
print(my_dog.name)

#클래스 변수에 접근
print(your_dog.sound)
#인스턴스 변수에 접근
print(your_dog.name)

print(id(my_dog.sound))
print(id(your_dog.sound))

print('----------------------')

