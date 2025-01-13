# x = 5
# y = 'Nicaise'
# print(x + y)
# print(x, y)

# x = 2
# y = 6
# z = complex(x, y)
# print(f'Complex nbr {z} has real {z.real} and imaginary {z.imag}.')

# import random
# print(random.random())
# print(random.randrange(1, 10))
# randList = [1, 4, 6,  8, 2]
# randList.sort(reverse=True)
# print(randList)
# print(random.choice(randList))

# a = 'Hello, World'
# print(a[1:7:2]) # [start: stop: len: skip(n-1)]
# print(a[::])
# b = 'banana'
# print('Letters in vsr b:')
# for letter in b:
#     print(letter)

# def o_area(r):
#     area = r * 3.14
#     print (f'The area for circle of radius {r} is {area: .2f}')
#     print('Radius is {}'.format(r))
# o_area(2)

# def myFunc(e):
#     return len(e)
# Lambda can have any number of args but ONLY 1 expression
# myFunc = lambda e: len(e)
# cars = ['BMW', 'Ford', 'Mitsubini', 'VM']
## Sorting
# cars.sort(key=myFunc)
# cars.sort(key=str.lower)
# cars.reverse()

## Copy
# list1 = cars.copy()
# list2 = list(cars)
# list3 = cars[:]
# print(cars)

# import json
# person = {
#     "name" : "Kirezi Nicaise",
#     "age" : 17,
#     "marrried" : True,
#     "cars" : [
#         {'car_name': 'Ford', 'year': 2005, 'car_price': 5000},
#         {'car_name': 'Mitsubishi', 'year': 2000, 'car_price': 3000},
#     ]
# }
# print(json.dumps(person, indent=True, sort_keys=True))

# f = open('hello.py', 'a')
# print(f.write("Hehe"))

# import os
# if os.path.exists('hello.py'):
#     f = open('hello.py', 'r')
#     print(f.readline())
# else:
#     print("hello.py doesn't exist")

x = 'A'
y = 'B'
z = 'C'
print(x,y,z)



