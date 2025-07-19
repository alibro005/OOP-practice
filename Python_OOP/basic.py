# print("Hello World")
# print(20 * 2)

# print("hello", 3, 4, sep="~")

# a = 2
# b = True
# c = None
# d = 3.4

# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))

# a = "2"
# b = "4"
# print(int(a) + int(4))  # typecasting

# name="Muhammad Ali"

# print(name[0:9])  #including 0 but not 9
# print(len(name))

# print(name[0:-7])

"""
name="harry"
print(name[-4:-2])
# 1:3
print(len(name))

"""

# age = int(input("Enter your age : "))

# if (age>18):
#    print("You are able to vote")
# else:
#    print("Your are not able to vote")

# from re import match
# import time

# timestamp = time.strftime("%H:%M:%S")
# print(timestamp)
# timestamp = int(time.strftime("%H"))
# print(timestamp)
# timestamp = time.strftime("%M")
# print(timestamp)
# timestamp = time.strftime("%S")
# print(timestamp)

# if timestamp > 17:
#     print("Good Morning")
# elif timestamp > 12:
#     print("Good Evening")
# else:
#     print("Good Night")

# x = int(input("Enter x : "))

# match x:  # match case
#     case 0:
#         print("no. is zero")
#     case 4:
#         print("no. is four")
#     case _ if x != 2:
#         print("none match")  # default case
#     case _ if x != 3:
#         print(x, "3")


# colors = ["red", "green", "blue"]

# for color in colors:
#     print(color)
#     for i in color:
#         print(i)

# for k in range(6):
#     print(k)

# for k in range(0,10,2):
#     print(k)

def chai(n):
    print(n)

chai("Muahammad Ali Siddiqui")



# from index import chai
# import random

# print(random.ran(1,10))

# tea_varities = ["black", "Green", "Golong", "White"]


# print(tea_varities[1:3])        # slicing

# tea_varities[3] = "Herbal"
# print(tea_varities)
# tea_varities[1:2] = ["Lemon"]
# print(tea_varities)

# tea_varities.append("Oolong")
# print(tea_varities)

# age = 11


# if age == 12:
#     print("Child")


# numbers = [-1, 3, -4, 5, -4, 10, 2, -3]

# positive_num = 0

# for num in numbers:
#     if num > 0:
#         positive_num += 1
# print("Final count", positive_num)

# n = 10
# count_even = 0

# for i in range(1, n + 1):
#     if i % 2 == 0:
#         count_even += 1

# print("Sum of even no. is:",count_even)

# n = int(input("Enter n : "))

# for i in range(1, 11):
#     if i == 5:
#         continue
#     print(n, " * ", i, " = ", n * i)

# chai = "Hello"
# reversed = ""

# for i in chai:
#     reversed = i + reversed

# print(reversed)

# cube = lambda x: x**3;         # lambada function


# def sum_all(*args):  # multiple arguments
# print(args)  # tupple

# return sum(args)


# print(sum_all(1, 2))
# print(sum_all(1, 2, 3, 4, 5, 6, 7))

# mutable  list
# immutable  tuple


# def print_kwargs(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}:{value}")


# print_kwargs(name="ahmed", power="hi")


# def even_generator(limit):
#     for i in range(2, limit + 1, 2):
#         yield i


# for i in even_generator(10):
#     print(i)


# def factorial(n):
#     fact = 1
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n - 1)


# print("The factorial is: ", factorial(5))


class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def full_name(self):
        return f"{self.brand} {self.model} "

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size


# my_car = Car("Toyota", "Corolla")

# print(my_car.brand)
# print(my_car.model)

my_tesla = ElectricCar("Tesla","Model 5","85 kWh")
print(my_tesla.full_name())

