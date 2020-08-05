

#리스트 자료형 이란?
    #리스트는 간단히 순서대로 늘어선 박스로 이해할수 있습니다.
    #각 박스에는 다양한 타입의 데이터를 저장할 수 있으며
    #이 박스들을 통들어서 리스트라고 부르게 됩니다.

#파이썬에서 리스트의 특징
    #1. 리스트에 저장된 요소가 모두 같은 타입일 필요는 없습니다.
    #2. 리스트에는 요소들이 순서대로 저장되며,
    #   각요소는 0부터 시작하는 인덱스 위치를 사용하여 접근할 수 있습니다.
    #3. 리스트는 그 값을 변경할수 있습니다.

    #참고1 : 이와 같은 데이터 타입을 다른 프로그래밍 언어에서는 배열(array)이라고도 부르지만,
    #       파이썬에서는 리스트(list)라는 용어만을 사용합니다.

    #참고2 : 아무런 요소도 저장하고 있지 않은 리스트를 빈리스트라고 부르며,
    #        파이썬에서는  []로 표현할수 있습니다.

#리스트 선언 하기
    #파이썬에서 리스트는 대괄호 [] 로 감싸서 선언 할수 있으며,
    #리스트 안의 요소(elements)들은  쉼표,로 구분 합니다
    #문법
    #리스트명(변수명) = [요소1, 요소2, 요소3,......]
    #                   0     1       2  ...... 인덱스 위치값
a = [] #비어 있는 리스트[]
b = [1,2,3]  # 숫자를 요솟값으로 가지는 리스트[]
c = ['Life','is','too','short']  #문자열을 요솟값으로 가지는 리스트[]
d = [1,2,'Life','is'] # 숫자와 문자열을 함께 요솟값으로 가지는 리스트[]
e = [1,2, ['Life','is'] ]  # 리스트[] 자체를 요솟값으로 가지는 리스트[]

#리스트 인덱싱
#예제
a = [1,2,3]
#    0 1 2    >>
#    -3-2-1   <<

print(a)  # [1, 2, 3] 출력됨
print(a[0]) # a[0]은 리스트a의 첫번째 요솟값을 얻는 코드 이다.
print(a[0]  + a[2]) #리스트의 첫번째 요소인 a[0]인덱스 위치의 값과
                    # 세번째 요소인 a[2]인덱스 위치의 값을 더한 결과  4를 출력함
print(a[-1]) # a[-1]는 리스트a의 마지막 요소값부터 가리켜 얻어 3을 출력함

#예제
#리스트a를  숫자 1,2,3과 또 다른 리스트인 ['a','b','c']를 포함 하여 만들기
a = [1,2,3, ['a','b','c'] ]
#    0 1 2       3
print(a[0]) # 1출력됨
print(a[-1]) #['a', 'b', 'c'] 출력됨
print(a[3]) #['a', 'b', 'c'] 출력됨

print(a[3][1])  # b 출력됨

#리스트a에 포함된 ['a','b','c']리스트에서 'a'값을 인덱싱을 사용해 끄집어 내기
#a[-1]  ->  ['a','b','c']
#              0  1   2
#a[-1][0] -> 'a'
print(a[-1][0]) # a 출력됨

#리스트 슬라이싱
#예제
a = [1,2,3,4,5]
#    0 1 2 3 4

print(a[0:2]) # 0위치에서 부터 2이전 까지인 1위치의 값인?  [1,2]리스트로 만들어서 출력함
print(a[:2])  # 처음부터 a[1]까지 ->  [1,2]리스트로 만들어서 출력함
print(a[2:])  # a[2]부터 마지막 인덱스 위치의 요소값 까지를  잘라내서 새로운 []리스트에 담아서 출력함
              # [3,4,5] 출력

#리스트 연산하기
#리스트 역시  +  기호를 사용해서 더할 수 있고    * 기호를 사용해서 반복할수 있다.
#1. 리스트 더하기 +
#예제
#리스트 사이에서 + 기호는 2개의 리스트를 합치는 기능을 한다.
a = [1,2,3]
b = [4,5,6]
c = a + b
print(c)
#2. 리스트 반복하기 *
a = [1,2,3]
b = a * 3    # [1,2,3,1,2,3,1,2,3]
print(b)

