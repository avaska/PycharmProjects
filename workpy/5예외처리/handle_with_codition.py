
#주제 :조건문으로 예외 처리하기

# #숫자를 입력받습니다
# user_input_a = input("정수입력>")
#
# #입력받은 문자열을 숫자로 변환 합니다
# number_input_a = int(user_input_a)
#
# #출력합니다
# print("원의 반지름 : ", number_input_a)
# print("원의 둘레 : ", 2 * 3.14 * number_input_a)
# print("원의 넓이 : ", 3.14 * number_input_a * number_input_a)

#위 코드는 정수를 입력하지 않으면 문제가 발생합니다
#따라서 정수를 입력하지 않았을때 조건으로 구분해서 해당 상황일때 다른 처리를 하도록 설정해 봅시다.
#--------------------------------------------------------------------------------

#숫자를 입력 받습니다
user_input_a = input("정수 입력>")

#참고 : 문자열의 isdigit()함수는 변수에 저장되어 있는 값이 숫자로만 구성된 글자인지 판별하여
#       숫자로만 구성되어 있으면 True를 반환함

#사용자 입력이 숫자로만 구성되어 있을때  True를 반환 하여  if문 내부 실행
if user_input_a.isdigit():
    #숫자로 변환합니다
    number_input_a = int(user_input_a)
    #출력합니다
    print("원의 반지름 : ", number_input_a)
    print("원의 둘레 : ", 2 * 3.14 * number_input_a)
    print("원의 넓이 : ", 3.14 * number_input_a * number_input_a)
else:
    print("정수를 입력하지 않았습니다")

print("출력성공 또는 실패!")

#위 예제 설명
#- 예외처리 후 정수로 변환할수 없는 문자열을 키보드로 입력 받았을 경우
#  lsdigit()함수를 사용해 숫자로 구성되어 있지 않다는 것을 확인하고,
#   else 구문 쪾으로 들어가서 '정수를 입력 하지 않았습니다' 라는 문자열을 출력합니다.













