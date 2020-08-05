
money = True

if money:
    print("택시를")
    print("타고")
    print("가라")

x = 3
y = 2
print(x > y)
print(x < y)

#3
money = 2000
if money >= 3000:
    print("택시 ㄱ")
else:
    print("걸어서")


money = 2000
card = True
if money >= 3000 or card:
    print("택시 ㄱ")
else:
    print("걸어서")

print(1 in [1,2,3])
print(1 not in [1,2,3])
print('a' in ('a','b','c'))
print('j' not in 'python')

pocket = ['paper', 'cellphone', 'money']
if 'money' in pocket:
    pass    #결과값 출력X
else:
    print("걸어서")


pocket = ['paper','handphone']
card = True
if 'money' in pocket:
    print("택시")
else:
    if card:
        print("택시")
    else:
        print("walk")


pocket = ['paper','handphone']
card = True
if 'money' in pocket:
    print("택시")
elif card:
    print("택시")
else:
    print("walk")

pocket = ['paper', 'money', 'cellphone']
if 'money' not in pocket: pass
else: print("카드를 꺼내라")


score = 80
if score >= 60:
    message = "success"
else:
    message = "failure"
print(message)

score = 50
message = "success" if score >= 60 else "failure"
print(message)