#3. 리스트 길이 구하기
#len함수 사용
a = [1,2,3]
print(len(a))  # 3개

#4. 리스트의 요소값 수정과 삭제
a = [1,2,3]
#    0 1 2
a[2] = 4
print(a)  # [1, 2, 4] 출력됨

#5. del함수 사용해 리스트 요소 삭제
a = [1,2,3]
del a[1]   # 1번째인덱스 위치의 값 2를 삭제 하여 새로운  [1,3]리스트를 되돌려 준다.
print(a)  # [1, 3]

#리스트 관련 함수

#1. 리스트에 요소 추가하기
#append(x) 함수는 리스트의 맨 마지막 위치에 x를 추가하는 함수 이다.
#예제
a = [1,2,3]
a.append(4)  # [1, 2, 3, 4]
print(a)
#예제
a.append([5,6])  #리스트의 맨 마지막 위치에 [5,6]리스트 추가 -> [1,2,3,4,[5,6]]

#2. 리스트에 저장된 요소 정렬
# short()함수는 리스트의 요소를 순서대로 정렬해 준다
#예제
a = [1,4,3,2]
a.sort()
print(a)   # [1, 2, 3, 4]

#3. 리스트에 저장된 요소값을 역순으로 뒤집기
# reverse()함수
#예제
a = ['a','c','b']
a.reverse()
print(a)  # ['b', 'c', 'a'] 출력됨

#4. 리스트 내부에 저장된 문자의 인덱스 위치 반환
# index(x) 함수는 리스트에 x값이 있으면 x의 인덱스 위치값을 돌려 준다.
#예제
a = [1,2,3]
#    0 1 2
print(a.index(3))  # 인덱스 위치 2를 반환 받아 출력
print(a.index(1))  # 인덱스 위치 0을 반환 받아 출력

#5. 리스트에 요소 삽입
# insert(a,b) 함수는  리스트의 a번째 위치에 b를 삽입하는 함수 이다.
#예제
a = [1,2,3]
#    0 1 2
a.insert(0,4)  # a[0]위치에 4 삽입
print(a)  # [4, 1, 2, 3]
#            0  1  2  3
a.insert(3,5)
print(a) # [4, 1, 2, 5, 3]
#           0  1  2  3  4

#6. 리스트 요소 제거
# remove(x) 함수는 리스트에서  첫번째로 존재하는 x를 삭제하는 함수 이다.
#예제
a = [1,2,3,1,2,3]
a.remove(3)  # a리스트는 3이라는 값을 2개 가지고 있을 경우  첫번째 3만 제거 함.
print(a)  # [1, 2, 1, 2, 3]

#7. 리스트 요소 끄집어 내기
#pop()함수는 리스트의 맨 마지막요소를 돌려주고  그요소는 삭제 한다.
a = [1,2,3]
print(a.pop())
print(a)

#pop(x)함수는 리스트의 x번째 요소를 돌려주고 그요소는 삭제 한다.
a = [1,2,3]
#    0 1 2
print(a.pop(1))  # 인덱스 위치 1에 존재 하는 2를 되돌려 받고  2를 삭제 한다.
print(a)  #다시 리스트 출력   [1,  3]

#8. 리스트에 포함된 요소x의 개수 세기
# count(x)함수는 리스트 안에 x가 몇개 있는지 조사하여 그 개수를 돌려주는 함수이다.
#예제
a = [1,2,3,1]
print(a.count(1)) #1이라는 값이 리스트a에 2개 들어 있으므로 2를 돌려 받아 2가 출력됨

#9. 리스트 확장
# extend(x) 함수에서 x에는 리스트만 올수 있으며 원래의  a리스트에 x리스트를 더하기 된다.
#예제
a = [1,2,3]
a.extend([4,5])
print(a)  #  [1, 2, 3, 4, 5] 하나로 합쳐진 리스트 출력
























































