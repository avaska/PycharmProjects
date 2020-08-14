
class Bird:
    def __init__(self):
        self.flying = True

    def birdsong(self):
        print("새소리")


class Sparrow(Bird): #상속

    #override
    def birdsong(self):
        print("짹짹")


my_pet = Sparrow()
print(my_pet.flying)
my_pet.birdsong()

#---------------------------------------------------------------------------------------------------

class Bird:
    def __init__(self):
        self.flying = True

    def birdsong(self):
        print("새소리")


class Sparrow(Bird): #상속

    #override
    def birdsong(self):
        print("짹짹")


class Chicken(Bird):
    def __init__(self):
        self.flying = False  #생성자 오버라이딩

    def birdsong(self):
        print("꼬꼬")

print('---------------------------------')

my_sparrow = Sparrow()
my_chicken = Chicken()

print(my_sparrow.flying)
my_sparrow.birdsong()

print(my_chicken.flying)
my_chicken.birdsong()
