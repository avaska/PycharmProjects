

#try except 구문을 사용합니다

try:
    #파일을 쓰기모드로 연다
    file = open("info.txt","w")
    #여러가지 처리를 수행합니다
    예외.발생해라()

except Exception as e:
    print(e)
finally:
    # 파일을 닫습니다
    file.close()

print("파일이 제대로 닫혔는지 확인하기")
print(file.closed)

#코드를 실행 해보면 closed속성의 반환값이 False이므로 파일이 닫히지 않았다는 것을 알수 있습니다
#따라서 반드시 finally구문을 사용하여 파일을 닫게 해야합니다.


