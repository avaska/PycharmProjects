

def test():
    print("test() 함수의 첫 줄입니다.")
    try:
        print("try구문이 실행되었습니다")
        # return
        # print("try구문의 return 키워드 뒤 입니다.")
    except:
        print("except구문이 실행되었습니다.")
    else:
        print("else구문이 실행되었습니다")
    finally:
        print("finally구문이 실행되었습니다")
    print("test()함수의 마지막 줄 입니다.")

test()

print('---------------------------------------')

def test2():
    print("test2() 함수의 첫 줄입니다.")
    try:
        print("try구문이 실행되었습니다")
        return
        print("try구문의 return 키워드 뒤 입니다.")
    except:
        print("except구문이 실행되었습니다.")
    else:
        print("else구문이 실행되었습니다")
    finally:
        print("finally구문이 실행되었습니다")
    print("test2()함수의 마지막 줄 입니다.")

test2()