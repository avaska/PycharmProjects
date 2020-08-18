
import random
print("#random 모듈")

print(random.random())

print(random.uniform(10,20))

print(random.randrange(10))

print(random.randrange(10, 20))

print(random.choice([1,2,3,4,5]))

list = ['ice cream', 'pancakes', 'brownies', 'cookies', 'candy']
random.shuffle(list)
print(list)

print( random.sample([1,2,3,4,5], k=2))


#-------------------------------------------------------------------

#sys module
import sys
print(sys.getwindowsversion())
print('----')
print(sys.copyright)
print('----')
print(sys.version)

#프로그램 강제 종료
# sys.exit()

#-------------------------------

#os module
import os

print('--------------------------------')
print("현재 운영체제 : ", os.name)
print("현재 폴더 : ", os.getcwd())
print("현재 폴더 내부의 요소들(목록) : ", os.listdir())

#폴더 생성 및 제거(폴더 비어있을 때만 제거 가능)
# os.mkdir("hello") #hello 폴더 생성
# os.rmdir("hello") #hello 폴더 삭제

#파일 생성하고 생성한 파일에 데이터 쓰기
# with open('original.txt', 'w') as file:
#     file.write('hello')


#----------------------------------------------
#urllib 모듈
from urllib import request

target = request.urlopen("https://google.com")

output = target.read().decode("utf-8")  #b(binary data) -> utf-8로 decode

print(output)




