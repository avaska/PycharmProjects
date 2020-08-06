
def call_10_times(func):
    for i in range(10): #[0,1,2,3,4,5,6,7,8,9]
        func()

def print_hello():
    print("hihi")

call_10_times(print_hello)

