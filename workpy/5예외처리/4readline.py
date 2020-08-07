

#특정 파일의 첫번째 줄을 읽어오는 예제
# f = open("C:\doit\새파일.txt",'r')  # 이미 생성 되어 있는 파일을 읽기 모드로 연 후
# line = f.readline() # readline()메소드를 사용해 파일의 첫 번째 줄을 읽어
# print(line) # 파이참의 출력공간에 출력 한다.


#특정 파일의 모든 줄을 읽어오는 예제
f = open("C:\doit\새파일.txt",'r') #파일을 읽기모드로 연다

while True: #무한 반복 하면서
    line = f.readline() #한줄을 읽어 와 line변수에저장
    if not line: #만약 더이상 읽을 줄이 없으면?
        break #반복문을 빠져 나감
    print(line) #한줄 단위로 읽어 들인 내용을 출력

f.close() #File객체 자원 해제








