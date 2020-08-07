
# try except else 구문으로 예외처리 합니다
    # - try except구문 뒤에 else구문을 붙여서 사용하면
    #   "예외가 발생하지 않았을때 실행할 코드'를 지정할수 있습니다.

#문법
# try:
#       예외가 예상되는 코드
# except:
#       예외가 발생했을때 실행할 코드
# else:
#       예외가 발생하지 않았을때 실행할 코드

try:
    number_input_a = int(input("정수입력>"))
except:
    print("정수를 입력하지 않았습니다.")
else:
    #출력합니다
    print("원의 반지름 : ", number_input_a)
    print("원의 둘레 : ", 2 * 3.14 * number_input_a)
    print("원의 넓이 : ", 3.14 * number_input_a * number_input_a)
















