

# try except 구문과  pass키워드 조합하기에 대한 설명
# - 예외가 발생하면 일단 처리 해 줘야 하지만,
#   해당 코드가 딱히 중요한 부분이 아니라면 일단 프로그램이 강제 종료 되는 것을 막자는 목적으로
#   except구문에 아무것도 넣지 않고
#   try구문을 사용하게 됩니다.(아래 그림 참고)
#   하지만 구문 내부에 아무 것도 넣지 않으면 구문오류가 발생하므로 ..
#   다음과 같이 pass키워드를 넣어 줍니다.

#그림
#   try:
#       예외가 발생할 가능성이 있는 코드
#   except:
#       pass

#예제. 숫자로 변환되는 것들만 리스트에 넣기

# #리스트
# list_input_a = ["52","273","32","스파이","103"]
#
# #반복을 적용합니다
# list_number = []  # [52,   273,    32, 103]
#
# for item in list_input_a: #["52","273","32","스파이","103"]
#     try:
#         #숫자로 변환해서 list_number리스트에 추가
#         float(item) #예외가 발생 하면  알아서 다음으로 진행은 안되겠지?
#         list_number.append(item) #예외없이 통과 했으면 리스트에 넣어줘~
#     except:
#         pass
#
# #출력합니다
# print("{} 내부에 있는 숫자는".format(list_input_a))
# print("{}입니다.".format(list_number))

#위코드에 대한 설명
# 숫자로 변환할수 없는 문자열이라면 float(item)를 실행할때 예외가 발생합니다
# 따라서 이를 이용해 try except구문으로 감싸고 예외가 발생하지 않는경우에만 list_number.append(item)의 코드가
#실행되도록 만든 코드 입니다.

list_input_a = ["52","273","32","스파이","103"]
list_number = []

for item in list_input_a:
    try:
        item = float(item)
        list_number.append(item)
    except:
        pass

print("{} 내부에 있는 숫자는".format(list_input_a) )
print("{}입니다".format(list_number))












