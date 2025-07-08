# x = 10;
# # print(x);

# x = [3,4,32,443,4];
# for i in range(0, len(x)):
#     print(x[i])


# class student:
#     name = "Ali"

# s1 = student()
# print(s1.name)
# s2 = student()
# print(s2.name)


# class student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

#     def get_avg(self):        # non-static methode
#         sum = 0
#         for val in self.marks:
#             sum += val
#         print("Hi", self.name, "your average score is:", sum / 3)


# s1 = student("Ali", [40, 90, 50])
# s1.get_avg()

# s1.name="Ahmed"
# s1.get_avg()


# class Account:
#     def __init__(self, bal, acc):
#         self.balance = bal
#         self.account = acc

#     def debit(self, amount):
#         self.balance -= amount
#         print("RS:", amount, "was debited")
#         print("total balance = ", self.get_balance())

#     def credit(self, amount):
#         self.balance += amount
#         print("RS:", amount, "was credited")
#         print("total balance = ", self.get_balance())

#     def get_balance(self):
#         return self.balance


# s1 = Account(1000, 1234)
# s1.debit(500)
# s1.credit(2000)


# class Car:
#     def __init__(self, brand, model, year):
#         self.brand = brand
#         self.model = model
#         self.year = year


# Car1 = Car("Corolla", 2021, 2025)
# print(Car1.brand)

# print(Car1.year)


# class Animal:
#     def speak(self):
#         return "Some sound"

# class Dog(Animal):
#     def speak(self):
#         return "Bark"


# class car:
#     def __init__(self,color,model):
#         self.color = color
#         self.model = model

#     def display(self):
#         print(self.color,self.model)

# my_car = car("Red","Tesla")
# my_car.display()


# class BankAccount:

#     def __init__(self, name, balance):
#         self.name = name  # public
#         self.__balance = balance  # private

#     def deposit(self, amount):
#         self.__balance = amount  # private

#     def get__balance(self):

#         return self.__balance


# account = BankAccount("Alice", 1000)
# print("Initial Balance:", account.get__balance())

# account.deposit(500)
# print("After Deposit:", account.get__balance())


# class Student:

#     def __init__(self, name):
#         self.__name = name

#     def get_name(self):
#         return self.__name

#     def set__name(self, new_name):
#         self.__name = self.__new_name


# class Robot:
#     def __init__(self, name, battery_level):
#         self.name = name
#         self.__battery_level = battery_level

#     def say_hello(self):
#         print("Hello,I am ", self.name)

#     def get_battery_level(self):
#         return self.__battery_level

#     def set_battery_level(self, new_level):
#         if 0 <= new_level <= 100:
#             self.__battery_level = new_level
#         else:
#             print("Battey level must be between 0 and 100")


# r1 = Robot("Robo", 75)
# r1.say_hello()
# print("Battery level", r1.get_battery_level())
# r1.set_battery_level(100)
# print("Updated Battery level", r1.get_battery_level())

# class Robot:
#    def __init__(self,name,battery_level):
#     self.name=name
#     self._battery_level=battery_level

#     def say_hello (self):
#       print(f"hello,I AM{self.name}!")


# class Student:
#     def __init__(self, name="unknown", age=0):
#         self.name = name
#         self.age = age

#     def display(self):
#         print("Name:", self.name, "Age:", self.age)


# s1 = Student()
# s2 = Student("Alice", 12)

# s1.display()
# s2.display()


# class Student:
#     def __init__(self, name, grade):
#         self.name = name
#         self.grade = grade

#     @classmethod
#     def from_dict(cls, data):
#         return cls(data["name"], data["grade"])

#     @classmethod
#     def from_string(cls, data_str):
#         name, grade = data_str.split(",")
#         return cls(name.strip(), int(grade.strip()))


# s1 = Student("John", 8)
# s2 = Student.from_dict({"name": "Emma", "grade": 7})
# s3 = Student.from_string("Liam, 6")


# print(s1.name, s1.grade)  # John 8
# print(s2.name, s2.grade)  # Emma 7
# print(s3.name, s3.grade)  # Liam 6


# class Student:
#     def __init__(self, name="unknown", age=0):
#         self.name = name
#         self.age = age

#     def display(self):
#         print(f"Name: {self.name}, Age:{self.age}")


# s1 = Student()
# s2 = Student("Alice", 12)

# s1.display()
# s2.display()


# class Student:
#     def __init__(self, *args):
#         if len(args) == 0:
#             self.name = "Unknown"
#             self.age = 0
#         elif len(args) == 1:
#             self.name = args[0]
#             self.age = 0
#         elif len(args) == 2:
#             self.name = args[0]
#             self.age = args[1]

#     def show(self):
#         print(f"Name: {self.name}, Age: {self.age}")


# s1 = Student()
# s2 = Student("Ali")
# s3 = Student("Imad", 20)

# s1.show()
# s2.show()
# s3.show()


# class Car:
#     def __init__(self, make, model, year):

#         self.make = make
#         self.model = model
#         self.year = year


# car = Car("Honda", "Civic", 2022)

# print(car.make)
# print(car.model)
# print(car.year)


# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def display(self):
#         print(f" Name : {self.name}, Age : {self.age}")


