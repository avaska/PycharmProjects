
class coordinate:
    #생성자
    def __init__(self, x, y):
        self.x = x
        self.y = y
    # 더하기 + 연산자 역할을 하는 메소드
        #self : coord1, other 변수에는 coord2가 들어가서
        #coordinate 클래스의 객체 형태로 반환
    def __add__(self, other):
        return coordinate(self.x + other.x, self.y + other.y)

coord1 = coordinate(5, 7)
coord2 = coordinate(3, 9)
coord3 = coord1.__add__(coord2)
print('x,y : ',coord3.x, ',', coord3.y)

print('----------------------------')

# f = open("C:/doit/새파일.txt", 'w')
#
# for i in range(1,11):
#     data =


#==============================================================================
#예제2.
class Student:
    def __init__(self, name, kor, math, eng, science):
        self.name = name   #instance variable
        self.kor = kor
        self.math = math
        self.eng = eng
        self.science = science

    #method
    def get_sum(self):
        return self.kor + self.math + self.eng + self.science

    def get_avg(self):
        return self.get_sum() / 4

    #magic method
    
    #toString() 호출 시 작동하는 매직메서드
    def __str__(self, student):
        return "{}\t{}\t{}".format(self.name,
                                   self.get_sum(student),
                                   self.get_avg(student)
                                   )
    def __eq__(self, value):
        return self.get_sum() == value.get_sum()

    def __ne__(self, other):
        return self.get_sum() != other.get_sum()

    def __gt__(self, other):
        return self.get_sum() > other.get_sum()

    def __ge__(self, other):
        return self.get_sum() >= other.get_sum()

    def __lt__(self, other):
        return self.get_sum() < other.get_sum()

    def __le__(self, other):
        return self.get_sum() <= other.get_sum()

# a = Student('kim', 20, 30, 40, 50)
# b = Student('lee', 100, 80, 70, 90)
# c = Student('park', 30, 50, 70, 90)
#
# print(a.__eq__(b))
# print(b.__ne__(c))

print('---------------------------------')
students = [
    Student('kim', 20, 30, 40, 50),
    Student('lee', 100, 80, 70, 90),
    Student('park', 30, 50, 70, 90),
    Student('윤인성', 76, 82, 92, 45),
    Student('연하진', 48, 21, 100, 77),
    Student('홍길동', 97, 98, 77, 86),
]

student_a = Student('윤인성', 76, 82, 92, 45)
student_b = Student('연하진', 48, 21, 100, 77)


print(student_a == student_b)
print(student_a != student_b)
print(student_a > student_b)
print(student_a >= student_b)
print(student_a <= student_b)
print(student_a < student_b)

# print(student_a.__str__())

# for stu in students:
#     # print(stu.name, "'s avg : ", stu.get_avg())
#     # stu.__str__(student_a)
#     print('eq : ', stu.__eq__(student_a))
#     print('ne : ', stu.__ne__(student_a))
#     print('gt : ', stu.__gt__(student_a))
#     print('ge : ', stu.__ge__(student_a))
#     print('lt : ', stu.__ge__(student_a))
#     print('le : ', stu.__ge__(student_a))
#     print('---------------------------------')














