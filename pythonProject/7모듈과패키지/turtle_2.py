
#마음대로 걷는 거북이
import turtle as t
import random

#거북이 모양 그래픽 사용
t.shape("turtle")
t.speed(0)

for x in range(500):
    #0~499를 요소로 받는 리스트 생성
    # 1 ~ 360 사이의 임의의 수를 골라 a 변수에 저장
    a = random.randint(1, 360)
    #a변수에 저장된 각도로 거북이의 방향을 회전
    t.setheading(a)
    #거북이를 10만큼 앞으로 이동시켜 선을 긋는다
    t.forward(10)