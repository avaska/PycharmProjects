class Dog:
    #속성(변수) 선언
    name = "삼식이"
    age = 3
    breed = "골든 리트리버"
    #메소드 선언
    def bark(self):    #self => this 역할
        print(self.name + "가 멍멍하고 짖는다.")

my_dog = Dog()

print(my_dog.breed)
my_dog.bark()