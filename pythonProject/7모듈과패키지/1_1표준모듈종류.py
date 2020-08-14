
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


