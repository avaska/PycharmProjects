
#예제. 파일을 열고 있으면 해당 파일을 이동하거나 덮어 쒸우거나 하는 것이 불가능 해집니다.
#따라서 프로그램에서 파일을 열었으면 무조건 닫아야 합니다
#파일을 제대로 닫았는지 파일객체의 closed속성으로 알수 있습니다.

# try:
#     #새로운 파일을 생성 하는 동시에 쓰기 모드로 연다
#     file = open("info.txt","w")
#     #여러가지 처리를 수행 합니다.
#     #file.write(dasda)
#     #파일을 닫습니다
#     file.close()
# except Exception as e:
#     print(e)
#
# print("파일이 제대로 닫혔는지 확인하기")
# print("file.closed : ", file.closed)

try:
    file = open("info.txt", "w")
    # file.write(dasda)
    file.close()
except Exception as e:
    print(e)

print("file.closed : ", file.closed)
