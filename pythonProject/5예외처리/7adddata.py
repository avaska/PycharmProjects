
#파일을 파일의 마지막에 새로운 내용을 추가 하기 위해 추가모드로 연다
# f = open("C:/doit/새파일.txt",'a')
#          #[11,12,13,14,15,16,17,18,19]
# for i in range(11,20): # 11 부터 19까지 i변수에 대입됨
#     data = "%d 번째 줄입니다.\n" %i
#     f.write(data) # 새파일.txt파일의 마지막에 data변수의 값을 추가로 쓴다.
#
# f.close()

f = open("C:/doit/새파일.txt", 'a')

for i in range(11, 20):
    data = "%d번째 줄입니다\n" %i
    f.write(data)

f.close()

f = open("C:/doit/새파일.txt", 'r')
data = f.read()
print(data)
f.close()