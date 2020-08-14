
class Student:
    #class variable
    count = 0
    students = [] #빈 리스트

    #class method
    @classmethod
    def print(cls): #class Student 클래스 자체가 넘어옴
        print("-----학생 목록------")
        print("이름\t총점\t평균")
        for student in cls.students:
            print(str(student)) #문자열로 변환해주는 매직메소드 호출
                                # => __str__() 호출
            print("-----------------")
    
    #생성자
    def __init__(self, name, kor, math, eng, science):
        self.name = name
        self.kor = kor
        self.math = math
        self.eng = eng
        self.science = science
        # 클래스변수에 접근하여 값을 설정
        Student.count += 1
        Student.students.append(self)
        #아래에서 Student() 인스턴스를 생성하여
        #위의 클래스변수 students=[] 리스트에 추가


    def get_sum(self):
        return self.kor + self.math + self.eng + self.science

    def get_avg(self):
        return self.get_sum() / 4

    def __str__(self):
        return "{}\t{}\t{}".format(self.name, self.get_sum(), self.get_avg())



a = Student('윤인성', 87, 98, 88, 95)
b = Student("연하진", 92, 98, 96, 98)
print(str(a))
print(str(b))

print('-------------------------------')

Student.print()


