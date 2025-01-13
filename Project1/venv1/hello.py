import random

# item_one=1
# item_two=2
# item_three=3
# total = item_one+\
#         item_two+\
#         item_three
# print(total)

# name1 = "ELissa"
# name2 = 'Elissa'
# name3 = '''Elissa'''
# print(name1 + ' ' + name2 + ' '+ name3)
''' 
How have u been
How have u been
How have u been
'''

"""
How have u been
How have u been
How have u been"""

# hey

# comma makes it a tuple
# a = b = c = 6,
# print(a)



# x = 3
# x = str(x)
# print(type(x))
# y = "3"
# y = int(y)
# print(type(y))

# x, y = 5, 10
# y, x = 5, 10
# a = 0
# a = x
# x = y
# y = a 
# print(x, y)

# nums = [1, 2, 3, 4, 5, 6]
# _, a, b, *rest = nums
# print(a, b, rest)

# a, b, c = "Joella", "Nicaise"
# print(a)

# names = ["Celia", "Joella", "Arsene", "Darlene", "Nicaise"]
# a, _, *tw, _ = names
# print(a)
# print(*tw)

# print(random.choice(names))
# print(names[1:5:2]) #[start 0: stop len: skip(n-1)]
# h = "Hello World!"
# print(h[::-1])

# a = 36
# b = 380000
# c = 1000
# msg = f"I am {a} old and I have a $ {b} salary"
# msg1 = "I am {age} old and I have a $ {balance} salary".format(age = a, balance = b)
# msg2 = "I am {0} old and I have a $ {1} salary".format(a, b)
# msg3 = "I am {} old and I have a $ {} salary".format(a, b)
# msg4 = "I've got $ {:,}".format(a+b)
# msg5 = "I've got $ {:,.2f}".format(a+b+c)
# msg6 = f"I am {'old' if a>18 else 'young'}"
# print(msg6)
# print(msg1)
# print(msg2)
# print(msg4)
# print(msg5)


# lst = ['a', 'b', 'c', 'd', 'e', 'f']
# lst[1:3] = [1, 2, 3, 4]
# lst[1] = [1, 2, 3, 4]
# lst[1:4] = "Hello"
# lst.remove('H')
# print(lst)

# lst = ["Nicaise", "Joella", "Belynda"]
# print([item for item in lst])
# print([item for item in lst if "i" in item])
# [print(item) for item in lst if "a" in item]

# SORTING BY NAME LENs
# def nameLen(name):
#     return len(name.lower())

# names = ["Edwige", "Nicaise", "joella", "Belynda"]
# names.sort(key=nameLen)
# print(names)

# def myFunc(**food):
#     print("i love " + food["tropical"])
# myFunc(tropical = "banana", equatorial = "avocado")

# def myFunc(**food):
#     return food['fruits']

# print(myFunc(fruits=["banana", "mango"], vegetables=[1, 2, 3]))


# Think about type conversion and come up with ideas!
# Extract imaginary and real part of a complex number
# Arithmetic Operations on complex numbers


# cars = [
# {
# 'Gasabo': [
# {'car_name': 'Ford', 'year': 2005, 'car_price': 5000, 'car_owner': 'Alice'},
# {'car_name': 'Mitsubishi', 'year': 2000, 'car_price': 3000, 'car_owner': 'Bob'},
# {'car_name': 'BMW', 'year': 2019, 'car_price': 25000, 'car_owner': 'Charlie'},
# {'car_name': 'VW', 'year': 2011, 'car_price': 12000, 'car_owner': 'David'}
# ]
# },
# {
# 'Kicukiro': [
# {'car_name': 'Toyota', 'year': 2018, 'car_price': 22000, 'car_owner': 'Eve'},
# {'car_name': 'Honda', 'year': 2015, 'car_price': 18000, 'car_owner': 'Frank'},
# {'car_name': 'Subaru', 'year': 2020, 'car_price': 27000, 'car_owner': 'Grace'},
# {'car_name': 'Nissan', 'year': 2017, 'car_price': 20000, 'car_owner': 'Heidi'}
# ]
# },
# {
# 'Nyarugenge': [
# {'car_name': 'Chevrolet', 'year': 2016, 'car_price': 15000, 'car_owner': 'Ivan'},
# {'car_name': 'Hyundai', 'year': 2019, 'car_price': 21000, 'car_owner': 'Judy'},
# {'car_name': 'Kia', 'year': 2021, 'car_price': 23000, 'car_owner': 'Kevin'},
# {'car_name': 'Mazda', 'year': 2014, 'car_price': 16000, 'car_owner': 'Laura'}
# ]
# }
# ]

# print(cars)

