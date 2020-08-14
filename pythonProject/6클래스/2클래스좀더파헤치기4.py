

class Student:
    #클래스 변수 선언
    count = 0
    #인스턴스 변수 생성 및 초기화
    def __init__(self,name,kor,math,eng,science):
        self.name = name
        self.kor = kor
        self.math = math
        self.eng = eng
        self.science = science
        #클래스변수에 접근하여 값을 설정
        Student.count +=1
        print("{}번째 학생이 생성되었습니다.".format(Student.count))

student = [
    Student("윤인성", 87,98,88,95),
    Student("연하진", 92,98,96,98),
    Student("구지연", 76,96,94,90),
    Student("나선주", 98,92,96,92),
    Student("윤아린", 95,98,98,98),
    Student("윤명월", 64,88,92,92)
]

print()
#클래스 변수에 접근
print("현재 생성된 총 학생수 {}명".format(Student.count))