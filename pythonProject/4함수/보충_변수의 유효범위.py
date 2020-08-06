
def func():
    local_var = "지역변수"
    print(local_var)

func()
# print(local_var)


i=0
while i<5:
    i+=1
    data = 5


print(data)

print('---------------------------------')
def func():
    #global 키워드를 사용하여 해당 전역변수를 재선언함
    global global_var
    #지역변수
    local_var = "지역변수"

    print(local_var)
    print(global_var) #함수 내부에서 함수 바깥에 선언된 전역변수의 값을 얻어 출력하고 있다.

#함수 밖에 전역 변수 선언
global_var = "전역변수"
func()

print('---------------------------------')


def func1():
    var = "지역변수"
    print(var)

var = "전역변수"
print(var)

func1()

print('---------------------------------')