cars = [
    {'district': 'Gasabo', 'car_name': 'Ford', 'year': 2005, 'car_price': 5000, 'car_owner': 'Alice'},
    {'district': 'Gasabo', 'car_name': 'Mitsubishi', 'year': 2000, 'car_price': 3000, 'car_owner': 'Bob'},
    {'district': 'Gasabo', 'car_name': 'BMW', 'year': 2019, 'car_price': 25000, 'car_owner': 'Charlie'},
    {'district': 'Gasabo', 'car_name': 'VW', 'year': 2011, 'car_price': 12000, 'car_owner': 'David'},
    {'district': 'Kicukiro', 'car_name': 'Toyota', 'year': 2018, 'car_price': 22000, 'car_owner': 'Eve'},
    {'district': 'Kicukiro', 'car_name': 'Honda', 'year': 2015, 'car_price': 18000, 'car_owner': 'Frank'},
    {'district': 'Kicukiro', 'car_name': 'Subaru', 'year': 2020, 'car_price': 27000, 'car_owner': 'Grace'},
    {'district': 'Kicukiro', 'car_name': 'Nissan', 'year': 2017, 'car_price': 20000, 'car_owner': 'Heidi'},
    {'district': 'Nyarugenge', 'car_name': 'Chevrolet', 'year': 2016, 'car_price': 15000, 'car_owner': 'Ivan'},
    {'district': 'Nyarugenge', 'car_name': 'Hyundai', 'year': 2019, 'car_price': 21000, 'car_owner': 'Judy'},
    {'district': 'Nyarugenge', 'car_name': 'Kia', 'year': 2021, 'car_price': 23000, 'car_owner': 'Kevin'},
    {'district': 'Nyarugenge', 'car_name': 'Mazda', 'year': 2014, 'car_price': 16000, 'car_owner': 'Laura'}
]

# 2. bubble sort
# sorted_by_price = cars[:]  
# for i in range(len(sorted_by_price)):
#     for j in range(0, len(sorted_by_price) - i - 1):
#         if sorted_by_price[j]['car_price'] > sorted_by_price[j + 1]['car_price']:
#             sorted_by_price[j], sorted_by_price[j + 1] = sorted_by_price[j + 1], sorted_by_price[j]
# print(sorted_by_price)

# 2. using a func
# def get_price(car):
#     return car['car_price']
# def sort_by_price(cars):
#     return sorted(cars, key=get_price)
# sorted_by_price = sort_by_price(cars)
# print(sorted_by_price)

# 3. use function
# total_car_price = 0
# def get_car_price(car):
#     return car['car_price']
# def sum_cars(cars):
#     return sum(map(get_car_price, cars))
# total_car_price = sum_cars(cars)
# print(total_car_price)

# 3. total price
# total_car_price = 0
# for car in cars:
#     total_car_price += car['car_price']
# print(total_car_price)

# 4. no loop
# total_car_price_nyarugenge = 0
# def get_car_price(car):
#     return car['car_price'] if car['district'] == "Nyarugenge" else 0
# def sum_cars(cars):
#     return sum(map(get_car_price, cars))
# total_car_price_nyarugenge = sum_cars(cars)
# print(total_car_price_nyarugenge)

# 4. total price
# total_nyarugenge_price = 0
# for car in cars:
#     if car['district'] == "Nyarugenge":
#         total_nyarugenge_price += car['car_price']
# print(total_nyarugenge_price)

# 5. location of cheapest car
# print(sorted_by_price[0]['district'])

# 6. func print_names
# def get_names(car):
#     return car['car_name']
# def print_names(cars):
#     return list(map(get_names, cars))
# car_names = print_names(cars)
# # sort them
# car_names.sort()
# print(car_names)

# # 6. print car names
# print simply
# for car in cars:
#     print(car['car_name'])
# assigned to a variable
# car_names = [car['car_name'] for car in cars]
# print(car_names)

# # 7. add new list
# brand_new = ['Audi', 'Tesla']
# car_names.sort()
# car_names.extend(brand_new)
# print(car_names)

# # 8. Get all except first
# car_except_first = car_names[1:]
# print(car_except_first)

# # 9. assign vars to 1st and 2nd
# cars_name1, cars_name2, *_ = car_names
# print(cars_name1, cars_name2)

# # 10. assign vars to 1st and 2nd and rest as list
# cars_name1, cars_name2, *rest = car_names
# print(cars_name1, cars_name2, rest)

# # 11. replacing slice
# car_names[1:4] = ['Tesla', 'Volvo']
# print(car_names)

# # 12. replacing slice
# car_names[1] = ['Tesla', 'Volvo']
# print(car_names)

# # 13. replace 3rd 
# car_names[2] = 'Hybrid car'
# print(car_names)

# # 14. replace 3rd 
# eCar='Electric Car'
# car_names[1:4] = eCar
# print(car_names)



# one = 1
# two = "two"
# three = "three"
# print(one,two)