# student1 = Student("Ali", 12)
# student2 = Student("Ahmed", 14)

# student1.display()
# student2.display()


# class Animal:
#     def speak(self):
#         print("Animal speaks")


# class Dog(Animal):
#     def bark(self):
#         print("Dog barks")


# d = Dog()
# d.speak()
# d.bark()


# class Father:
#     def skils(self):
#         print("Father: Gardening and Painting")


# class Mother:
#     def skills(self):
#         print("Mother: Cooking and Singing")


# class Child(Father, Mother):
#     def my_skills(self):
#         print("Child: Playing Football")


# c = Child()
# c.skils()
# c.skills()
# c.my_skills()

# Code to demonstrate Composition

# Class Salary in which we are
# declaring a public method annual salary
# class Salary:
#     def __init__(self, pay, bonus):
#         self.pay = pay
#         self.bonus = bonus

#     def annual_salary(self):
#         return (self.pay*12)+self.bonus


# # Class EmployeeOne which does not
# # inherit the class Salary yet we will
# # use the method annual salary using
# # Composition
# class EmployeeOne:
#     def __init__(self, name, age, pay, bonus):
#         self.name = name
#         self.age = age

#         # Making an object in which we are
#         # calling the Salary class
#         # with proper arguments.
#         self.obj_salary = Salary(pay, bonus)  # composition

#     # Method which calculates the total salary
#     # with the help of annual_salary() method
#     # declared in the Salary class
#     def total_sal(self):
#         return self.obj_salary.annual_salary()

# # Making an object of the class EmployeeOne
# # and providing necessary arguments
# emp = EmployeeOne('Geek', 25, 10000, 1500)

# # calling the total_sal method using
# # the emp object
# print(emp.total_sal())


# class Salary:
#     def __init__(self, pay, bonus):
#         self.pay = pay
#         self.bonus = bonus


# class EmployeeOne:
#     def __init__(self, name, age, sal):
#         self.name = name
#         self.age = age

#         self.agg_salary = sal

#     def total_sal(self):
#         return self.agg_salary.annual_salary()


# salary = Salary(10000, 1500)
# emp = EmployeeOne("Geek", 25, salary)

# print(emp.total_sal())


# class Book:
#     def __init__(self, title, author):
#         self.title = title
#         self.author = author

#     def info(self):
#         return f"{self.title} by {self.author}"


# class Library:
#     def __init__(self):
#         self.books = []

#     def add_book(self, book):
#         # new_book = Book(title, author)  # composition

#         self.books.append(book)

#     def show_books(self):
#         for book in self.books:
#             print(book.info())


# lib = Library()
# lib.add_book("Harry Potter", "J.K. Rowling")
# lib.add_book("The Hobbit", "J.R.R. Tolkien")

# lib.show_books()


# book1 = Book("Harry Potter", "J.K. Rowling")
# book2 = Book("The Hobbit", "J.R.R. Tolkien")

# lib = Library()
# lib.add_book(book1)
# lib.add_book(book2)

# lib.show_books()


# class Circle:
#     def area(self, radius):
#         return 3.14 * radius * radius

# class Square:
#     def area(self, side):
#         return side * side


# circle1 = Circle()
# square1 = Square()

# circle_area = circle1.area(5)
# square_area = square1.area(4)

# print("Area of Circle:", circle_area)
# print("Area of Square:", square_area)


# class Shape:
#     def area(self):
#         pass

#     def print_area(self):
#         print(f"Area: {self.area()}")

# class Circle(Shape):
#     def _init_(self, radius):
#         self.radius = radius

#     def area(self):
#         return 3.14 * self.radius * self.radius

# class Square(Shape):
#     def _init_(self, side):
#         self.side = side

#     def area(self):
#         return self.side * self.side

# class Circle:
#     def area(self, radius):
#         return 3.14 * radius * radius

# class Square:
#     def area(self, side):
#         return side * side


# circle1 = Circle()
# square1 = Square()

# circle_area = circle1.area(5)
# square_area = square1.area(4)

# print("Area of Circle:", circle_area)
# print("Area of Square:", square_area)

# a = 257
# b = 257
# print(a is b)

# Operator Overloading in Python

# class Vector:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#     def __str__(self):
#          return "Vector(%d, %d)" % (self.a, self.b)
#     def __add__(self, other):
#         return Vector(self.a + other.a, self.b + other.b)

# v1 = Vector(2, 10)
# v2 = Vector(5, -2)
# print(v1 + v2)

# METHOD OVERLOADING In PYTHON

# class Display:
#     def show(self, a=None, b=None):
#         if a is not None and b is not None:
#             print(f"Two values: {a} and {b}")
#         elif a is not None:
#             print(f"One value: {a}")
#         else:
#             print("No value provided")
        
# d = Display()

# d.show()           # Output: No value provided
# d.show(10)         # Output: One value: 10
# d.show(10, 20)     # Output: Two values: 10 and 20


# class Math:
#     def add(self, *args):
#         return sum(args)

# m = Math()

# print(m.add())             # Output: 0
# print(m.add(5))            # Output: 5
# print(m.add(1, 2, 3, 4))   # Output: 10

